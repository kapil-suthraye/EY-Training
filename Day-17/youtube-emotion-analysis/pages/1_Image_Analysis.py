import streamlit as st

from modules.image_emotion import analyze_image
from utils.charts import image_chart
from utils.emotion_helper import emotion_descriptions

st.title("Image Emotion Analysis")

uploaded_file = st.file_uploader(
    "Upload Image",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file:

    image_path = "uploads/temp.jpg"

    with open(image_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    st.image(
        uploaded_file,
        use_container_width=True
    )

    if st.button("Analyze Image"):

        with st.spinner(
            "Analyzing image..."
        ):

            result = analyze_image(
                image_path
            )

        dominant = result[
            "dominant_emotion"
        ]

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

        fig = image_chart(
            result["emotions"]
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )