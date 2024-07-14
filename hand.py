import cv2
import mediapipe as mp
import numpy as np
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL

mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils

webcam = cv2.VideoCapture(0)

devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(
    IAudioEndpointVolume._iid_, CLSCTX_ALL, None
)
volume = cast(interface, POINTER(IAudioEndpointVolume))
volume_range = volume.GetVolumeRange()
min_volume = volume_range[0]
max_volume = volume_range[1]

def set_volume(volume_level):
    volume.SetMasterVolumeLevel(volume_level, None)

with mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.7, min_tracking_confidence=0.6) as hands:
    while webcam.isOpened():
        success, img = webcam.read()
        if not success:
            print("Ignoring empty camera frame.")
            continue

        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        results = hands.process(img)

        img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                mp_drawing.draw_landmarks(img, hand_landmarks, mp_hands.HAND_CONNECTIONS)
                
                index_finger_tip = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]
                wrist = hand_landmarks.landmark[mp_hands.HandLandmark.WRIST]

                distance = np.linalg.norm(
                    np.array([index_finger_tip.x, index_finger_tip.y]) - 
                    np.array([wrist.x, wrist.y])
                )

                volume_level = np.interp(distance, [0.1, 0.4], [min_volume, max_volume])
                set_volume(volume_level)

        cv2.imshow('Gesture Detection', img)
        if cv2.waitKey(5) & 0xFF == ord("q"):
            break

webcam.release()
cv2.destroyAllWindows()
