FROM python:3.10
RUN  mkdir /code
WORKDIR /code
COPY ./requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
COPY ./core /code/core
COPY . .
CMD ["uvicorn", "core.main:app", "--host", "0.0.0.0", "--port", "80"]

