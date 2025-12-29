import qrcode
import os

QR_FOLDER = "../web_app/static/qrcodes"
os.makedirs(QR_FOLDER, exist_ok=True)

items = [
    (1, "Apple", 10),
    (2, "Banana", 5),
    (3, "Orange", 8),
    (4, "Mango", 15),
    (5, "Grapes", 12),
]

for slno, name, price in items:
    data = f"{slno},{name},{price}"
    qr = qrcode.make(data)
    qr.save(f"{QR_FOLDER}/{name}.jpg")

print("QR codes generated successfully")
