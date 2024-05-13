from Questgen import main

payload = {
    "input_text": """my name is mai and i like watching movies. I am 19 years old .""",
    "input_question": ["What does mai like?","how old is mai?"]
}


predictor = main.AnswerPredictor()
answers = predictor.predict_answer(payload)


print(answers)