# Data Acquisition Constraints in Grassroots Environments

*(Note: This text is formatted for inclusion in your paper under the Methodology or System Limitations section to justify your hardware choices.)*

## Physical Constraints of Computer Vision in Football

The efficacy of any computer vision (CV) pipeline—particularly those relying on multi-object tracking (e.g., ByteTrack) and spatial metric extraction—is fundamentally constrained by the physical properties of the video capture. Elite environments bypass this issue through multi-camera stadium arrays that map 3D spaces into accurate 2D tactical maps. Conversely, grassroots environments are restricted to single-camera, uncalibrated setups. 

To design an effective prototype, it is necessary to evaluate the feasibility of accessible recording methods against the algorithmic requirements of the AI.

### 1. Handheld Pitch-Level Recording (Smartphones)
- **Accessibility:** Extremely high. Requires no specialized hardware or setup time.
- **AI Feasibility:** Very Low. 
- **Limitations:** Recording from the sidelines at eye-level introduces severe *occlusion*, where players closer to the camera obscure those further away. Furthermore, at ground level, the AI lacks depth perception. A 15-meter gap between a midfielder and a defender may appear as a 0-meter gap on a 2D screen. 
- **System Impact:** If restricted to pitch-level footage, the AI cannot calculate "team shape" or "compactness." It can only analyze localized, 1v1 interactions or simple ball-tracking events.

### 2. Aerial Recording (Drones)
- **Accessibility:** Low to Moderate. Requires a drone, a licensed pilot (depending on local regulations), and active operation.
- **AI Feasibility:** Extremely High.
- **Limitations:** While an overhead oblique angle provides perfect tactical mapping with zero occlusion, drones suffer from restrictive battery constraints (typically 20-30 minutes per flight), making them unfeasible for recording a full 90-minute amateur match without disruptive battery swaps. Furthermore, safety regulations often prohibit flying drones over active crowds or public parks where grassroots games occur.

### 3. Elevated Masts / Tall Tripods (The Optimal Compromise)
- **Accessibility:** High. This encompasses commercial AI cameras (e.g., Veo, Pixellot) or low-cost DIY alternatives such as a smartphone mounted on a 5-to-7-meter painter's pole or lighting stand placed at the halfway line.
- **AI Feasibility:** High.
- **System Impact:** The 5-7 meter elevation significantly mitigates occlusion, allowing the YOLOv8 detection model to clearly distinguish individual players. More importantly, the elevated oblique angle provides enough depth representation for the AI to calculate relative spatial metrics (such as the convex hull area of a defensive line).

## Proposed Hardware Methodology for the GTA Prototype

Based on the feasibility analysis above, the Grassroots Tactical Assistant (GTA) will be optimized for **Elevated Mast Recording**. 

By assuming a minimum recording elevation of 4 meters (achievable via a standard heavy-duty tripod or budget mast), the system strikes the necessary balance. It avoids the financial and logistical barriers of drones and multi-camera stadium setups, while providing the AI pipeline with sufficient depth perception to calculate the collective tactical behaviors (e.g., team shape, defensive spacing) that coaches value most. 

The user workflow remains strictly grassroots: the coach sets up the mast at the halfway line, presses record, and uploads the single MP4 file post-match for automated analysis.
