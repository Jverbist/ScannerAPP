# Logistics Sorting Application

A web application that enables warehouse teams to sort items by their purchase order (POBE) dynamically. This application supports real-time item sorting and provides counts for each sorted POBE, making it easy to manage large inventories.

## Features
- Upload Excel files with packing slip data.
- Input item serial numbers manually or via a scanner.
- Automatically sort items by POBE in real-time.
- Display counts for each POBE and unmatched items.
- Easy deployment using Docker.

  **DEMO** 
  ![Alt Text](/static/ScreenRecording2024-12-19at11.41.05-ezgif.com-video-to-gif-converter.gif)
---

## Application Flow

1. **Upload Packing Slip**:
   - Navigate to the **Home page**.
   - Upload an Excel file containing packing slip data. The file must have the following columns:
     - `PO Number`
     - `Item`
     - `Serial Number`

2. **Input Serial Numbers**:
   - Navigate to the **Input Items page**.
   - Enter item serial numbers manually or via a barcode scanner. Each number should be entered on a new line.

3. **View Sorted Results**:
   - The application dynamically sorts the items into tables grouped by POBE.
   - Each table includes a count of the items for the respective POBE.
   - Unmatched items are displayed in a separate list.

4. **Repeat Process**:
   - New serial numbers can be added at any time to update the sorted results dynamically.

---

## Prerequisites

### Local Development
- Python 3.7 or higher
- Flask (`pip install flask`)
- Pandas (`pip install pandas`)
- OpenPyXL (`pip install openpyxl`)

### Deployment
- Docker
- Ubuntu Server (or any Linux-based environment)

---

## Installation (Local Development)

1. Clone the repository:
  ```bash
   git clone https://github.com/Jverbist/ScannerAPP.git
   cd ScannerAPP
   ```
2. Change this piece of code in app.py at the bottom to this:
  ```python
  if __name__ == '__main__':
    app.run(debug=True)
  ```
3. Install dependencies:
  ```bash
   pip install -r requirements
   ```
4. Run the application locally:
  ```bash
   python app.py
  ```
5. Access the application `http://127.0.0.1:5000` 




