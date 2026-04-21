# Master Methodology: System Design of the Grassroots Tactical Assistant (GTA)

## 1. Introduction and Architectural Overview
The methodology detailed herein establishes the theoretical and technical framework for the Grassroots Tactical Assistant (GTA). The primary engineering challenge lies in bridging the gap between professional-grade football analytics—which rely on multi-million dollar optical tracking arrays and wearable GPS micro-technology—and the severe resource constraints of amateur football. To achieve this, the GTA employs a modular, low-cost architecture consisting of a single-camera capture system, a robust computer vision pipeline utilizing YOLOv8 and ByteTrack, a relative spatial mathematics engine, and a Mobile-First Explainable AI (XAI) interface specifically optimized for the pedagogical limitations of grassroots coaches.

## 2. Hardware Logistics and Data Acquisition constraints
The foundation of any computer vision system is the quality of its input data. In professional environments, optical tracking is achieved via 16-camera rigs calibrated to the exact 3D dimensions of the stadium. Grassroots clubs are restricted to a single, uncalibrated consumer-grade camera (typically a smartphone or a commercial action camera). 

### 2.1 The Field of View (FOV) Limitation
A standard football pitch is 100 meters in length and 64 meters in width. Geometric modeling confirms that a standard smartphone lens (possessing a 75-degree horizontal FOV) positioned at the halfway line cannot capture the entire pitch. Even when utilizing an ultrawide lens (120-degree FOV), the camera only captures the central 70% of the pitch, missing the extreme corners. Consequently, the GTA is not designed to analyze full-pitch transitions; rather, it operates under a "Tactical Focus" paradigm, where the camera is explicitly pointed at a specific third of the pitch (e.g., the defensive third) to analyze localized structural shape.

### 2.2 Occlusion Mathematics and the 5-Meter Mast
The most significant barrier to single-camera tracking is player occlusion—where a player positioned near the camera obstructs the line of sight to a player positioned further away. 
Mathematical visualization of the pitch geometry dictates that ground-level recording is non-viable. If a camera is placed at a height of 1.5 meters on the sideline, a 1.8-meter tall player standing 2 meters away will entirely eclipse the remaining 62 meters of the pitch width.
To circumvent this, the GTA hardware specification requires a 5-meter elevated telescopic mast. Trigonometric calculation proves that from a height of 5 meters, the line of sight directed at the feet of a player on the far sideline (64 meters away) passes at an elevation of 4.85 meters when crossing the near sideline. This guarantees a clearance of over 3 meters above any near-side player, effectively eliminating lateral occlusion and ensuring uninterrupted tracking continuity for the AI models.

## 3. The Computer Vision Pipeline
The extraction of raw tactical data from the video feed is executed via a two-stage computer vision pipeline, strictly utilizing open-source, pre-trained neural networks to minimize computational overhead.

### 3.1 Object Detection via YOLOv8
The first stage employs YOLOv8 (You Only Look Once, version 8), a state-of-the-art, single-stage object detection model. YOLOv8 is highly optimized for real-time inference. In this architecture, the model is fine-tuned to identify the `person` class (Class 0) and the `sports ball` class (Class 32). 
The output of the YOLOv8 module is an array of bounding boxes for each frame, represented by Cartesian coordinates `(x1, y1, x2, y2)` alongside a confidence score.

### 3.2 Multi-Object Tracking via ByteTrack
A critical misconception in sports analytics is the necessity of identifying player jersey numbers to maintain tracking continuity. The GTA bypasses this via ByteTrack, a highly efficient multi-object tracking algorithm.
ByteTrack does not rely on optical character recognition (OCR). Instead, it links the YOLOv8 bounding boxes across consecutive frames utilizing a Kalman Filter. The Kalman Filter mathematically predicts the trajectory and velocity of each bounding box. By calculating the Intersection over Union (IoU) of the predicted box location against the actual box location in the subsequent frame, ByteTrack assigns a persistent Track ID (e.g., `Player_14`) to the object. This ensures continuous identification even if a player's back is turned to the camera.

