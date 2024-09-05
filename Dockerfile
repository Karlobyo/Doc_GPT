FROM python:3.10.6-buster

#WORKDIR /prod

# RUN apt-get update && apt-get install -y \
# libhdf5-dev \
# && rm -rf /var/lib/apt/lists/*


# We strip the requirements from useless packages like `ipykernel`, `matplotlib` etc...
COPY requirements_prod.txt requirements.txt
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY doc_gpt doc_gpt
COPY setup.py setup.py
RUN pip install .

#COPY Makefile Makefile
#RUN make reset_local_files

CMD uvicorn doc_gpt.api.fast:app --host 0.0.0.0 --port $PORT


# wo tensorflow and torch, with squeezed requirements
# smaller GAR MEMORY the docker image went from 12 to 1 GB
