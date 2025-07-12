import cv2
import time
from utils import compute_offset, decide_command

# Load Haar Cascade model (face detection by default)
cascade_path = "models/haarcascade_frontalface_default.xml"
detector = cv2.CascadeClassifier(cascade_path)

# Open webcam
cap = cv2.VideoCapture(0)
time.sleep(2)  # Wait for the camera to warm up

frame_center_x = int(cap.get(3) / 2)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    objects = detector.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

    command = "SEARCHING"

    for (x, y, w, h) in objects:
        obj_center_x = x + w // 2
        offset = compute_offset(frame_center_x, obj_center_x)
        command = decide_command(offset)

        # Draw bounding box and center line
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.line(frame, (obj_center_x, 0), (obj_center_x, frame.shape[0]), (255, 0, 0), 2)
        break  # Track the first object only

    # Draw center line and display command
    cv2.line(frame, (frame_center_x, 0), (frame_center_x, frame.shape[0]), (0, 0, 255), 2)
    cv2.putText(frame, f"Command: {command}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

    cv2.imshow("AI Object Tracker", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
