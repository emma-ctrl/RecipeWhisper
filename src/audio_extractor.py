# this is where a youtube url is coverted into an audio file

import yt_dlp
import os
import re

class AudioExtractor:
    def __init__(self, download_path: str = "downloads/"):
        self.download_path = download_path
        os.makedirs(download_path, exist_ok=True)

    def _sanitise_filename(self, filename: str) -> str:
        """Remove or replace problematic characters in filenames"""
        # Replace problematic characters with underscores
        filename = re.sub(r'[<>:"/\\|?*"]', '_', filename)
        # Remove multiple underscores
        filename = re.sub(r'_+', '_', filename)
        # Remove leading/trailing underscores
        filename = filename.strip('_')
        return filename
    
    def extract_audio(self, youtube_url: str) -> str:
        """Takes a YouTube URL, returns path to audio file"""
        
        # First get video info to get the title
        with yt_dlp.YoutubeDL({'quiet': True}) as ydl:
            info = ydl.extract_info(youtube_url, download=False)
            original_title = info.get('title', 'video')
        
        # Sanitise the title for the filename
        safe_title = self._sanitise_filename(original_title)
        
        # Configuration for yt-dlp with sanitised filename
        ydl_opts = {
            'format': 'bestaudio/best',
            'outtmpl': f'{self.download_path}{safe_title}.%(ext)s',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
        }
        
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([youtube_url])
            
            return f"{self.download_path}{safe_title}.mp3"
