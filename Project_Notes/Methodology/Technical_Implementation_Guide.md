# Technical Implementation Guide: Grassroots Tactical Assistant

*(Note: This document provides the programmatic blueprint for the AI pipeline, addressing feasibility constraints and providing reference Python code for your paper's technical chapters.)*

## 1. Feasibility Analysis: How Tracking Actually Works

A common misconception is that AI needs to "read" jersey numbers to track players. This is false.
*   **The "No Numbers" Solution:** YOLOv8 detects the physical *shape* and texture of a human body, assigning a bounding box regardless of the jersey direction. The tracking algorithm (ByteTrack) maintains identity frame-to-frame by using a **Kalman Filter**. It predicts where the bounding box will be in the next millisecond based on current velocity and trajectory (using a metric called Intersection over Union, or IoU). Therefore, the AI can track a player perfectly even if their back (and number) is turned away from the camera.
*   **The "Action Tracking" Solution:** YOLOv8 does *not* detect actions (like a "tackle"). It only outputs `(x, y)` pixel coordinates. To detect actions in a lightweight grassroots system, we must use **Rule-Based Geometric Logic** rather than heavy 3D-CNN Action Recognition models. (e.g., If the ball's coordinates rapidly accelerate away from Player A's coordinates, the system logs a "Pass").

## 2. Input / Output Specifications

| Module | Input Required | Output Generated |
| :--- | :--- | :--- |
| **YOLOv8** | Raw MP4 Video Frame | Bounding Boxes `(x1, y1, x2, y2)`, Class (`0` for player, `32` for ball), Confidence (`0.85`) |
| **ByteTrack** | YOLO Bounding Boxes | Track ID `(e.g., Player_14)` attached to each bounding box |
| **K-Means** | Bounding Box Pixel Crop | Team Assignment `(Team_A, Team_B, Referee)` |
| **Tactical Engine** | `(x,y)` coordinates of all players | JSON Tactical Event `{"event": "line_break", "time": "14:23"}` |

## 3. Python Implementation (Core Inference Pipeline)

This is the actual Python logic required to run the detection and tracking pipeline using the Ultralytics library.

```python
import cv2
from ultralytics import YOLO

# 1. Load the YOLOv8 model (fine-tuned on a football dataset)
model = YOLO('yolov8m-football.pt')

# 2. Open the grassroots video file
video_path = "grassroots_match_half1.mp4"
cap = cv2.VideoCapture(video_path)

while cap.isOpened():
    success, frame = cap.read()
    if not success:
        break

    # 3. Run Inference AND Tracking (ByteTrack is built into Ultralytics)
    # The 'persist=True' argument tells the AI to remember IDs between frames
    results = model.track(frame, tracker="bytetrack.yaml", persist=True)

    # 4. Extract data for the Tactical Engine
    for result in results:
        boxes = result.boxes
        for box in boxes:
            # Get geometric coordinates
            x1, y1, x2, y2 = box.xyxy[0]
            # Get the Track ID (Who is this player?)
            track_id = int(box.id[0]) if box.id is not None else None
            # Get class (Is it a player or the ball?)
            cls = int(box.cls[0]) 

            # Send this data to K-Means and the Rule-Based Tactical Engine
```

## 4. Python Implementation (Rule-Based Action Tracking)

Here is a simplified example of how the software translates raw `(x,y)` coordinates into a "Pass Detection" action using distance calculations, bypassing the need for a heavy Action Recognition AI.

```python
import math

def detect_pass(ball_coords, player_coords, current_ball_speed):
    # ball_coords = (x, y), player_coords = (x, y)
    
    # 1. Calculate the Euclidean distance between the ball and the player
    distance = math.sqrt((ball_coords[0] - player_coords[0])**2 + 
                         (ball_coords[1] - player_coords[1])**2)
    
    # 2. Rule-Based Logic: If the ball is very close to the player AND suddenly speeds up
    distance_threshold = 50 # pixels
    speed_threshold = 20 # pixels per frame
    
    if distance < distance_threshold and current_ball_speed > speed_threshold:
        return True # Pass Action Detected!
    
    return False
```
