# Hand Gesture Detection

This is a simple hand gesture detection project using OpenCV and MediaPipe.

## Features

- Detects hand gestures in real-time using your webcam.
- Draws landmarks on detected hands.

## Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/yourusername/hand-gesture-detection.git
    cd hand-gesture-detection
    ```

2. **Create and activate a virtual environment:**

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

## Usage 

1. **Run the hand gesture detection script:**

    ```bash
    python src/hand_gesture_detection.py
    ```

2. **Interact with the Webcam:**

   - The script will open your front camera and start detecting hand gestures.
   - You should see real-time hand landmarks drawn on the video feed.
   - Press 'q' to close the webcam window and stop the script.

## Directory Structure

- `src/`: Contains the main Python script for hand gesture detection.
   - `hand_gesture_detection.py` : The primary script for capturing video from the front camera and detecting hand gestures using MediaPipe.
- `images/`: Contains example output images and screenshots.
- `requirements.txt`: Lists the Python dependencies.
- `README.md`: Provides an overview of the project.

## Additional Information

   - Dependencies:
     - `opencv-python` : For capturing video and image processing.
     - `mediapipe` : For hand gesture detection and drawing landmarks.

---
