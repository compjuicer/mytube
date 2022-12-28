import os

from dotenv import load_dotenv

from flask import Flask

from yt_dlp import YoutubeDL

load_dotenv()

app = Flask(__name__)

audio_client = YoutubeDL({
    'ignoreerrors': True,
    'format': 'm4a',
    'extractaudio': True,
    'paths': { 'home': os.environ['AUDIO_FOLDER'] }
})

video_client = YoutubeDL({
    'ignoreerrors': True,
    'format': 'mp4',
    'paths': { 'home': os.environ['VIDEO_FOLDER'] }
})

@app.route('/download/audio/<id>')
def download_audio(id):
    result = audio_client.download(id)
    return f'{result}'

@app.route('/download/video/<id>')
def download_video(id):
    result = video_client.download(id)
    return f'{result}'

