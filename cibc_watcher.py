import os
import time
import pandas as pd
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# === CONFIGURATION ===
WATCH_FOLDER = r"C:\Users\SalihAl-Tak\OneDrive - adam-tools.com\Desktop\Bank_statements\CIBC"
OUTPUT_FOLDER = r"C:\Users\SalihAl-Tak\OneDrive - adam-tools.com\Desktop\Bank_statements\PROCESSED"
processed_files = {}

# === CLEANING FUNCTION ===
def clean_cibc_csv(file_path):
    print(f"🔧 Processing CIBC CSV: {file_path}")
    df = pd.read_csv(file_path)

    # Clean column names
    df.columns = [col.strip() for col in df.columns]
    
    # Handle different CIBC CSV formats
    if len(df.columns) >= 4:
        # New format: Date, Description, Outflow (Column C), Inflow (Column D)
        df.rename(columns={
            df.columns[0]: "Date",
            df.columns[1]: "Description", 
            df.columns[2]: "Outflow",  # Column C
            df.columns[3]: "Inflow"    # Column D
        }, inplace=True)
    else:
        # Fallback for different formats
        print(f"⚠️ Unexpected CIBC format with {len(df.columns)} columns")
        return

    # Convert amounts to numeric
    df["Outflow"] = pd.to_numeric(df["Outflow"], errors="coerce").fillna(0)
    df["Inflow"] = pd.to_numeric(df["Inflow"], errors="coerce").fillna(0)

    # Remove rows with no transaction amount
    df = df[(df["Outflow"] != 0) | (df["Inflow"] != 0)]

    # Convert date column
    df["Date"] = pd.to_datetime(df["Date"], errors="coerce")

    # Clean up and select final columns - keep separate Inflow and Outflow
    df = df[["Date", "Description", "Inflow", "Outflow"]].dropna()

    # Add source identifier and merchant column
    df["Source"] = "CIBC"
    df["Merchant"] = df["Description"]  # Use description as merchant for now

    # Save cleaned CSV
    base_name = os.path.splitext(os.path.basename(file_path))[0]
    output_path = os.path.join(OUTPUT_FOLDER, f"{base_name}_cibc_cleaned.csv")
    df.to_csv(output_path, index=False)

    print(f"✅ Cleaned CIBC CSV saved to: {output_path}")
    print(f"📊 Processed {len(df)} transactions")


# === FILE WATCHER ===
class CSVWatcher(FileSystemEventHandler):
    def on_created(self, event):
        self.process(event)

    def on_modified(self, event):
        self.process(event)

    def process(self, event):
        print(f"[DEBUG] Detected file event: {event.src_path}")
        if event.is_directory or not event.src_path.lower().endswith(".csv"):
            return

        path = event.src_path
        now = time.time()

        if path in processed_files and now - processed_files[path] < 10:
            print(f"[DEBUG] Skipping recently processed: {path}")
            return

        processed_files[path] = now

        # Try multiple times in case file is locked
        for attempt in range(5):
            try:
                clean_cibc_csv(path)
                break
            except PermissionError:
                print(f"[WAIT] File locked, retrying... ({attempt + 1}/5)")
                time.sleep(1)


# === MAIN LOOP ===
def start_watching():
    if not os.path.exists(OUTPUT_FOLDER):
        os.makedirs(OUTPUT_FOLDER)

    print(f"👀 Watching: {WATCH_FOLDER}")
    observer = Observer()
    observer.schedule(CSVWatcher(), path=WATCH_FOLDER, recursive=False)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

if __name__ == "__main__":
    start_watching()
