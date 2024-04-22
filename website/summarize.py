from summarizer import Summarizer

def summarize_text(text):
    model = Summarizer()
    summary = model(text)
    return summary

#you  use the bert-extractive-summarizer which works well with modern NLP approaches