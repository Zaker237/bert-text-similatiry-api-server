FROM python:3.9

WORKDIR /code
COPY ./requirements.txt /code/requirements.txt
RUN pip install -r /code/requirements.txt
COPY ./similarity /code

CMD ["uvicorn", "similarity.main:app", "--host", "0.0.0.0", "--port", "8002"]