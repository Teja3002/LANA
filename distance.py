import cv2
import cvzone
from cvzone.FaceMeshModule import FaceMeshDetector
import time
from plyer import notification

cap = cv2.VideoCapture(0)
detector = FaceMeshDetector(maxFaces=5)

start_time = None
notification_sent = False

while True:
    success, img = cap.read()
    img, faces = detector.findFaceMesh(img, draw=False)

    if faces:
        face = faces[0]
        pointLeft = face[145]
        pointRight = face[374]

        w, _ = detector.findDistance(pointLeft, pointRight)
        W = 6.3

        f = 840
        d = (W * f) / w

        print(d)

        if d < 60:
            if start_time is None:
                start_time = time.time()
            else:
                elapsed_time = time.time() - start_time
                if elapsed_time >= 10 and not notification_sent:
                    notification.notify(
                        title='Distance Alert',
                        message='Distance less than 60 for 10 seconds.',
                        timeout=10
                    )
                    print("Notification sent")
                    notification_sent = True
        else:
            start_time = None
            notification_sent = False

    cv2.imshow("Image", img)
    cv2.waitKey(1)
