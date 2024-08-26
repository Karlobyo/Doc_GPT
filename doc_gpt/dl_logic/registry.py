from transformers import pipeline

def load_summary_model():
    pipe_summary = pipeline("summarization", model="sshleifer/distilbart-xsum-12-6")
    return pipe_summary
