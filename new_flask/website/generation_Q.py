from Questgen import main
from flask import jsonify


# Function to generate questions
def generate_questions(text):
    qe = main.BoolQGen() 
    payload = {
        "input_text": text,
    }
    try:
        questions = qe.predict_shortq(payload)
        return questions
    except Exception as e:
        # Log the exception and return an error message
        print(f"An error occurred during question generation: {e}")
        return jsonify({"error": "An error occurred during question generation"}), 500




















# from flask import Blueprint, request, jsonify
# from transformers import pipeline

# # Blueprint for question generation routes
# generation_Q = Blueprint('generation_Q', __name__)

# # Load the question-generation pipeline
# question_generator = pipeline('question-generation')

# # Route to generate questions from text
# @generation_Q.route('/generate_questions', methods=['POST'])
# def generate_questions():
#     try:
#         data = request.get_json()
#         text = data.get('text')
#         # Generate questions using the pipeline
#         generated_questions = question_generator(text)
#         return jsonify(generated_questions), 200
#     except Exception as e:
#         return jsonify({"error": str(e)}), 500
