import numpy as np

def check_motion_consistency(motion_data):
    """
    Analyzes motion data to check for consistency.
    If motion is inconsistent (suggesting manipulation), it returns "Fake".
    """
    # Motion data is expected to be a list of (dx, dy) vectors
    magnitudes = np.linalg.norm(motion_data, axis=1)  # Calculate magnitudes of motion vectors

    # Calculate the standard deviation of the magnitudes
    std_dev = np.std(magnitudes)

    # If the standard deviation is too high, it suggests large, erratic movements typical of fake edits
    if std_dev > 10:  # Adjust this threshold based on experimentation
        return "Fake"
    else:
        return "Real"
