from questgen import main

# Function to generate questions
def generate_questions(text):
    qe= main.BoolQGen() 
    payload = {
        "input_text": text,
    }
    questions = qe.predict_shortq(payload)
    return questions
