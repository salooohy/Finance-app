# Finance App - Product Requirements Document (PRD)

## 1. Executive Summary

The Finance App is a comprehensive personal finance management system designed to automate bank statement processing, categorize transactions, and provide detailed financial analytics. The application consists of three main components: automated file watchers for bank statement processing, a Streamlit-based web dashboard for transaction management, and data persistence capabilities.

## 2. Product Overview

### 2.1 Vision
To create an automated, user-friendly personal finance management system that eliminates manual data entry and provides comprehensive financial insights through intelligent categorization and analytics.

### 2.2 Mission
Simplify personal finance management by automatically processing bank statements, categorizing transactions, and providing actionable financial insights through an intuitive web interface.

### 2.3 Target Users
- Individuals managing personal finances
- Users with multiple bank accounts (CIBC, AMEX)
- People seeking automated transaction categorization
- Users requiring monthly financial summaries and exports

## 3. Product Features

### 3.1 Core Features

#### 3.1.1 Automated Bank Statement Processing
- **File Watchers**: Real-time monitoring of bank statement folders
  - CIBC CSV file processing (`cibc_watcher.py`)
  - AMEX XLS file processing (`exceltocsv.py`)
- **Data Cleaning**: Automatic standardization of transaction formats
- **Output Generation**: Processed files saved to designated folders

#### 3.1.2 Transaction Management Dashboard
- **File Upload**: CSV file upload interface
- **Excel-like Editing**: Inline editing of transaction data
- **Smart Categorization**: Automatic transaction categorization based on merchant keywords
- **Data Validation**: Real-time data validation and error handling

#### 3.1.3 Financial Analytics
- **Expense Tracking**: Detailed expense categorization and totals
- **Monthly Summaries**: Inflow/outflow analysis by month
- **Visual Analytics**: Interactive charts and graphs using Plotly
- **Export Capabilities**: Excel file generation with multiple sheets

#### 3.1.4 Data Persistence
- **Session Management**: Current session data handling
- **Master Database**: Persistent storage of all transactions
- **Data Merging**: Automatic duplicate removal and data consolidation
- **Backup System**: JSON-based data storage

### 3.2 Advanced Features

#### 3.2.1 Category Management
- **Dynamic Categories**: Add/edit expense categories
- **Keyword Learning**: Automatic merchant-to-category mapping
- **Custom Rules**: User-defined categorization rules

#### 3.2.2 Multi-Account Support
- **CIBC Integration**: Automated CSV processing
- **AMEX Integration**: XLS file processing with xlwings
- **Unified View**: Combined transaction history across accounts

#### 3.2.3 Reporting & Export
- **Master Excel Files**: Comprehensive monthly summaries
- **Transaction Details**: Complete transaction history
- **Formatted Reports**: Professional Excel formatting with charts

## 4. Technical Architecture

### 4.1 Technology Stack
- **Frontend**: Streamlit (Python web framework)
- **Backend**: Python with pandas for data processing
- **File Processing**: 
  - xlwings for Excel file handling
  - pandas for CSV processing
  - watchdog for file system monitoring
- **Data Visualization**: Plotly for interactive charts
- **Data Storage**: JSON files for persistence

### 4.2 System Components

#### 4.2.1 File Watchers
```
cibc_watcher.py - Monitors CIBC CSV files
exceltocsv.py - Processes AMEX XLS files
```

#### 4.2.2 Main Application
```
main.py - Streamlit dashboard application
```

#### 4.2.3 Data Files
```
categories.json - Category definitions and keywords
transactions_data.json - Persistent transaction storage
master_finance_tracker.xlsx - Generated Excel reports
```

### 4.3 Data Flow
1. Bank statements downloaded to monitored folders
2. File watchers detect new files and process them
3. Cleaned data saved to processed folders
4. Users upload processed files to dashboard
5. Transactions categorized and edited in web interface
6. Data appended to master database
7. Reports generated and exported

## 5. User Interface Design

### 5.1 Dashboard Layout
- **Header**: Application title and status indicators
- **File Upload**: Drag-and-drop CSV file upload
- **Tabbed Interface**: 
  - Outflow (expenses) management
  - Inflow (income) tracking
  - Master Tracker (monthly summaries)

