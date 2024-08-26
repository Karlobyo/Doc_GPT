
from doc_gpt.dl_logic.registry import load_summary_model

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

# $WIPE_BEGIN
# 💡 Preload the model to accelerate the predictions
# We want to avoid loading the heavy Deep Learning model from MLflow at each `get("/predict")`
# The trick is to load the model in memory when the Uvicorn server starts
# and then store the model in an `app.state.model` global variable, accessible across all routes!
# This will prove very useful for the Demo Day
app.state.model = load_summary_model()
# $WIPE_END

# http://127.0.0.1:8000/predict?pickup_datetime=2012-10-06 12:10:20&pickup_longitude=40.7614327&pickup_latitude=-73.9798156&dropoff_longitude=40.6513111&dropoff_latitude=-73.8803331&passenger_count=2
@app.get("/predict")
def predict(question: str):
    """
    Summarizes input text.
    """

    # 💡 Optional trick instead of writing each column name manually:
    # locals() gets us all of our arguments back as a dictionary
    # https://docs.python.org/3/library/functions.html#locals
    X_pred = question

    model = app.state.model
    assert model is not None

    y_pred = model(question)

    response = y_pred[0]["summary_text"]

    # ⚠️ fastapi only accepts simple Python data types as a return value
    # among them dict, list, str, int, float, bool
    # in order to be able to convert the api response to JSON
    return response
    # $CHA_END


@app.get("/")
def root():
    # $CHA_BEGIN
    return dict(greeting="Hello")
    # $CHA_END
