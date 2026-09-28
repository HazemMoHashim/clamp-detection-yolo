import cv2
import os

# Create a folder to save your frames
output_folder = "clamp_frames"
os.makedirs(output_folder, exist_ok=True)

# Load the video
video_path = "task.mp4"
cap = cv2.VideoCapture(video_path)

# Calculate total frames and the interval to get exactly 30 frames
total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
interval = total_frames // 30

frame_count = 0
saved_count = 0

while cap.isOpened() and saved_count < 30:
    ret, frame = cap.read()
    if not ret:
        break
    
    # Save a frame every time we hit the interval
    if frame_count % interval == 0:
        filename = os.path.join(output_folder, f"frame_{saved_count:02d}.jpg")
        cv2.imwrite(filename, frame)
        saved_count += 1
        
    frame_count += 1

cap.release()
print(f"Successfully saved {saved_count} frames to '{output_folder}'")