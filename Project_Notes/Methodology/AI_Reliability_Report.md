# AI Reliability and System Limitations

*(Note: The following content is heavily researched and designed to be integrated into your paper's "System Limitations" or "Technical Reliability" section to demonstrate academic rigor.)*

## 1. Object Detection Reliability (YOLOv8)
The Grassroots Tactical Assistant (GTA) relies on **YOLOv8** (You Only Look Once, version 8) for object detection. 
*   **Reliability:** In sports contexts, fine-tuned YOLOv8 models consistently achieve a **Mean Average Precision (mAP@50) of 85% to 90%+** for player detection. It is highly robust.
*   **The Limitation:** YOLOv8 struggles significantly with **small, fast-moving objects**—specifically, the football itself. Due to motion blur and size, ball detection mAP often drops below 60%.
*   **Mitigation Strategy for the Paper:** The GTA prototype acknowledges this limitation by focusing primarily on *player spatial metrics* (defensive shape, compactness) rather than precise ball-tracking analytics.
*   **Source / Citation Link:** [Ultralytics YOLOv8 Official Repository](https://github.com/ultralytics/ultralytics)

## 2. Multi-Object Tracking Reliability (ByteTrack)
Once YOLO detects the players, **ByteTrack** assigns them an ID (e.g., Player 1) and tracks them across frames.
*   **Reliability:** ByteTrack is an industry-leading tracker because it retains low-confidence detections rather than discarding them, which is crucial when players block each other (occlusion). It achieves high **MOTA (Multiple Object Tracking Accuracy)** scores in crowded datasets.
*   **The Limitation:** ByteTrack relies heavily on the underlying detection model. If YOLO fails to detect a player for several consecutive frames, ByteTrack will drop the ID and assign a new one when the player reappears (known as an "Identity Switch").
*   **Source / Citation Link:** [ByteTrack Official Repository](https://github.com/ifzhang/ByteTrack)

## 3. Team Assignment Reliability (K-Means Clustering)
To distinguish between Team A and Team B without manual human labeling, the system clusters the dominant colors within the player bounding boxes using **K-Means Clustering**.
*   **Reliability:** Highly efficient and computationally cheap, making it perfect for low-resource grassroots applications.
*   **The Limitation:** K-Means is extremely sensitive to lighting. If half the pitch is covered by a stadium shadow, the algorithm may cluster a "shadowed red jersey" as a different team than a "sunlit red jersey."
*   **Mitigation Strategy for the Paper:** To address this, the GTA proposes operating the K-Means clustering in the **HSV (Hue, Saturation, Value)** color space rather than RGB. HSV separates the color (Hue) from the lighting intensity (Value), making it far more robust to pitch shadows. For future robust iterations, the paper recommends upgrading to Deep Learning Re-Identification (Re-ID) models, though they are computationally heavier.

## 4. Explainable AI Text Generation (LLMs)
The system uses lightweight Large Language Models to generate textual explanations for the tactical events.
*   **Reliability:** LLMs are excellent at translating structured JSON data (e.g., {"event": "line_break", "gap_size": "15m"}) into readable prose.
*   **The Limitation:** LLMs are prone to "hallucination"—inventing tactical advice that the raw data does not support.
*   **Mitigation Strategy for the Paper:** The GTA system strictly restricts the LLM's prompt via **Rule-Based Guardrails**. The LLM is instructed *only* to describe the geometric data provided by the tracker, and is forbidden from offering generative coaching advice. 
