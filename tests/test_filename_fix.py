# test_filename_fix.py
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from src.audio_extractor import AudioExtractor

def test_filename_sanitisation():
    extractor = AudioExtractor()
    
    # Test the sanitisation function
    test_titles = [
        'Peaches & Cream "Chips and Salsa"',
        'Simple Recipe: Easy & Quick!',
        'How to Cook <Perfect> Pasta',
        'Recipe/Instructions\\File'
    ]
    
    for title in test_titles:
        safe_title = extractor._sanitise_filename(title)
        print(f"Original: {title}")
        print(f"Sanitised: {safe_title}")
        print("-" * 40)

if __name__ == "__main__":
    test_filename_sanitisation()