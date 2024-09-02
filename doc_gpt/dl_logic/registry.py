from transformers import pipeline

def load_summary_model():
    pipe_summary = pipeline("summarization", model="sshleifer/distilbart-xsum-12-6")
    return pipe_summary


def load_document_model_text():
    pipe_qa = pipeline("question-answering", model="deepset/roberta-base-squad2")
    return pipe_qa


def load_document_model():
    pipe_doc = pipeline("document-question-answering", model="impira/layoutlm-invoices")
    return pipe_doc
