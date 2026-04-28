# System Design and Methodology

*(Note: The following text is drafted in academic tone, ready to be copied directly into the "Methodology" and "System Concept" sections of your main draft document.)*

## Proposed System Architecture: The Grassroots Tactical Assistant (GTA)

To address the constraints of amateur football, we propose the Grassroots Tactical Assistant (GTA), a web-based prototype designed to extract tactically meaningful insights from ordinary, non-calibrated video footage. Rather than requiring multi-camera setups or wearable GPS trackers, the GTA relies entirely on accessible 2D video inputs, mimicking the realities of grassroots coaching environments.

### Computer Vision Pipeline
The underlying artificial intelligence framework avoids the necessity of training deep learning models from scratch, leveraging robust, pre-trained computer vision architectures. The pipeline consists of three primary stages:
1. **Detection and Tracking:** Player and ball detection are achieved using YOLOv8 (You Only Look Once), an open-source object detection model known for its high inference speed and accuracy in sports contexts. Player tracking across frames is maintained using ByteTrack, a multi-object tracking algorithm that reliably links bounding boxes even during occlusions.
2. **Team Assignment:** To differentiate between opposing teams and referees without requiring manual labeling, a K-Means clustering algorithm is applied to the dominant color histograms extracted from the tracked bounding boxes.
3. **Tactical Metric Extraction:** Recognizing the difficulty of homography mapping (2D pixel to 3D pitch mapping) on uncalibrated panning cameras, the system focuses on relative spatial metrics. For example, defensive compactness is calculated dynamically by generating a convex hull (polygon) connecting the outermost players of a designated defensive unit, tracking sudden expansions in area as indicators of structural failure.

## Designing Explainability (XAI) for Coaches

Explainability in the GTA is treated not as a supplementary feature, but as a core design requirement. The system translates raw computational outputs into visual and contextual explanations tailored for end-users who lack data science expertise. 

The XAI interface employs a dual-modality approach:
1. **Visual Overlays:** When the system flags a tactical event (e.g., a broken defensive line), it projects visual annotations directly onto the video feed. This includes drawing the defensive polygon to illustrate team shape and overlaying dynamic distance lines (in relative pixels or estimated meters) to highlight critical gaps between defenders.
2. **Contextual Natural Language Summaries:** To prevent cognitive overload from raw numerical data, the interface integrates lightweight Large Language Models (LLMs) to generate textual summaries of the visual data. Instead of displaying abstract metrics, the system outputs interpretable insights, such as: *"The defensive shape was compromised due to a sudden 15-meter gap forming between the Left Back and Center Back."*

## Proposed Methodology and HCI Evaluation

The development and evaluation of the GTA will follow a human-centered design (HCD) methodology, occurring in two distinct phases.

### Phase 1: Prototype Development
Initial model tuning and prototype development will utilize the SoccerNet dataset. As a large-scale, open-source repository containing pre-labeled tracking data and action spotting, SoccerNet provides a robust baseline for validating the YOLOv8 and tracking pipeline without the immediate need for local data collection.

### Phase 2: User Evaluation in the Wild
The core contribution of this research lies in evaluating the system's explainability and usability with its target demographic. We will conduct a user evaluation study involving 5 to 10 grassroots and amateur coaches. 
To ensure ecological validity, the prototype will be tested using video footage captured from the coaches' own local amateur matches (recorded via standard tripods or smartphones). The evaluation will employ the "Think-Aloud" protocol, where coaches interact with the web dashboard while verbalizing their thought processes. The primary variables of interest include:
- **Comprehension:** Do the visual overlays accurately convey *why* the AI flagged a specific event?
- **Trust:** Does the presence of natural language summaries and confidence scores increase the coach's trust in the system's tactical assessments compared to traditional black-box analytics?
- **Actionability:** Can the coach immediately translate the AI's insight into a practical training intervention?
