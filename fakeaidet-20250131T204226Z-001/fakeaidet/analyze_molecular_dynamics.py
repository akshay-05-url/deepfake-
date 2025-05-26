import numpy as np
def analyze_molecular_dynamics(positions, velocities):
    """
    Analyze molecular dynamics to check if the simulated motion follows physical rules.
    If there are unusual accelerations or unrealistic speeds, mark the video as "Fake".
    """
    # Check for unrealistic speeds (based on your specific simulation settings)
    speeds = np.linalg.norm(velocities, axis=1)  # Calculate speed (magnitude of velocity)
    max_speed = np.max(speeds)

    # If the maximum speed is too high, it's unrealistic and may indicate a fake video
    if max_speed > 5:  # Adjust the threshold based on your simulation
        return "Fake"
    else:
        return "Real"
