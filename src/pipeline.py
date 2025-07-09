# ochestrator that brings together all the compoents 

import os
from src.audio_extractor import AudioExtractor
from src.transcriber import OpenAITranscriber
from src.recipe_parser import RecipeParser
from src.models import Recipe

class RecipeWhisperPipeline:
    def __init__(self):
        self.audio_extractor = AudioExtractor()
        self.transcriber = OpenAITranscriber()
        self.recipe_parser = RecipeParser()
    
    def process_youtube_video(self, youtube_url: str) -> Recipe:
        """Complete pipeline: YouTube URL → Structured Recipe"""
        
        print("Step 1: Extracting audio from YouTube...")
        try:
            audio_file = self.audio_extractor.extract_audio(youtube_url)
            print(f"Audio extracted: {audio_file}")
        except Exception as e:
            raise Exception(f"Audio extraction failed: {e}")
        
        print("Step 2: Converting audio to transcript...")
        try:
            transcript = self.transcriber.transcribe(audio_file)
            print(f"Transcript generated ({len(transcript)} characters)")
        except Exception as e:
            raise Exception(f"Transcription failed: {e}")
        
        print("Step 3: Parsing transcript into structured recipe...")
        try:
            recipe = self.recipe_parser.parse_transcript(transcript)
            print(f"Recipe parsed: {recipe.title}")
        except Exception as e:
            raise Exception(f"Recipe parsing failed: {e}")
        
        # Clean up audio file
        try:
            os.remove(audio_file)
            print("Cleaned up temporary audio file")
        except:
            pass  # Don't fail if cleanup doesn't work
        
        return recipe
    
    def process_transcript_only(self, transcript: str) -> Recipe:
        """Skip audio extraction, just parse transcript"""
        return self.recipe_parser.parse_transcript(transcript)