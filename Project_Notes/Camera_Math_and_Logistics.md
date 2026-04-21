# Camera Mathematics and Logistics for Grassroots AI

This document provides the mathematical justification and logistical blueprints for capturing grassroots football footage capable of supporting AI analysis (like YOLOv8 tracking).

## 1. The 180-Degree Problem: Field of View (FOV) Mathematics

A standard football pitch is 100 meters long. Commercial systems like Veo use two lenses to capture a panoramic 180-degree view. To understand why a single smartphone cannot do this statically from the sideline, we apply basic right-angle trigonometry:

**Distance Required = (Length / 2) / tan(HFOV / 2)**

*   **Standard Smartphone Lens (~75° Horizontal FOV)**
    *   D = 50 / tan(37.5°)
    *   **Result:** The camera must be placed **65 meters** behind the sideline to fit the entire 100m length in the frame.
*   **Ultrawide Smartphone Lens (~120° Horizontal FOV)**
    *   D = 50 / tan(60°)
    *   **Result:** The camera must be placed **28.8 meters** behind the sideline.

**Conclusion:** It is physically impossible to capture the entire pitch statically using a single smartphone from a standard sideline (which typically has 2 to 5 meters of clearance before hitting fences or stands).

### Proposed Workarounds for the GTA Prototype:
Since a static single camera fails, the prototype must rely on one of three methods:
1.  **The Panning Approach:** A coach physically pans the mast (or uses an auto-tracking gimbal like a Pivo pod) to follow the ball. *AI Limitation: The AI must continuously calculate homography to account for the moving background.*
2.  **The "Veo Hack" (Dual Phones):** Mounting two cheap smartphones at a 45-degree diverging angle and stitching the video in post-production. *HCI Limitation: Increases setup complexity for the user.*
3.  **The Tactical Focus Approach (Recommended):** The camera uses an ultrawide lens and focuses statically on *one half* of the pitch (e.g., the defensive third). Tactical AI analysis is performed solely when the play enters this zone.

## 2. Avoiding Occlusion: The Height Mathematics

If a camera is at ground level, a player near the sideline will block the view of a player on the far sideline (occlusion). We must calculate the height required to see *over* the near player.

*   **Distance to near player:** ~2 meters.
*   **Distance to far player:** ~66 meters (far sideline).
*   **Player Height:** 1.8 meters.

If we place the camera at an elevated height of **5 meters**:
The geometric slope of the line of sight from the camera (5m) to the far player's feet (0m at 66m away) is 5 / 66 = 0.075.
At 2 meters away (where the near player stands), the line of sight drops by 2 * 0.075 = 0.15m.
Therefore, the camera's view crosses the near player at a height of **4.85 meters** off the ground.

**Conclusion:** A 5-meter mast provides a massive **3.05-meter vertical clearance** over the head of a 1.8m tall player standing on the near sideline. This proves mathematically that a 5-meter mast virtually eliminates severe occlusion, allowing YOLOv8 to track players flawlessly across the entire width of the pitch.

## 3. Physical Logistics: Building the Mast

For this system to be adopted by grassroots coaches, the hardware must be accessible, cheap, and safe. Here is the blueprint for a DIY grassroots mast:

*   **The Pole:** A 16-to-24-foot heavy-duty telescopic aluminum painter's pole (approx. - at a hardware store).
*   **The Base:** A heavy-duty lighting C-stand or speaker stand with a wide tripod footprint.
*   **The Weights:** At least two 20 lb (9 kg) sandbags draped over the tripod legs. A 5-meter pole acts as a sail in the wind; without sandbags, it will tip over and destroy the phone.
*   **The Mount:** A 1/4"-20 threaded painter's pole adapter attached to a smartphone clamp with an adjustable ball-head.
*   **The Workflow:** 
    1. Clamp the phone and angle it down toward the pitch.
    2. Connect a cheap Bluetooth remote shutter to the phone.
    3. Push the telescopic pole up to 5 meters and lock it.
    4. Click the Bluetooth remote to start recording right before kickoff.
