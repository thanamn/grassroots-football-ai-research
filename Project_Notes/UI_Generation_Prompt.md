# UI Generator Prompt for the GTA System

*Copy and paste the exact text below into any UI designing AI (like v0 by Vercel, Midjourney, or Google's UI generation tools) to get a perfect, highly detailed mockup of your system.*

***

**System Role & Goal:**
Design a highly realistic, modern, and premium User Interface (UI) for a sports analytics web application called the "Grassroots Tactical Assistant" (GTA). The app is designed for amateur football (soccer) coaches.

**Device & Orientation:**
The UI must be formatted for an iPad/Tablet screen viewed in Landscape mode. The design must feel "Mobile-First" and touch-friendly, avoiding tiny text or complex spreadsheet data dumps.

**Color Palette & Aesthetic:**
Use a sleek, professional "Dark Mode" aesthetic (deep charcoals, blacks, and subtle glowing accents). The interface should look high-tech but extremely clean, minimizing cognitive load.

**Layout Architecture (The Three-Panel Dashboard):**

1. **The Main Video Player (Center/Left - 70% of screen):**
   - Display a large, high-definition video player showing a football match captured from an elevated halfway-line angle (like a Veo camera).
   - **XAI Overlay (Crucial):** On top of the video feed, draw an "Explainable AI" overlay. Show a glowing, semi-transparent geometric polygon (convex hull) connecting 4 defending players to visualize the "Team Shape". Draw a bright dashed line between two of the defenders showing a "15m Gap". 
   - **Smart Timeline:** At the bottom of the video, the scrubber bar should have colored dots/markers indicating key tactical events.

2. **The Tactical Event Feed (Right Sidebar - 30% of screen):**
   - A sleek, scrollable sidebar titled "Tactical Events".
   - It contains 3 or 4 vertical "Event Cards". 
   - Each card should have: A timestamp (e.g., 14:23), a warning icon, and text describing the event. *Include Thai language text on the cards to show localization* (e.g., "14:23 - ช่องว่างในแนวรับกว้างเกินไป" which means Defensive gap too wide).
   - Each card MUST have small "Thumbs Up" and "Thumbs Down" feedback icons for the coach to rate the AI's accuracy.

3. **The XAI Toggle Panel (Bottom bar below the video):**
   - A clean horizontal control bar with touch-friendly toggle switches (iOS style toggles).
   - The toggles should be labeled: "Show Team Shape", "Show Distance Lines", and "Show Player IDs". The "Show Team Shape" toggle should be in the 'ON' position, glowing to match the polygon on the video.

**Vibe & Output Requirements:**
The final output should look like a fully coded, interactive React/Tailwind web application ready to be deployed on a tablet on the side of a football pitch. Prioritize visual clarity, large touch targets, and an emphasis on the geometric AI overlays on the video.
