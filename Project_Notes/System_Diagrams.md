# System Architecture and Workflow Diagrams

These diagrams visualize the flow of data and the user experience for your Grassroots Tactical Assistant (GTA) prototype. You can include these flowcharts in your final paper to clearly illustrate your system design.

## 1. The AI & Computer Vision Pipeline
This diagram shows how raw video is processed into explainable tactical insights.

```mermaid
graph TD
    A[Raw MP4 Video from Mast] --> B(YOLOv8 Detection)
    B -->|Bounding Boxes| C(ByteTrack)
    C -->|Player IDs| D(K-Means Color Clustering)
    
    D -->|Team A, Team B, Referees| E{Tactical Engine}
    
    E -->|Calculate Polygon Area| F[Defensive Compactness Metric]
    E -->|Calculate Distance| G[Defensive Gap Metric]
    
    F --> H{Explainable AI Module}
    G --> H
    
    H -->|Draws Polygons/Lines| I[Visual Overlays]
    H -->|LLM Translation| J[Natural Language Summary]
    
    I --> K((Coach Web Dashboard))
    J --> K
```

## 2. The HCI / Coach Workflow
This diagram illustrates the human-centered process, from setting up the camera to receiving tactical feedback.

```mermaid
sequenceDiagram
    participant C as Amateur Coach
    participant M as 5m Camera Mast
    participant S as GTA Web System
    
    C->>M: Sets up mast at halfway line
    C->>M: Starts recording via Bluetooth
    Note over C,M: 90 Minute Match Played
    C->>M: Stops recording & downloads MP4
    C->>S: Uploads MP4 to Web Dashboard
    
    Note over S: AI Pipeline Processes Video
    
    S-->>C: Returns video with "Tactical Events" timeline
    
    C->>S: Clicks "Defensive Shape Broken" event
    S-->>C: Displays video frame with XAI Overlays (Polygons & Lines)
    S-->>C: Displays Text: "Gap between LB and CB exceeded 15m"
    
    C->>S: Clicks "Thumbs Up" (Helpful feedback)
```

## 3. The 180-Degree Workaround (Tactical Focus)
If you choose the "Tactical Focus" workaround discussed in the logistics math, here is how the camera capture zones work.

```mermaid
graph LR
    subgraph Football Pitch
        A[Attacking Third]
        B[Midfield Third]
        C[Defensive Third]
    end
    
    subgraph Ultrawide Camera on Mast
        Cam((Camera at Halfway Line))
    end
    
    Cam -.->|Static FOV Focus| B
    Cam -.->|Static FOV Focus| C
    
    style Cam fill:#f9f,stroke:#333,stroke-width:2px
    style C fill:#bbf,stroke:#f66,stroke-width:2px,stroke-dasharray: 5 5
```
