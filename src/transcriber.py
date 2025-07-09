# this is where the audio is converted to text 

import openai
import os
from dotenv import load_dotenv

load_dotenv()

class OpenAITranscriber:
    def __init__(self):
        self.client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    
    def transcribe(self, audio_file_path: str) -> str:
        """Convert audio file to text using OpenAI Whisper API"""
        try:
            with open(audio_file_path, 'rb') as audio_file:
                transcript = self.client.audio.transcriptions.create(
                    model="whisper-1",
                    file=audio_file,
                    response_format="text"
                )
            return transcript
        except Exception as e:
            raise Exception(f"Transcription failed: {str(e)}")