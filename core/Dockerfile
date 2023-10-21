FROM python:3.11-buster
RUN  mkdir /code
WORKDIR /code

RUN apt-get update && \
    apt install -y python3-dev

RUN pip install --upgrade pip
RUN pip install poetry
ADD pyproject.toml .
RUN poetry config virtualenvs.create false
RUN poetry install --no-root --no-interaction --no-ansi

EXPOSE 8000

COPY . .

#CMD ["uvicorn", "core.main:app", "--host", "0.0.0.0", "--port", "80"]

