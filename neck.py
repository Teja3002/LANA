import time

import cv2
import mediapipe as mp
import numpy as np
from plyer import notification

mp_pose = mp.solutions.pose
mp_drawing = mp.solutions.drawing_utils

cap = cv2.VideoCapture(0)
start_time = None
notification_sent = False
with mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5) as pose:
    while cap.isOpened():
        success, image = cap.read()

        image = cv2.cvtColor(cv2.flip(image, 1), cv2.COLOR_BGR2RGB)

        results = pose.process(image)

        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

        if results.pose_landmarks:
            neck_x = results.pose_landmarks.landmark[mp_pose.PoseLandmark.NOSE].x
            neck_y = results.pose_landmarks.landmark[mp_pose.PoseLandmark.NOSE].y

            neck_angle = np.degrees(np.arctan2(neck_y - 0.5, neck_x - 0.5))

            cv2.putText(image, f"Neck Angle: {int(neck_angle)}", (20, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

            if neck_angle > 20:

                cv2.putText(image, "Adjust neck posture!", (20, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

                if start_time is None:
                    start_time = time.time()
                else:
                    elapsed_time = time.time() - start_time
                    if elapsed_time >= 10 and not notification_sent:
                        notification.notify(
                            title='Posture alert',
                            message='Correct your neck posture',
                            timeout=10
                        )
                        print("Notification sent")
                        notification_sent = True
            else:
                start_time = None
                notification_sent = False
        cv2.imshow('Neck Viewing Angle Monitoring', image)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()
