# Grassroots User Needs Assessment and System Justification

*(Note: The following text is designed to be integrated into the "Problem Statement" or "System Justification" section of your research paper. It academically validates why the system was built the way it was.)*

## Identifying the HCI Gap in Grassroots Football

While elite football clubs employ dedicated teams of data scientists and utilize multi-camera arrays or wearable GPS trackers, grassroots and amateur environments operate under severe resource constraints. A review of coaching challenges reveals four distinct pain points that prevent the adoption of modern video analysis at the amateur level:

1. **Temporal Constraints (The "Time" Problem):** Amateur coaches typically balance full-time employment with their coaching duties. Manually scrubbing through 90 minutes of raw video to locate and "tag" specific tactical breakdowns is often impossible.
2. **Financial and Hardware Constraints:** Grassroots teams cannot afford wearable player-tracking technology (- per player) or professional software licenses. They are restricted to a single, uncalibrated video camera (often a smartphone on a tripod).
3. **Technological Complexity (The "Spreadsheet" Problem):** Existing professional analytics software (e.g., Sportscode, Hudl) is designed for data analysts, heavily featuring complex spreadsheets and data matrices. Amateur coaches report high cognitive overload when presented with raw data tables, leading to software abandonment.
4. **Pedagogical Friction (The "Communication" Problem):** Grassroots players often struggle to comprehend abstract verbal feedback (e.g., "Our defensive line was too high and disconnected"). Coaches need immediate, visual evidence to bridge the gap between tactical theory and player understanding.

## System Solution Mapping: The Grassroots Tactical Assistant (GTA)

To ensure high usability and adoption, the architecture and UI/UX of the Grassroots Tactical Assistant were explicitly designed to resolve these four pain points.

| Identified User Pain Point            | GTA System Solution (Feature Justification)                                                                                                                                                                                                                                                                                                                                                       |
| :------------------------------------ | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **1. Temporal Constraints**     | **Automated Event Tagging (Smart Timeline):** The YOLOv8 and ByteTrack pipeline autonomously identifies when defensive structures fail, placing colored markers on the video timeline. This eliminates manual scrubbing, allowing coaches to review key moments instantly.                                                                                                                  |
| **2. Hardware Constraints**     | **Single-Camera 2D Metric Extraction:** By relying entirely on relative spatial metrics (e.g., convex hull area) rather than exact 3D pitch calibration, the system operates effectively on standard 2D video captured from a simple 5-meter halfway-line mast.                                                                                                                             |
| **3. Technological Complexity** | **Visual-First Dashboard Design:** The UI strictly avoids data tables. Instead, tactical events are presented chronologically in a simple sidebar, maintaining a low cognitive load suitable for a tablet interface on the pitch.                                                                                                                                                           |
| **4. Pedagogical Friction**     | **Explainable AI (XAI) Visual Overlays:** Rather than providing a raw statistic (e.g., "Compactness = 450 sq meters"), the XAI module draws glowing polygons and distance lines directly over the video frames. Combined with Thai-localized LLM summaries, this allows players to *see* the shape breakdown exactly as the coach sees it, dramatically improving feedback comprehension. |

**Conclusion:** By explicitly aligning the AI's capabilities with the lived reality of amateur coaches, the GTA avoids the common pitfall of being "over-engineered and under-utilized," presenting a highly feasible solution for grassroots digitalization.
