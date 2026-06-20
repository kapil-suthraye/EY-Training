import cv2

from collections import Counter

from deepface import DeepFace


def analyze_video(video_path):

    cap = cv2.VideoCapture(video_path)

    emotions = []

    frame_count = 0

    while True:

        ret, frame = cap.read()

        if not ret:
            break

        frame_count += 1

        if frame_count % 30 != 0:
            continue

        try:

            result = DeepFace.analyze(
                frame,
                actions=["emotion"],
                enforce_detection=False
            )

            emotions.append(
                result[0]["dominant_emotion"]
            )

        except:
            pass

    cap.release()

    return Counter(emotions)