# gradio_app.py
import gradio as gr
import sys
import os

# Add project root to path
sys.path.insert(0, os.path.dirname(__file__))

from src.pipeline import RecipeWhisperPipeline

def process_youtube_video_with_progress(youtube_url, progress=gr.Progress()):
    """Process YouTube video with clean progress updates"""
    
    if not youtube_url:
        return ""
    
    if not youtube_url.startswith(("https://www.youtube.com", "https://youtu.be")):
        return '<div class="error-card">Please enter a valid YouTube URL</div>'
    
    try:
        # Step 1: Initialize
        progress(0, desc="Initializing pipeline...")
        
        pipeline = RecipeWhisperPipeline()
        
        # Step 2: Audio extraction
        progress(0.2, desc="Extracting audio from YouTube...")
        audio_file = pipeline.audio_extractor.extract_audio(youtube_url)
        
        # Step 3: Transcription
        progress(0.5, desc="Converting audio to text...")
        transcript = pipeline.transcriber.transcribe(audio_file)
        
        # Step 4: Recipe parsing
        progress(0.8, desc="Parsing recipe with AI...")
        recipe = pipeline.recipe_parser.parse_transcript(transcript)
        
        # Step 5: Cleanup
        progress(0.95, desc="Cleaning up...")
        try:
            os.remove(audio_file)
        except:
            pass
        
        progress(1.0, desc="Complete!")
        
        # Format the final output with custom styling
        ingredients_html = ""
        for ingredient in recipe.ingredients:
            amount_unit = f"{ingredient.amount} {ingredient.unit}".strip() if ingredient.amount else ""
            if amount_unit:
                ingredients_html += f"<li><strong>{ingredient.name}</strong> - {amount_unit}</li>\n"
            else:
                ingredients_html += f"<li><strong>{ingredient.name}</strong></li>\n"
        
        instructions_html = ""
        for step in recipe.instructions:
            instructions_html += f"<div class='instruction-step'><strong>{step.step_number}.</strong> {step.instruction}</div>\n"
        
        output = f"""
        <div class="recipe-card">
            <h2 class="recipe-title">{recipe.title}</h2>
            
            <div class="ingredients-section">
                <h3>Ingredients ({len(recipe.ingredients)})</h3>
                <ul class="ingredients-list">
                    {ingredients_html}
                </ul>
            </div>
            
            <div class="instructions-section">
                <h3>Instructions ({len(recipe.instructions)})</h3>
                {instructions_html}
            </div>
        </div>
        """
        
        return output
        
    except Exception as e:
        return f'<div class="error-card">Error processing video: {str(e)}<br><br>Try a different video or check if the URL is accessible</div>'

