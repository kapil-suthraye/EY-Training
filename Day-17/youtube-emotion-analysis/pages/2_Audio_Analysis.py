import streamlit as st
import pandas as pd

from modules.audio_emotion import (
    analyze_audio
)

from utils.charts import (
    audio_chart
)

st.title(
    "Audio Emotion Analysis"
)

audio_file = st.file_uploader(
    "Upload Audio",
    type=["wav", "mp3"]
)

if audio_file:

    audio_path = "uploads/audio.wav"

    with open(audio_path, "wb") as f:
        f.write(
            audio_file.getbuffer()
        )

    st.audio(audio_file)

    if st.button(
        "Analyze Audio"
    ):

        with st.spinner(
            "Analyzing audio..."
        ):

            result = analyze_audio(
                audio_path
            )

        st.subheader(
            "Emotion Scores"
        )

        st.write(result)

        fig = audio_chart(
            result
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

        dominant = max(
            result,
            key=lambda x: x["score"]
        )

        st.metric(
            "Dominant Emotion",
            dominant["label"]
        )