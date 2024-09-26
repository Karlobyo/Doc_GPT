
#from doc_gpt.dl_logic.registry import load_summary_model, load_document_model, load_document_model_text

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


# @app.get("/summarize")
# def summarize(text: str, min_length: int = 20, max_length: int = 50):
#     """
#     Summarizes input text.
#     """

#     app.state.model = load_summary_model()

#     model = app.state.model
#     assert model is not None

#     response = model(text, min_length=min_length, max_length=max_length)

#     output = response[0]["summary_text"]

#     #breakpoint()
#     # ⚠️ fastapi only accepts simple Python data types as a return value
#     # among them dict, list, str, int, float, bool
#     # in order to be able to convert the api response to JSON
#     return output

# #app.state.model = load_document_model()

# @app.get("/document")
# def document(doc: str, question: str, min_length: int = 5, max_length: int = 20):
#     """
#     Gives you answers about input document
#     """

#     app.state.model = load_document_model_text()

#     model = app.state.model
#     assert model is not None

#     qa = {"question": question, "context": doc}

#     response = model(qa)

#     output = response["answer"].capitalize()

#     return output



# @app.get("/document_upload")
# def document_upload(image_path: str, question: str):
#     """
#     Gives you answers about input document
#     """

#     app.state.model = load_document_model()

#     model = app.state.model
#     assert model is not None

#     response = model(image_path, question)

#     output = response[0]["answer"]

#     # ⚠️ fastapi only accepts simple Python data types as a return value
#     # among them dict, list, str, int, float, bool
#     # in order to be able to convert the api response to JSON
#     return output



@app.get("/")
def root():
    return dict(greeting="Hello")




# if __name__=='__main__':
#     summarize("""Endometriosis often causes severe pain in the pelvis, especially during menstrual periods. Some people also have pain during sex or when using the bathroom. Some people have trouble getting pregnant.
# Some people with endometriosis dont have any symptoms. For those who do, a common symptom is pain in the lower part of the belly (pelvis).""")
