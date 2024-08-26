
from doc_gpt.dl_logic.registry import load_summary_model, load_document_model

#from transformers import pipeline

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Allowing all middleware is optional, but good practice for dev purposes
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

app.state.model = load_summary_model()

@app.get("/summarize")
def predict(question: str):
    """
    Summarizes input text.
    """

    model = app.state.model
    assert model is not None

    response = model(question)

    output = response[0]["summary_text"]

    # ⚠️ fastapi only accepts simple Python data types as a return value
    # among them dict, list, str, int, float, bool
    # in order to be able to convert the api response to JSON
    return output

app.state.model = load_document_model()

@app.get("/document")
def predict(doc_url: str, question: str):
    """
    Gives you answers about input document
    """

    model = app.state.model
    assert model is not None

    response = model(doc_url, question)

    output = response[0]["answer"]

    # ⚠️ fastapi only accepts simple Python data types as a return value
    # among them dict, list, str, int, float, bool
    # in order to be able to convert the api response to JSON
    return output


@app.get("/")
def root():
    return dict(greeting="Hello")
