import streamlit as st

from modules.video_emotion import (
    analyze_video
)

from utils.charts import (
    video_chart
)

from utils.emotion_helper import (
    emotion_descriptions
)

st.title(
    "Video Emotion Analysis"
)

video_file = st.file_uploader(
    "Upload Video",
    type=[
        "mp4",
        "avi",
        "mov"
    ]
)

if video_file:

    video_path = "uploads/video.mp4"

    with open(video_path, "wb") as f:
        f.write(
            video_file.getbuffer()
        )

    st.video(video_file)

    if st.button(
        "Analyze Video"
    ):

        with st.spinner(
            "Analyzing video..."
        ):

            result = analyze_video(
                video_path
            )

        st.write(result)

        dominant = max(
            result,
            key=result.get
        )

        st.metric(
            "Dominant Emotion",
            dominant.upper()
        )

        st.info(
            emotion_descriptions.get(
                dominant,
                "No explanation available."
            )
        )

        fig = video_chart(
            result
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )