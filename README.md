# Finance App - Personal Finance Management System

A comprehensive personal finance management system that automates bank statement processing, categorizes transactions, and provides detailed financial analytics through an intuitive web interface.

## Features

### 🔄 Automated Bank Statement Processing
- **CIBC Integration**: Automated CSV processing with file watcher
- **AMEX Integration**: XLS file processing with xlwings
- **Real-time Monitoring**: Automatic file detection and processing

### 📊 Transaction Management
- **Excel-like Editing**: Inline editing of transaction data
- **Smart Categorization**: Automatic transaction categorization based on merchant keywords
- **Separate Inflow/Outflow Tracking**: Clear separation of money in vs money out
- **Data Validation**: Real-time data validation and error handling

### 📈 Financial Analytics
- **Monthly Summaries**: Detailed inflow/outflow analysis by month
- **Visual Analytics**: Interactive charts and graphs using Plotly
- **Master Tracker**: Comprehensive financial overview
- **Export Capabilities**: Excel file generation with multiple sheets

### 💾 Data Persistence
- **Session Management**: Current session data handling
- **Master Database**: Persistent storage of all transactions
- **Data Merging**: Automatic duplicate removal and data consolidation
- **Backup System**: JSON-based data storage

## Technology Stack

- **Frontend**: Streamlit (Python web framework)
- **Backend**: Python with pandas for data processing
- **File Processing**: 
  - xlwings for Excel file handling
  - pandas for CSV processing
  - watchdog for file system monitoring
- **Data Visualization**: Plotly for interactive charts
- **Data Storage**: JSON files for persistence

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd Financeapp
```

2. Create and activate virtual environment:
```bash
python -m venv myenv
# Windows
myenv\Scripts\activate
# macOS/Linux
source myenv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

### Running the Main Application
```bash
streamlit run main.py
```

### File Watchers
- **CIBC Watcher**: `python cibc_watcher.py`
- **AMEX Watcher**: `python exceltocsv.py`

### Configuration
- Update file paths in `cibc_watcher.py` and `exceltocsv.py` to match your bank statement folders
- Modify `categories.json` to customize transaction categorization

## File Structure

```
Financeapp/
├── main.py                 # Main Streamlit application
├── cibc_watcher.py         # CIBC CSV file processor
├── exceltocsv.py          # AMEX XLS file processor
├── run_converter.bat      # Batch file to run converters
├── categories.json        # Transaction categorization rules
├── transactions_data.json # Persistent transaction storage
├── Finance_App_PRD.md     # Product Requirements Document
├── README.md              # This file
├── .gitignore             # Git ignore rules
└── myenv/                 # Virtual environment
```

## Data Format

### CIBC CSV Format
- Date, Description, Outflow (Column C), Inflow (Column D)
- Processed files: `filename_cibc_cleaned.csv`

### AMEX XLS Format
- Date, Description, Amount
- All amounts treated as outflows (expenses)
- Processed files: `filename_amex_cleaned.csv`

### Streamlit Input
- Date, Description, Inflow, Outflow, Source, Merchant, Category

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## License

This project is for personal use. Please ensure you comply with your bank's terms of service when processing bank statements.

## Security Note

- Bank statement data is stored locally only
- No data is transmitted to external servers
- Ensure your local files are properly secured
- The `.gitignore` file excludes sensitive data files

## Support

For issues or questions, please create an issue in the repository or contact the maintainer.
