# this is where a youtube url is coverted into an audio file

import yt_dlp
import os

class AudioExtractor:
    def __init__(self, download_path: str = "downloads/"):
        self.download_path = download_path
        os.makedirs(download_path, exist_ok=True)
    
    def extract_audio(self, youtube_url: str) -> str:
        """Takes a YouTube URL, returns path to audio file"""
        # Configuration for yt-dlp
        ydl_opts = {
            'format': 'bestaudio/best',
            'outtmpl': f'{self.download_path}%(title)s.%(ext)s',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
        }
        
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(youtube_url, download=False)
            title = info.get('title', 'video')
            ydl.download([youtube_url])
            
            return f"{self.download_path}{title}.mp3"
