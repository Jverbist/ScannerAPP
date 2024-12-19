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



## Installation (Using Docker)

1. On your server create a directory and navigate in the directory:
  ```bash
  mkdir logisticsAPP
  cd logisticsAPP
  ```
2. Create and Save Dockerfile:
  ```bash
  nano Dockerfile
  ---------------------------------------------------------------
  # Use an official Python runtime as a base image
  FROM python:3.9-slim

  # Set the working directory in the container
  WORKDIR /app

  # Install system dependencies
  RUN apt-get update && apt-get install -y --no-install-recommends \
      git && \
      apt-get clean && \
      rm -rf /var/lib/apt/lists/*

  # Clone the repository from GitHub
  RUN git clone https://github.com/Jverbist/ScannerAPP.git /app

  # Install application dependencies
  RUN pip install --no-cache-dir -r requirements.txt

  # Expose the application port
  EXPOSE 5000

  # Run the application
  CMD ["python", "app.py"]

  ```
3. Build Docker image:
  ```bash
 docker build --no-cache -t logistics-app .  
  ```
4. Create and Save **docker-compose.yml**:
  ```bash
  nano docker-compose.yml
  ----------------------------------------------------------------
  version: "3.8"
  services:
    flask-app:
      image: logistics-app
      build:
        context: .
      ports:
        - "80:5000"
  ```
5. Run docker-compose to deploy container:
  ```bash
    docker-compose up -d
  
  ```
6. Access the application in your browser at `http://<server-ip>`

## Troubleshooting
#### Issue: "TCP Reset from Server"
- Endure the Flask app is binding to `0.0.0.0` in `app.py`:
  ```python
  app.run(host='0.0.0.0', port=5000)
  ```
- Check Docker port mapping:
  ```bash
  docker ps
  ```
- Open port 80 in the firewall:
  ```bash
  sudo ufw allow 80/tcp
  ```
#### Log
To view container logs:
```bash
docker logs <container-id>
```


## License

