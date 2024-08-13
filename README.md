# YOLOv8n-Pose Keypoint Detection

This project uses the YOLOv8n-Pose model to process a video and detect keypoints (pose estimation) of individuals. The processed video is saved with bounding boxes and keypoints overlaid on the detected persons.

## Project Structure

- **yolov8n-pose.pt**: The pre-trained YOLOv8n-Pose model used for pose detection.
- **dancing.mp4**: The input video file where keypoints are detected.
- **processed_video.mp4**: The output video file with detected keypoints and bounding boxes.

## Requirements

- Python 3.6+
- Ultralytics YOLOv8
- OpenCV
- shutil

Install the necessary dependencies using:

```bash
pip install ultralytics opencv-python

