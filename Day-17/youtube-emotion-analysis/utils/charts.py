import pandas as pd
import plotly.express as px


def image_chart(emotions):

    df = pd.DataFrame(
        emotions.items(),
        columns=[
            "Emotion",
            "Score"
        ]
    )

    return px.bar(
        df,
        x="Emotion",
        y="Score",
        title="Emotion Distribution"
    )


def audio_chart(result):

    df = pd.DataFrame(
        result
    )

    return px.bar(
        df,
        x="label",
        y="score",
        title="Audio Emotion Scores"
    )


def video_chart(result):

    df = pd.DataFrame(
        result.items(),
        columns=[
            "Emotion",
            "Count"
        ]
    )

    return px.pie(
        df,
        names="Emotion",
        values="Count",
        title="Video Emotion Distribution"
    )


def youtube_video_chart(video_result):

    df = pd.DataFrame(
        video_result.items(),
        columns=[
            "Emotion",
            "Count"
        ]
    )

    fig = px.pie(
        df,
        names="Emotion",
        values="Count",
        title="Video Emotion Distribution"
    )

    return fig


def youtube_audio_chart(audio_result):

    df = pd.DataFrame(
        audio_result
    )

    fig = px.bar(
        df,
        x="label",
        y="score",
        title="Audio Emotion Scores"
    )

    return fig