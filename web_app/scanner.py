import cv2
import numpy as np
import pyzbar.pyzbar as pyzbar
import requests

ESP32_URL = "http://192.168.1.61/cam-hi.jpg"
SERVER_URL = "http://127.0.0.1:5000/update"

last = ""

while True:
    img = requests.get(ESP32_URL).content
    frame = cv2.imdecode(np.frombuffer(img, np.uint8), 1)

    for code in pyzbar.decode(frame):
        data = code.data.decode()
        if data != last:
            last = data
            slno, _, _ = data.split(",")
            requests.post(SERVER_URL, json={"slno": int(slno)})

    cv2.imshow("ESP32 QR Scanner", frame)
    if cv2.waitKey(1) == 27:
        break

cv2.destroyAllWindows()
