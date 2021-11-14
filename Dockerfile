FROM python:3.8-slim-buster

WORKDIR /fastapi-docker

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
EXPOSE 8000:8000
COPY . . 
CMD [ "uvicorn", "server:app","--host", "127.0.0.1", "--reload"]
# CMD ["uvicorn", "server:app", "--reload"]
