import yt_dlp
import subprocess

from modules.video_emotion import analyze_video
from modules.audio_emotion import analyze_audio


def analyze_youtube(url):

    video_path = "uploads/youtube_video.mp4"

    ydl_opts = {
        "format": "mp4",
        "outtmpl": video_path
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

    audio_path = "uploads/youtube_audio.wav"

    subprocess.run(
        [
            "ffmpeg",
            "-i",
            video_path,
            audio_path,
            "-y"
        ]
    )

    video_result = analyze_video(
        video_path
    )

    audio_result = analyze_audio(
        audio_path
    )

    return {
        "video_emotion": video_result,
        "audio_emotion": audio_result
    }