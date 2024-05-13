from flask import Blueprint, request, jsonify
from .transcribe import transcribe_audio
from .summarize import summarize_text
from .generation_Q import generate_questions

views = Blueprint('views', __name__)

@views.route('/transcribe', methods=['POST'])
def transcribe_route():
    # Your existing code for transcribe route
    pass

@views.route('/summarize', methods=['POST'])
def summarize_route():
    # Your existing code for summarize route
    pass

@views.route('/questions', methods=['POST'])
def questions_route():
    # Your existing code for questions route
    pass
