from setuptools import setup
from setuptools import find_packages

with open("requirements_test.txt") as f:
    content = f.readlines()

requirements = [x.strip() for x in content]


setup(name="doc_gpt",
      description="chatbot for document assistance",
      packages=find_packages(),
      install_requires=requirements)
