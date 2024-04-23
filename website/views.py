from flask import Blueprint, request
from .transcribe import transcribe_audio  # Import the transcription function
from .summarize import summarize_text     # Import the summarize function
from .question_gen import generate_questions   # Import the generate_ questions function


views = Blueprint('views', __name__)

@views.route('/transcribe', methods=['POST'])
def transcribe_route():
    if 'file' not in request.files:
        return 'No file part', 400
    file = request.files['file']
    if file.filename == '':
        return 'No selected file', 400
    if file:
        transcription = transcribe_audio(file)
        # Save transcription to database or pass to frontend
        return transcription, 200
    

@views.route('/summarize', methods=['POST'])
def summarize_route():
    # Get 'text' from the request data
    text = request.form['text']  # or request.json['text'] if JSON is used
    summary = summarize_text(text)
    return summary

@views.route('/questions', methods=['POST'])
def questions_route():
    # Get 'text' from the request data
    text = request.form['text']  # or request.json['text'] if JSON is used
    questions = generate_questions(text)
    return questions


