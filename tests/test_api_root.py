import unittest
import requests
import time

class TestApiRoot(unittest.TestCase):
    def test_api_root(self):
        # testin the api root

        time.sleep(15)

        url = "http://localhost:8000/"

        result = requests.get(url).json()

        self.assertEqual(result["greeting"], "Hello")
