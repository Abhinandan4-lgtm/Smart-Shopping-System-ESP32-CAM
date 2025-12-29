# Smart-Shopping-System-ESP32-CAM

This project implements a smart shopping system where products are identified using external QR codes.  
An ESP32-CAM captures images of QR codes, Python decodes them, and a Flask-based website updates the shopping cart in real time.

---

## 🔧 System Architecture

External QR Code  
↓  
ESP32-CAM (Camera only)  
↓  
Python QR Scanner (OpenCV + PyZbar)  
↓  
Flask Web Server  
↓  
Website Table (Price, Quantity, Total)

---

## 🚀 Features

- External QR codes (printed or displayed)
- ESP32-CAM used only as camera
- QR decoding done in Python
- Real-time quantity update
- Automatic total calculation
- Clean web interface (no QR shown)

---

## 🧰 Technologies Used

- ESP32-CAM (AI Thinker)
- Arduino IDE
- Python
- Flask
- OpenCV
- PyZbar
- HTML/CSS

---

---

## ▶️ How to Run

## 1. Install Python libraries

pip install -r requirements.txt
## 2. Generate QR Codes
python qr_generation/generate_qr_codes.py

## 3. Upload ESP32-CAM Code

Open esp32_cam_server.ino

Board: AI Thinker ESP32-CAM

Upload via FTDI / Arduino UNO (USB-Serial)

## 4. Run Website
python web_app/app.py

## 5. Run Scanner
python web_app/scanner.py

### 📸 ESP32-CAM Stream URL
http://<ESP32_IP>/cam-hi.jpg
