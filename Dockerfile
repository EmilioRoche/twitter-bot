FROM python:3.7-alpine

WORKDIR /bot_app

COPY src /bot_app/src
COPY requirements.txt /bot_app

RUN pip3 install -r /bot_app/requirements.txt

CMD ["python3", "src/main.py"]