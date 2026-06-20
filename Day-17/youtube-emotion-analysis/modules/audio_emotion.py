from transformers import pipeline

classifier = pipeline(
    task="audio-classification",
    model="superb/wav2vec2-base-superb-er"
)

def analyze_audio(audio_path):

    result = classifier(audio_path)

    return result