### 3.3 Team Assignment via K-Means Clustering
Following detection and tracking, the system must classify players into opposing teams. The pipeline extracts a pixel crop of the upper half of each bounding box (isolating the jersey color from the shorts and socks). The pixel data is converted from RGB to the HSV (Hue, Saturation, Value) color space to mitigate the effects of pitch-side shadows and uneven lighting. An unsupervised K-Means clustering algorithm ($k=3$) is then applied to categorize the dominant hues into Team A, Team B, and Match Officials.

## 4. Coordinate Translation and The Tactical Mathematics Engine
In professional systems, 2D pixel coordinates are translated into 3D pitch coordinates via complex homography matrices and multi-camera calibration. This is impossible in grassroots environments due to moving tripod heads and uncalibrated lenses. 

### 4.1 Relative Spatial Metrics
To solve this, the GTA relies entirely on "Relative Spatial Metrics." The system does not attempt to calculate exact distances in real-world meters (e.g., "Player A ran 10.5 km"). Instead, it calculates geometric relationships within the 2D pixel space (e.g., "The pixel distance between Player A and Player B expanded by 40%").

### 4.2 Core Tactical Calculations
The Tactical Engine processes the resulting `(x, y)` coordinate arrays to identify structural breakdowns:
1.  **Defensive Compactness (Convex Hull):** The engine identifies the 10 outfield players of the defending unit. It applies a mathematical algorithm to calculate the Convex Hull—the smallest enclosing polygon that contains all 10 coordinate points. If the area of this polygon rapidly expands, the system flags a loss of defensive compactness.
2.  **Team Length and Width (Stretching):** The engine calculates the maximum displacement along the longitudinal axis (`max(x) - min(x)`) and the lateral axis (`max(y) - min(y)`). If the longitudinal displacement exceeds a defined pixel threshold, the system flags a "Vertically Stretched" event.
3.  **Inter-Line Distances:** The engine calculates the geometric centroid of the defensive unit and the centroid of the midfield unit. It continuously monitors the Euclidean distance between these two centroids to detect dangerous spatial gaps.

## 5. Human-Computer Interaction (HCI) and XAI UI/UX Design
The final and most critical component of the methodology is the presentation of this complex mathematical data to the end-user: the amateur coach.

### 5.1 Cognitive Load Reduction
Amateur coaches operate under extreme temporal and cognitive constraints. Professional analytics platforms (e.g., Sportscode) heavily feature complex data matrices and spreadsheets, which induce cognitive overload and software abandonment in grassroots users.
Therefore, the GTA interface is engineered strictly as a Mobile-First, visual dashboard. It avoids raw numerical data entirely, presenting tactical anomalies as chronological "Event Cards" in a simplified sidebar.

### 5.2 Multimodal Explainable AI (XAI)
To bridge the pedagogical gap between abstract data and player comprehension, the GTA utilizes Multimodal Explainable AI. When the Tactical Engine detects a 20-meter gap between the defensive and midfield lines, the UI does not just output text. It overlays glowing geometric shapes—such as the Convex Hull polygon or bright red distance lines—directly onto the video frame. 
Furthermore, recognizing the demographic constraints of the target users, the system incorporates a Large Language Model (LLM) to generate localized, natural-language summaries of the geometric breakdowns in Thai (e.g., "ช่องว่างในแนวรับกว้างเกินไป"). This multimodal approach removes subjective coach-player friction by presenting objective, visual, and easily readable proof of tactical errors.

## 6. System Validation Methodology
To isolate and validate the accuracy of the Tactical Mathematics Engine prior to the integration of the YOLOv8 camera pipeline, development leverages the Metrica Sports Open Data repository. This dataset provides pre-processed, anonymized `(x, y)` coordinate tracking data for all 22 players captured at 25 frames per second. By testing the Python geometric logic against this gold-standard open data, developers can ensure the accuracy of the Convex Hull and Euclidean distance algorithms independently of hardware capture variables.
