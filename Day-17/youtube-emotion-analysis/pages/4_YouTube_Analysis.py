import streamlit as st

from modules.youtube_emotion import (
    analyze_youtube
)

from utils.charts import (
    youtube_video_chart,
    youtube_audio_chart
)

from utils.emotion_helper import (
    emotion_descriptions
)

st.title(
    "YouTube Emotion Analysis"
)

youtube_url = st.text_input(
    "Paste YouTube URL"
)

if st.button(
    "Analyze YouTube Video"
):

    with st.spinner(
        "Downloading and analyzing..."
    ):

        result = analyze_youtube(
            youtube_url
        )

    # ----------------------------------
    # VIDEO RESULTS
    # ----------------------------------

    st.subheader(
        "Video Emotion Analysis"
    )

    video_result = result[
        "video_emotion"
    ]

    dominant_video = max(
        video_result,
        key=video_result.get
    )

    st.metric(
        "Dominant Video Emotion",
        dominant_video.upper()
    )

    st.info(
        emotion_descriptions.get(
            dominant_video,
            "No explanation available."
        )
    )

    video_fig = youtube_video_chart(
        video_result
    )

    st.plotly_chart(
        video_fig,
        use_container_width=True
    )

    # ----------------------------------
    # AUDIO RESULTS
    # ----------------------------------

    st.subheader(
        "Audio Emotion Analysis"
    )

    audio_result = result[
        "audio_emotion"
    ]

    dominant_audio = max(
        audio_result,
        key=lambda x: x["score"]
    )

    st.metric(
        "Dominant Audio Emotion",
        dominant_audio["label"]
    )

    audio_fig = youtube_audio_chart(
        audio_result
    )

    st.plotly_chart(
        audio_fig,
        use_container_width=True
    )

    st.subheader(
    "Final Emotion Summary"
)

    if dominant_video.lower() == dominant_audio["label"].lower():

        st.success(
            f"Overall Emotion: {dominant_video.upper()}"
        )

    else:

        st.warning(
            f"""
            Video indicates: {dominant_video.upper()}

            Audio indicates: {dominant_audio['label'].upper()}
            """
        )