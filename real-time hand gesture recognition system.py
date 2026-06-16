import cv2
import os

gesture_id = 6
num_images = 300  
save_path = f'dataset/{gesture_id}'

os.makedirs(save_path, exist_ok=True)


cap = cv2.VideoCapture(0)
print(f"Collecting images for gesture ID: {gesture_id}")

count = 0
while True:
    ret, frame = cap.read()
    if not ret:
        break

    
    x1, y1, x2, y2 = 100, 100, 300, 300
    roi = frame[y1:y2, x1:x2]
    roi = cv2.resize(roi, (200, 200))

    cv2.rectangle(frame, (x1, y1), (x2, y2), (255, 0, 0), 2)
    cv2.putText(frame, f"Capturing {count}/{num_images}", (50, 50),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    cv2.imshow("Capture Gesture", frame)

    key = cv2.waitKey(1)
    if key == ord('c'): 
        cv2.imwrite(f"{save_path}/{count}.jpg", roi)
        count += 1

    elif key == ord('q') or count >= num_images:
        break

cap.release()
cv2.destroyAllWindows()
print("Dataset collection complete.")
