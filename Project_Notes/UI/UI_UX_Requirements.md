# UI/UX Requirements and Interface Design

*(Note: The following text is prepared for the "System Interface Design" section of your research paper. It details the human-centered constraints and features of the Grassroots Tactical Assistant (GTA).)*

## 1. Target User Persona and Constraints

The GTA is designed specifically for **Thai grassroots football coaches and university-level student coaches**. This demographic presents unique Human-Computer Interaction (HCI) challenges that dictate the design of the system:
*   **Hardware Environment:** Coaches operate on the pitch or in locker rooms. They do not use desktop computers during training. The system must be a **Tablet/Mobile-First Web Application**, optimized for touch interfaces in landscape mode.
*   **Cognitive Load:** Amateur coaches have limited time and rarely possess data-science backgrounds. The UI must avoid "data dumping" (e.g., massive spreadsheets of running metrics). The design philosophy is strictly: *Visuals first, text second, numbers last.*
*   **Bilingual Localization:** While coaches are familiar with universal English football terminology (e.g., "Pressing," "Compactness"), complex AI explanations in English increase cognitive load. The UI relies on a bilingual approach: standard tactical headers remain in English, but the Explainable AI (XAI) summaries are generated in **Thai language** to ensure immediate comprehension and trust.

## 2. Core UI Architecture: The Three-Panel Dashboard

To minimize navigation depth, the core analytical experience is restricted to a single, highly interactive dashboard.

### A. The Video Player (Center Stage)
*   The uploaded match video occupies the majority of the screen real estate.
*   **Smart Timeline:** The traditional video scrubber is augmented with colored "Event Markers" (e.g., Red for Defensive Breakdowns, Green for Attacking Transitions) so the coach can jump directly to AI-flagged moments without watching the full 90 minutes.

### B. The Tactical Event Feed (Right Sidebar)
*   A scrollable chronological list of tactical events detected by the AI.
*   Each event card features a clear icon, a timestamp, and a brief Thai summary (e.g., *⏱️ 14:23 - ช่องว่างในแนวรับกว้างเกินไป*).
*   **Feedback Mechanism:** Each card includes a "Thumbs Up / Thumbs Down" button. This is a critical HCI feature that allows coaches to rate the AI's accuracy, fostering a sense of control and providing data for future system refinement.

### C. The XAI Toggle Panel (Bottom / Overlay)
*   When a coach clicks an event in the feed, the video pauses, and the XAI Panel appears.
*   This panel contains simple touch-friendly toggle switches allowing the coach to visually deconstruct the AI's logic directly on the video feed:
    *   [Toggle] **แสดงรูปทรงทีม (Show Team Shape):** Overlays a semi-transparent polygon over the defensive unit.
    *   [Toggle] **แสดงระยะห่าง (Show Distance Lines):** Draws bright connecting lines between defenders with estimated meter gaps.
    *   [Toggle] **แสดง ID ผู้เล่น (Show Player IDs):** Highlights the specific players involved in the error.

## 3. Explainability (XAI) as a UI Priority

In elite analytics, black-box systems are often tolerated if they produce winning results. In grassroots sports, if a coach does not understand *why* the AI flagged a play, they will reject the software. 

The GTA interface achieves explainability by instantly mapping the AI's mathematical output (e.g., an expanded convex hull) to a visual overlay on the exact frame of the video. Below the video, a natural-language LLM generates a concise, one-sentence summary in Thai, translating the geometric anomaly into actionable coaching advice. This multimodal approach (Visual + Textual) ensures that trust is built through transparent, understandable feedback.
