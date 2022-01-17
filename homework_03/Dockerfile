# to run use:
# cd homework_03
# docker build --progress=plain . -t blog-app
# cd blog
# docker run --expose=8000 -p 8000:8000 blog-app

FROM python:3.9-buster

WORKDIR /var/app

RUN pip install poetry==1.1.12

COPY blog/pyproject.toml blog/poetry.lock ./

RUN poetry config virtualenvs.create false

RUN poetry install

COPY blog .

CMD uvicorn app:app --host=0.0.0.0 --port=8000
