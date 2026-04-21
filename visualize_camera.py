import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as patches

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))

# --- Plot 1: Top-Down FOV Proof ---
# Pitch dimensions: 100m length x 64m width
pitch_rect = patches.Rectangle((0, 0), 100, 64, linewidth=2, edgecolor='green', facecolor='lightgreen', zorder=1)
ax1.add_patch(pitch_rect)

# Camera placed at halfway line (x=50), 5 meters back (y=-5)
cam_x, cam_y = 50, -5
ax1.plot(cam_x, cam_y, 'ko', markersize=8, label="Camera Lens", zorder=3)

# 75 degree FOV (Standard Lens)
# Half-angle = 37.5 degrees
dist_75 = 64 - cam_y # distance to far sideline
spread_75 = dist_75 * np.tan(np.radians(37.5))
ax1.fill([cam_x, cam_x - spread_75, cam_x + spread_75], [cam_y, 64, 64], color='blue', alpha=0.3, label="Standard Lens (75° FOV)", zorder=2)

# 120 degree FOV (Ultrawide)
spread_120 = dist_75 * np.tan(np.radians(60))
ax1.fill([cam_x, cam_x - spread_120, cam_x + spread_120], [cam_y, 64, 64], color='red', alpha=0.2, label="Ultrawide Lens (120° FOV)", zorder=2)

ax1.set_xlim(-20, 120)
ax1.set_ylim(-10, 70)
ax1.set_aspect('equal')
ax1.set_title("Top-Down FOV Proof:\nWhy One Camera Cannot Capture 100m")
ax1.set_xlabel("Pitch Length (m)")
ax1.set_ylabel("Pitch Width (m)")
ax1.legend()

# --- Plot 2: Side-Profile Occlusion Proof ---
cam_height = 5
dist_near = 2 # Player 2m away
dist_far = 66 # Far sideline player
player_h = 1.8

# Plot Camera
ax2.plot(0, cam_height, 'ko', markersize=8, label="Camera (5m Mast)")

# Plot Near Player (The Obstacle)
ax2.plot([dist_near, dist_near], [0, player_h], 'b-', linewidth=4, label="Near Player (1.8m)")
ax2.plot(dist_near, player_h, 'bo', markersize=6) # Head

# Plot Far Player (The Target)
ax2.plot([dist_far, dist_far], [0, player_h], 'r-', linewidth=4, label="Far Player (1.8m)")
ax2.plot(dist_far, 0, 'ro', markersize=6) # Feet

# Plot Sightline from Camera to Far Player Feet
ax2.plot([0, dist_far], [cam_height, 0], 'g--', linewidth=2, label="Line of Sight")

# Calculate sightline height at the near player's position
slope = (0 - cam_height) / (dist_far - 0)
height_at_near = cam_height + slope * dist_near
ax2.plot(dist_near, height_at_near, 'go', markersize=8, label=f"Clearance Height: {height_at_near:.2f}m")

# Visual line showing the clearance over the head
ax2.plot([dist_near, dist_near], [player_h, height_at_near], 'm:', linewidth=2, label=f"Safe Clearance: {height_at_near - player_h:.2f}m")

ax2.set_xlim(-5, 70)
ax2.set_ylim(0, 6)
ax2.set_title("Side-Profile Occlusion Proof:\nHow a 5m Mast Sees Over Players")
ax2.set_xlabel("Distance from Camera Base (m)")
ax2.set_ylabel("Height (m)")
ax2.legend()
ax2.grid(True)

plt.tight_layout()
plt.savefig(r'C:\Users\thana\.gemini\antigravity\brain\3d9f4ef6-ffad-4438-bcfb-afa2d8649a80\camera_proof.png', dpi=150)
print('Saved camera_proof.png')