### 5.2 Key Interface Elements
- **Data Editor**: Excel-like editing with column configuration
- **Category Management**: Add/edit categories interface
- **Summary Views**: Real-time expense summaries
- **Export Buttons**: One-click Excel file generation
- **Visual Charts**: Interactive pie charts for expense breakdown

## 6. User Stories

### 6.1 Primary User Stories
1. **As a user**, I want to automatically process my bank statements so that I don't have to manually enter transactions.
2. **As a user**, I want to categorize my expenses automatically so that I can track my spending patterns.
3. **As a user**, I want to edit transactions like in Excel so that I can correct errors and split bills.
4. **As a user**, I want to see monthly summaries so that I can understand my financial trends.
5. **As a user**, I want to export my data to Excel so that I can create custom reports.

### 6.2 Secondary User Stories
1. **As a user**, I want to add custom categories so that I can organize my expenses according to my needs.
2. **As a user**, I want to see visual charts so that I can quickly understand my spending patterns.
3. **As a user**, I want to delete incorrect transactions so that my data remains accurate.
4. **As a user**, I want to track both income and expenses so that I can see my net financial position.

## 7. Success Metrics

### 7.1 Functional Metrics
- **Processing Accuracy**: 95%+ correct transaction categorization
- **Processing Speed**: < 30 seconds for 1000+ transactions
- **Data Integrity**: Zero data loss during processing
- **Export Success**: 100% successful Excel file generation

### 7.2 User Experience Metrics
- **Time to First Insight**: < 2 minutes from file upload to summary view
- **Error Rate**: < 5% user errors during transaction editing
- **User Satisfaction**: Positive feedback on Excel-like editing experience

## 8. Technical Requirements

### 8.1 Performance Requirements
- **Response Time**: < 3 seconds for dashboard interactions
- **File Processing**: Handle files up to 10MB
- **Concurrent Users**: Support single-user operation
- **Data Storage**: Efficient JSON-based persistence

### 8.2 Compatibility Requirements
- **Operating System**: Windows 10/11
- **Python Version**: 3.8+
- **Browser Support**: Chrome, Firefox, Edge (latest versions)
- **File Formats**: CSV, XLS, XLSX

### 8.3 Security Requirements
- **Data Privacy**: Local data storage only
- **File Validation**: Input validation for uploaded files
- **Error Handling**: Graceful error handling and user feedback

## 9. Implementation Roadmap

### 9.1 Phase 1: Core Functionality (Completed)
- ✅ File watchers for bank statement processing
- ✅ Basic Streamlit dashboard
- ✅ Transaction categorization system
- ✅ Excel export functionality

### 9.2 Phase 2: Enhanced Features (Current)
- 🔄 Improved user interface
- 🔄 Advanced analytics
- 🔄 Better error handling
- 🔄 Performance optimizations

### 9.3 Phase 3: Future Enhancements
- 📋 Multi-user support
- 📋 Advanced reporting features
- 📋 Mobile-responsive design
- 📋 API integration for real-time bank data

## 10. Risk Assessment

### 10.1 Technical Risks
- **File Processing Failures**: Mitigated by error handling and retry logic
- **Data Corruption**: Mitigated by backup systems and validation
- **Performance Issues**: Mitigated by optimization and monitoring

### 10.2 User Experience Risks
- **Learning Curve**: Mitigated by intuitive interface design
- **Data Loss**: Mitigated by automatic saving and backup features
- **Complexity**: Mitigated by progressive disclosure of features

## 11. Conclusion

The Finance App represents a comprehensive solution for personal finance management, combining automated data processing with an intuitive user interface. The system successfully addresses the core need for automated transaction categorization while providing powerful analytics and reporting capabilities. The modular architecture allows for future enhancements and scalability while maintaining simplicity for end users.

The current implementation demonstrates strong technical foundations with room for growth in user experience enhancements and additional features. The focus on Excel-like editing and familiar workflows ensures user adoption while the automated processing capabilities provide significant time savings for financial management tasks.
