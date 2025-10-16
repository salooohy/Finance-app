import os
import time
import pandas as pd
import xlwings as xw
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# === USER CONFIGURATION ===
WATCH_FOLDER = r"C:\Users\SalihAl-Tak\OneDrive - adam-tools.com\Desktop\Bank_statements\AMEX"
OUTPUT_FOLDER = r"C:\Users\SalihAl-Tak\OneDrive - adam-tools.com\Desktop\Bank_statements\PROCESSED"

# === RECENT FILES TRACKER FOR DEBOUNCING ===
processed_files = {}

# === FUNCTION TO PROCESS .XLS FILE ===
def process_xls(file_path):
    try:
        print(f"🔧 Processing: {file_path}")
        app = xw.App(visible=False)
        wb = app.books.open(file_path)
        sheet = wb.sheets[0]

        # Read from row 15 onward (skip rows 1–14)
        data = sheet.range("A12").options(expand="table").value
        wb.close()
        app.quit()

        # Convert to DataFrame
        df = pd.DataFrame(data[1:], columns=data[0])
        df.dropna(how="all", inplace=True)

        # Clean column names
        df.columns = [col.strip() for col in df.columns]

        # Clean and filter 'Amount' column
        if "Amount" in df.columns:
            df["Amount"] = (
                df["Amount"]
                .astype(str)
                .str.replace("$", "", regex=False)
                .str.replace(",", "", regex=False)
                .str.strip()
            )
            df["Amount"] = pd.to_numeric(df["Amount"], errors="coerce")
            # For AMEX credit card, all amounts are outflows
            df["Outflow"] = df["Amount"].abs()  # All AMEX transactions are outflows
            df["Inflow"] = 0  # No inflows for credit card

        # Clean and parse 'Date' column
        if "Date" in df.columns:
            df["Date"] = df["Date"].astype(str).str.replace(".", "", regex=False)
            df["Date"] = pd.to_datetime(df["Date"], format="%d %b %Y", errors="coerce")

        # Add source identifier and merchant column
        df["Source"] = "AMEX"
        if "Merchant" not in df.columns:
            df["Merchant"] = "AMEX Transaction"  # Default merchant name

        # Select final columns - keep separate Inflow and Outflow
        final_columns = ["Date", "Description", "Inflow", "Outflow", "Source", "Merchant"]
        df = df[final_columns].dropna()

        # Save cleaned data as CSV
        base_name = os.path.splitext(os.path.basename(file_path))[0]
        output_path = os.path.join(OUTPUT_FOLDER, f"{base_name}_amex_cleaned.csv")
        df.to_csv(output_path, index=False)
        print(f"✅ Saved to: {output_path}")

    except Exception as e:
        print(f"❌ Error processing {file_path}: {e}")



# === FILE WATCHER ===
class XLSWatcher(FileSystemEventHandler):
    def on_created(self, event):
        self.process(event)

    def on_modified(self, event):
        self.process(event)

    def process(self, event):
        if event.is_directory or not event.src_path.lower().endswith(".xls"):
            return

        path = event.src_path
        now = time.time()

        # Debounce: skip if processed in the last 10 seconds
        if path in processed_files and now - processed_files[path] < 10:
            return

        processed_files[path] = now
        print(f"[DEBUG] Processing file: {path}")
        process_xls(path)

# === MAIN LOOP ===
def start_watching():
    if not os.path.exists(OUTPUT_FOLDER):
        os.makedirs(OUTPUT_FOLDER)

    print(f"👀 Watching: {WATCH_FOLDER}")
    observer = Observer()
    observer.schedule(XLSWatcher(), path=WATCH_FOLDER, recursive=False)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

if __name__ == "__main__":
    start_watching()
