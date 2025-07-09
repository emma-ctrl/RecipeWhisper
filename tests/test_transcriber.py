# test_transcriber.py
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from src.transcriber import OpenAITranscriber
import os

def test_transcriber():
    print("=== Testing Transcriber ===")
    
    transcriber = OpenAITranscriber()
    print("Transcriber initialized")
    
    # For now, let's just test the initialization
    # Later we'll test with a real audio file
    print("Ready to transcribe audio files")
    
    # Test with OpenAI client
    try:
        # Simple test to verify API key works
        response = transcriber.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": "Say hello"}],
            max_tokens=5
        )
        print("OpenAI API connection working")
    except Exception as e:
        print(f"OpenAI API error: {e}")

if __name__ == "__main__":
    test_transcriber()