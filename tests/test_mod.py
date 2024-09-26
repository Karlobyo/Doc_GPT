import unittest
from doc_gpt.dl_logic.registry import load_summary_model, load_document_model, load_document_model_text

class TestMod(unittest.TestCase):

    def test_mod(self):
        # checking that the model is loaded
        model_sum = load_summary_model()
        model_doc = load_document_model()
        model_txt = load_document_model_text()
        self.assertIsNotNone(model_sum)
        self.assertIsNotNone(model_doc)
        self.assertIsNotNone(model_txt)
