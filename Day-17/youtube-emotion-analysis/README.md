# Emotion Intelligence Platform

## Overview

Emotion Intelligence Platform is a multimodal AI application that analyzes human emotions from multiple data sources including:

* Images
* Audio Files
* Video Files
* YouTube Videos

The platform leverages Computer Vision, Speech Intelligence, and Deep Learning models to identify emotional states and present insights through an interactive Streamlit dashboard.

The project demonstrates the practical application of multimodal AI systems by combining facial emotion recognition, voice emotion analysis, video frame processing, and YouTube content analysis into a unified platform.

---

## Key Features

### Image Emotion Analysis

* Detects emotions from facial expressions in uploaded images
* Supports JPG, JPEG, and PNG formats
* Identifies dominant emotion
* Displays confidence distribution across emotion categories
* Interactive visualization dashboard

### Audio Emotion Analysis

* Analyzes emotional tone from speech recordings
* Supports WAV and MP3 formats
* Classifies emotional patterns in voice signals
* Displays emotion confidence scores
* Generates visual emotion analytics

### Video Emotion Analysis

* Processes video frames using computer vision
* Extracts facial emotions across multiple frames
* Calculates dominant emotion across the entire video
* Generates emotion distribution reports
* Supports MP4, AVI, and MOV formats

### YouTube Emotion Analysis

* Downloads YouTube videos using yt-dlp
* Extracts video stream for facial emotion analysis
* Extracts audio stream for speech emotion analysis
* Performs multimodal emotion detection
* Generates combined emotion insights
* Fully automated analysis pipeline

---

## Architecture

```text
User Input
    │
    ▼
Streamlit Frontend
    │
    ├─────────────► Image Module
    │                    │
    │                    ▼
    │              DeepFace
    │
    ├─────────────► Audio Module
    │                    │
    │                    ▼
    │          Wav2Vec2 Emotion Model
    │
    ├─────────────► Video Module
    │                    │
    │                    ▼
    │           Frame-by-Frame Analysis
    │
    └─────────────► YouTube Module
                         │
          ┌──────────────┴──────────────┐
          ▼                             ▼
     Video Analysis               Audio Analysis
          │                             │
          └──────────────┬──────────────┘
                         ▼
                 Emotion Dashboard
```

---

## Technology Stack

### Frontend

* Streamlit
* Plotly

### Computer Vision

* OpenCV
* DeepFace

### Audio Intelligence

* Hugging Face Transformers
* Wav2Vec2

### Video Processing

* OpenCV
* FFmpeg

### YouTube Integration

* yt-dlp

### Data Processing

* Pandas
* NumPy

### AI/ML Frameworks

* TensorFlow
* PyTorch
* Hugging Face

---

## Project Structure

```text
emotion-analyzer/
│
├── app.py
│
├── pages/
│   ├── 1_Image_Analysis.py
│   ├── 2_Audio_Analysis.py
│   ├── 3_Video_Analysis.py
│   └── 4_YouTube_Analysis.py
│
├── modules/
│   ├── image_emotion.py
│   ├── audio_emotion.py
│   ├── video_emotion.py
│   ├── youtube_emotion.py
│   └── text_emotion.py
│
├── utils/
│   ├── charts.py
│   └── emotion_helper.py
│
├── uploads/
├── outputs/
├── assets/
└── requirements.txt
```

---

## AI Models Used

### Facial Emotion Recognition

DeepFace Emotion Recognition Model

Supported Emotions:

* Happy
* Sad
* Angry
* Fear
* Surprise
* Neutral
* Disgust

### Speech Emotion Recognition

Model:

```text
superb/wav2vec2-base-superb-er
```

Capabilities:

* Speech feature extraction
* Emotion classification
* Confidence scoring

---

## Installation

### Clone Repository

```bash
git clone https://github.com/your-username/emotion-intelligence-platform.git

cd emotion-intelligence-platform
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Environment

Windows:

```bash
venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## FFmpeg Setup

Download FFmpeg and add it to your system PATH.

Verify installation:

```bash
ffmpeg -version
```

---

## Run Application

```bash
streamlit run app.py
```

Application will be available at:

```text
http://localhost:8501
```

---

## Sample Workflow

### YouTube Emotion Analysis

1. Paste YouTube URL
2. Download video automatically
3. Extract audio using FFmpeg
4. Analyze video frames using DeepFace
5. Analyze speech using Wav2Vec2
6. Generate emotion insights
7. Visualize results using Plotly

---

## Business Applications

### Customer Experience Analytics

Analyze customer sentiment from video reviews and feedback sessions.

### Human Resources

Evaluate employee engagement and communication patterns.

### Media Intelligence

Analyze emotional responses in interviews, podcasts, and social media content.

### Mental Health Monitoring

Support emotion-aware wellness applications.

### Content Analytics

Measure emotional tone across multimedia content.

---

## Highlights

* Multimodal AI System
* Computer Vision Pipeline
* Speech Intelligence Pipeline
* YouTube Content Processing
* Real-Time Analytics Dashboard
* Modular Architecture
* Scalable Design
* Free and Open-Source Technology Stack

---

## Future Enhancements

* Real-Time Webcam Emotion Detection
* Live Microphone Emotion Analysis
* Whisper-based Transcription
* Text Sentiment Analysis
* Emotion Timeline Visualization
* PDF Report Generation
* LLM-Powered Emotion Summaries
* Cloud Deployment on Azure/GCP

---

## Learning Outcomes

This project demonstrates practical experience in:

* Generative AI Applications
* Multimodal AI Systems
* Computer Vision
* Audio Intelligence
* Deep Learning Integration
* Streamlit Development
* Data Visualization
* End-to-End AI Product Development

---

## Author

Kapil Suthraye

AI & Data Engineer

Specializing in:

* Generative AI
* Data Engineering
* Machine Learning
* Multi-Agent Systems
* Cloud Data Platforms
