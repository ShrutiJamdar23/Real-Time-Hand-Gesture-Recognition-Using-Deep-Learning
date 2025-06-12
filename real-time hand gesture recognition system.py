import cv2
import os

# Parameters
gesture_id = 6# Change this for each gesture
num_images = 300  # How many images to capture
save_path = f'dataset/{gesture_id}'

# Create folder if it doesn't exist
os.makedirs(save_path, exist_ok=True)

# Start webcam
cap = cv2.VideoCapture(0)
print(f"Collecting images for gesture ID: {gesture_id}")

count = 0
while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Define Region of Interest (ROI) box
    x1, y1, x2, y2 = 100, 100, 300, 300
    roi = frame[y1:y2, x1:x2]
    roi = cv2.resize(roi, (200, 200))

    # Show feedback
    cv2.rectangle(frame, (x1, y1), (x2, y2), (255, 0, 0), 2)
    cv2.putText(frame, f"Capturing {count}/{num_images}", (50, 50),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    cv2.imshow("Capture Gesture", frame)

    # Save image every few frames
    key = cv2.waitKey(1)
    if key == ord('c'):  # Press 'c' to capture an image
        cv2.imwrite(f"{save_path}/{count}.jpg", roi)
        count += 1

    elif key == ord('q') or count >= num_images:
        break

cap.release()
cv2.destroyAllWindows()
print("Dataset collection complete.")