# Create Gradio interface with custom CSS
def create_interface():
    
    # Enhanced CSS with more specific selectors
    custom_css = """
    /* Main theme colors */
    .gradio-container {
        background: #f8fffe !important;
    }
    
    /* Header styling */
    .main-header {
        text-align: center;
        color: #2d5a27 !important;
        margin-bottom: 30px;
    }
    
    /* Force button styling with high specificity */
    button.btn.btn-lg.btn-primary,
    .btn-primary,
    button[variant="primary"],
    .gradio-button.primary {
        background: #2d5a27 !important;
        background-color: #2d5a27 !important;
        border-color: #2d5a27 !important;
        color: white !important;
    }
    
    button.btn.btn-lg.btn-primary:hover,
    .btn-primary:hover,
    button[variant="primary"]:hover,
    .gradio-button.primary:hover {
        background: #1a3318 !important;
        background-color: #1a3318 !important;
        border-color: #1a3318 !important;
        color: white !important;
    }
    
    /* Force textbox label styling */
    .gradio-textbox label,
    .gr-textbox label,
    label[for*="textbox"],
    .input-label {
        color: #2d5a27 !important;
        font-weight: 600 !important;
    }
    
    /* Force textbox input styling */
    .gradio-textbox input,
    .gr-textbox input,
    input[type="text"],
    .input-field {
        border: 2px solid #2d5a27 !important;
        border-color: #2d5a27 !important;
    }
    
    .gradio-textbox input:focus,
    .gr-textbox input:focus,
    input[type="text"]:focus,
    .input-field:focus {
        border-color: #2d5a27 !important;
        box-shadow: 0 0 0 2px rgba(45, 90, 39, 0.2) !important;
        outline: none !important;
    }
    
    /* Override any purple/blue styling */
    * {
        --primary-500: #2d5a27 !important;
        --primary-600: #1a3318 !important;
    }
    
    /* Recipe card styling */
    .recipe-card {
        background: #f0f8f0 !important;
        border: 2px solid #c8e6c9 !important;
        border-radius: 15px !important;
        padding: 25px !important;
        margin: 20px 0 !important;
        box-shadow: 0 4px 6px rgba(45, 90, 39, 0.1) !important;
    }
    
    .recipe-title {
        color: #2d5a27 !important;
        font-size: 1.8em !important;
        margin-bottom: 20px !important;
        text-align: center !important;
        border-bottom: 2px solid #c8e6c9 !important;
        padding-bottom: 10px !important;
    }
    
    .ingredients-section, .instructions-section {
        margin: 20px 0 !important;
    }
    
    .ingredients-section h3, .instructions-section h3 {
        color: #2d5a27 !important;
        font-size: 1.3em !important;
        margin-bottom: 15px !important;
    }
    
    /* Ingredients list styling */
    .ingredients-list {
        list-style: none !important;
        padding: 0 !important;
        margin: 0 !important;
    }
    
    .ingredients-list li {
        background: #ffffff !important;
        border: 1px solid #c8e6c9 !important;
        border-radius: 8px !important;
        padding: 10px 15px !important;
        margin: 8px 0 !important;
        position: relative !important;
        padding-left: 30px !important;
    }
    
    .ingredients-list li:before {
        content: "•" !important;
        color: #2d5a27 !important;
        font-weight: bold !important;
        position: absolute !important;
        left: 15px !important;
        font-size: 1.2em !important;
    }
    
    /* Instructions styling */
    .instruction-step {
        background: #ffffff !important;
        border: 1px solid #c8e6c9 !important;
        border-radius: 8px !important;
        padding: 15px !important;
        margin: 10px 0 !important;
        border-left: 4px solid #2d5a27 !important;
    }
    
    .instruction-step strong {
        color: #2d5a27 !important;
    }
    
    /* Error card styling */
    .error-card {
        background: #ffebee !important;
        color: #c62828 !important;
        border: 2px solid #ef9a9a !important;
        border-radius: 10px !important;
        padding: 20px !important;
        margin: 20px 0 !important;
    }
    
    /* Progress bar styling */
    .progress-bar,
    .progress-bar-fill {
        background: #2d5a27 !important;
    }
    """
    
    # Alternative: Use Gradio's built-in green theme
    green_theme = gr.themes.Soft(
        primary_hue="green",
        secondary_hue="green",
        neutral_hue="slate",
    ).set(
        button_primary_background_fill="#2d5a27",
        button_primary_background_fill_hover="#1a3318",
        button_primary_border_color="#2d5a27",
        button_primary_text_color="#ffffff",
        input_border_color="#2d5a27",
        input_border_color_focus="#2d5a27",
    )
    
    with gr.Blocks(title="RecipeWhisper", theme=green_theme, css=custom_css) as demo:
        
        gr.HTML("""
        <div class="main-header">
            <h1>RecipeWhisper</h1>
            <p>Transform cooking videos into structured recipes using AI</p>
        </div>
        """)
        
        with gr.Row():
            with gr.Column(scale=4):
                url_input = gr.Textbox(
                    label="YouTube URL",
                    placeholder="https://www.youtube.com/watch?v=...",
                    lines=1
                )
            with gr.Column(scale=1):
                submit_btn = gr.Button("Extract Recipe", variant="primary")
        
        output = gr.HTML(label="Recipe Output")
        
        # Connect the function with progress
        submit_btn.click(
            fn=process_youtube_video_with_progress,
            inputs=[url_input],
            outputs=[output]
        )
        
        # Also allow Enter key to submit
        url_input.submit(
            fn=process_youtube_video_with_progress,
            inputs=[url_input],
            outputs=[output]
        )
    
    return demo

if __name__ == "__main__":
    # Create and launch the interface
    demo = create_interface()
    
    # Launch the app
    demo.launch(
        server_name="0.0.0.0",
        server_port=7860,
        share=False,
        show_error=True
    )