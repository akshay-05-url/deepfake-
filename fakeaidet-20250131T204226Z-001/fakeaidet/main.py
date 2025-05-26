# Assuming all your functions are imported here
from extract_frames import extract_frames
from compute_optical_flow import compute_optical_flow,check_motion_consistency
from md_stimulation import simulate_molecular_dynamics

import analyze_molecular_dynamics

def detect_fake_video(video_path):
    """
    Main function to detect if a video is fake or real by:
    1. Extracting frames from the video
    2. Computing optical flow
    3. Analyzing motion consistency
    4. Simulating molecular dynamics
    5. Evaluating results and determining the video authenticity
    """
    
    print("Step 1: Extracting frames from video...")
    # Step 1: Extract frames from the video
    extract_frames(video_path, "extracted_frames", 1)  # Saves frames to 'extracted_frames' folder

    print("Step 2: Computing optical flow...")
    # Step 2: Compute Optical Flow to analyze motion
    motion_data = compute_optical_flow(video_path)

    print("Step 3: Checking motion consistency...")
    # Step 3: Check motion consistency using Optical Flow
    motion_check_result = check_motion_consistency(motion_data)

    print("Step 4: Simulating molecular dynamics...")
    # Step 4: Simulate Molecular Dynamics to analyze physical consistency
    positions, velocities = simulate_molecular_dynamics(motion_data)
    md_check_result = analyze_molecular_dynamics(positions, velocities)

    # Step 5: Combine the results from both analyses to determine if the video is real or fake
    if motion_check_result == "Fake" or md_check_result == "Fake":
        print("The video is likely FAKE.")
    else:
        print("The video is likely REAL.")

# Example usage
if __name__ == "__main__":
    # Set the video path to the file in the same directory
    video_path = "sample_video.mp4"  # Ensure your video file is in the same directory
    detect_fake_video(video_path)  # Automatically call the function with the provided video file
