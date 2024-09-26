import unittest
from doc_gpt.api.fast import load_summary_model

class TestEx(unittest.TestCase):
    def test_ex(self):
        # just a dummy test
        self.assertEqual(1, 1)


    def model_exist(self):
        # checking that the model is loaded
        model = load_summary_model()
        self.assertIsNotNone(model)
