import cv2
import os

def extract_frames(video_path, output_folder, frame_rate=1):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        print("Error: Could not open video.")
        return

    frame_count, saved_count = 0, 0

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        if frame_count % frame_rate == 0:
            frame_filename = os.path.join(output_folder, f"frame_{saved_count}.jpg")
            cv2.imwrite(frame_filename, frame)
            print(f"Saved {frame_filename}")
            saved_count += 1

        frame_count += 1

    cap.release()
    print(f"Extracted {saved_count} frames successfully!")

# Run the function
if __name__ == "__main__":
    extract_frames("sample_video.mp4", "extracted_frames", 1)
