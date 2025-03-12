import cv2
from pyzbar.pyzbar import decode
import numpy as np

import cv2 
from pyzbar.pyzbar import decode
import numpy as np

kamera = cv2.VideoCapture(0)

while True:
    ret, videoGoruntu = kamera.read()
    
    if not ret:
        break

    qr_codes = decode(videoGoruntu)
    for qr in qr_codes:
        qr_text = qr.data.decode("utf-8")
        print("QR İçeriği:", qr_text)

        
        koseler = qr.polygon
        if len(koseler) == 4:
            pts = np.array([(p.x, p.y) for p in koseler], np.int32)
            pts = pts.reshape((-1, 1, 2))
            cv2.polylines(videoGoruntu, [pts], True, (0, 255, 0), 2)

    cv2.imshow("Bilgisayar Kamerası", videoGoruntu)

    if cv2.waitKey(1) & 0xFF == ord('x'):
        break

kamera.release()
cv2.destroyAllWindows()

#qr okuma için