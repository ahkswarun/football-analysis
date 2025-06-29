# 🎯 Player Re-Identification and Tracking - 15 Second Video

This project implements player detection, tracking, and re-identification on a short sports video. The goal is to:

Detect players, referees, and the ball using a YOLO-based object detection model  
Assign unique IDs to each player based on their initial appearance  
Maintain consistent IDs even when players leave and re-enter the frame  
Visually annotate the video with clear player, referee, and ball indicators  


Required Libraries:

ultralytics

supervision

numpy

pandas

opencv-python

torch

Tracker Functionality
The Tracker class in trackers.py handles:

Player, Referee, Ball Detection: Using YOLO model

Tracking: Leveraging ByteTrack for consistent ID assignment

Re-identification: Maintains same IDs for players who temporarily leave the frame

Annotation: Players visualized with ellipses, referees with distinct color, and ball with triangles

Intermediate detection results can be cached to stubs/track_stubs.pkl for faster re-runs.

Running the Code
Make sure:

✅ Your input video is placed in the input/ directory as input.mp4
✅ Your trained YOLO model (best.pt) is placed in the models/ directory


Notes
GPU recommended for faster inference if available

The system is designed for short sports clips but can be extended for longer videos

Re-identification performance depends on player appearance consistency

