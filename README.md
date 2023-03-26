### Text Similarity API

this repository contains a small web server with an API to calculate the similarity between a text and a list of texts. The server is build using [FastApi](https://fastapi.tiangolo.com/) and [sentence-transformers librairie](https://huggingface.co/sentence-transformers) from [huggingface](https://huggingface.co).

**NB**: The Languages of the text should be English.

I build this to integrate it the [This](https://github.com/Zaker237/Learn-Next-Similarity-Api-Service) project.

#### REQUIREMENTS

- python >=3.6
- docker

#### How to run ?

Create a venv folder:
```console
$ python3 -m venv venv
```

Activate the venv:
```console
$ source venv/bin/activate
```

Install requirements:
```console
$ pip install -r requirements.txt
```

Run the server:
```console
$ uvicorn similarity.main:app --reload --host 0.0.0.0 --port 8002
```

The server shoul start on the port 8002 and the api documentation should available [Hier](http://localhost:8002/docs).

Don't forget to deactivate the venv when you're done:
```console
$ deactivate
```