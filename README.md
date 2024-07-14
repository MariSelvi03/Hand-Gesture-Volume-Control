# Hand Gesture Volume Control

  This project uses computer vision and machine learning to detect hand gestures and control the volume on your computer. It leverages 
  OpenCV for video capture and MediaPipe for hand tracking.

## Project Setup and Structure

   **Installation Instructions**
   1. **Clone the repository:**

   ```sh
   git clone https://github.com/yourusername/hand-gesture-volume-control.git
   cd hand-gesture-volume-control
   ```

   2. **Create and activate a virtual environment:**

   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

   3. **Install the dependencies:**

   ```sh
   pip install -r requirements.txt
   ```
   **Usage**
  1. **Run the Python script:**

  ```sh
  python hand_gesture_volume_control.py
  ```

  2. **Control the volume using hand gestures:**

  - Open your hand in front of the camera to increase the volume.
  - Close your hand to decrease the volume.
    
  ## Explanation of Files and Folders
  
  - images/: This folder contains the output images from the hand detection and gesture recognition process.
    
  - gesture_detection_example.png: Example image showing hand landmarks and gesture detection.
    
  - hand_gesture_volume_control.py: The main script for capturing video, detecting hand gestures, and controlling the volume.
    
  - requirements.txt: Lists all the Python packages required to run the project.
    
  - README.md: Provides an overview of the project, installation instructions, usage instructions, and explanations of the files 
      and folders.

  ## Additional Information 
   - **Dependencies:**
     - **opencv-python**: For real-time computer vision.
     - **mediapipe**: For hand gesture detection and tracking.
---
