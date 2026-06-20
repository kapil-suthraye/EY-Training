from deepface import DeepFace

def analyze_image(image_path):

    result = DeepFace.analyze(
        img_path=image_path,
        actions=["emotion"],
        detector_backend="opencv",
        enforce_detection=False
    )

    return {
        "dominant_emotion":
            result[0]["dominant_emotion"],

        "emotions":
            result[0]["emotion"]
    }