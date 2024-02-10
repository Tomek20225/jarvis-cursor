import cv2
import os
import argparse

def extract_frames(avi_file_path, output_dir):
    file_name = os.path.splitext(os.path.basename(avi_file_path))[0]

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    cap = cv2.VideoCapture(avi_file_path)
    if not cap.isOpened():
        print("Error: Could not open video")
        return
    
    frame_count = 0
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        frame_path = os.path.join(output_dir, f"{file_name}_{frame_count:04d}.jpg")
        cv2.imwrite(frame_path, frame)
        frame_count += 1

    cap.release()
    print(f"Done! Extracted {frame_count} frames")

def main():
    parser = argparse.ArgumentParser(description="Extract frames from an AVI file and save as JPG images.")
    parser.add_argument("avi", help="Path to the AVI file")
    parser.add_argument("out", help="Directory where frames will be saved", default="./frames", nargs='?')
    args = parser.parse_args()
    extract_frames(args.avi, args.out)

if __name__ == "__main__":
    main()