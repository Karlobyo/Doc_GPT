import unittest
from doc_gpt.dl_logic.registry import load_summary_model

class TestMod(unittest.TestCase):

    def test_mod(self):
        # checking that the model is loaded
        model = load_summary_model()
        self.assertIsNotNone(model)
