# Tactical Metrics and Development Datasets

*(Note: This document provides the blueprint for the "System Development Methodology" section of your research paper, outlining exactly what the AI will calculate and how developers can build it.)*

## 1. The Development Dataset: Metrica Sports Open Data

To build the Tactical Engine, developers do not need to wait for the YOLOv8 camera pipeline to be completed. They can build and test the mathematical logic using the industry "gold standard" open-source tracking dataset.

**Metrica Sports Sample Data**
*   **GitHub Repository:** `https://github.com/metrica-sports/sample-data`
*   **Description:** Metrica Sports has publicly released anonymized tracking data for multiple 90-minute matches. The data is provided in CSV format and contains the exact `(x, y)` coordinate data for all 22 players and the ball at 25 frames per second.
*   **Development Usage:** By feeding this CSV data into the Python Tactical Engine, developers can write the geometric logic for "Defensive Compactness" and verify its accuracy immediately without needing computer vision processing.

## 2. Core Tactical Metrics for the Grassroots Prototype

The Grassroots Tactical Assistant (GTA) avoids complex, opaque metrics (like "Expected Threat"). Instead, it focuses on fundamental spatial geometry that amateur coaches can easily understand and visualize. 

The system relies on three core calculations:

### A. Defensive Compactness (Team Shape Area)
*   **Tactical Purpose:** Measures how tightly grouped the defending team is. A highly compact team restricts space for the opponent to pass through.
*   **Mathematical Calculation:** The system identifies the 10 outfield players of the defending team. It calculates the **Convex Hull**—the smallest polygon that encapsulates all 10 players based on their `(x, y)` coordinates. The area of this polygon (in square meters) dictates compactness.
*   **AI Event Trigger:** If the Convex Hull area rapidly expands by a specified percentage (e.g., >30% in 3 seconds), the AI flags an "Uncompact Defense" event.

### B. Vertical Team Stretching (Team Length)
*   **Tactical Purpose:** Measures the vertical distance between the deepest defender (usually the center-back) and the highest attacker (the striker).
*   **Mathematical Calculation:** Using the `x` coordinates (assuming the pitch length runs along the x-axis), the system calculates: `Length = max(player_x) - min(player_x)`. 
*   **AI Event Trigger:** If `Length > 45 meters` while the opponent has possession, the AI flags a "Team Vertically Stretched" event, indicating the team is vulnerable to passes between the lines.

### C. Inter-Line Gaps
*   **Tactical Purpose:** Measures the physical separation between specific positional units (e.g., the defensive line and the midfield line).
*   **Mathematical Calculation:** The system calculates the centroid (average `x` and `y` coordinates) of the 4 defenders and the centroid of the 4 midfielders. It then calculates the Euclidean distance between these two centroids.
*   **AI Event Trigger:** If the distance between the defensive line and midfield line exceeds a set threshold (e.g., >15 meters), the AI flags a "Line Disconnected" event and draws a red XAI distance line between the two units on the video.
