FROM python:3.7-slim

WORKDIR /app

COPY app.py requirements.txt ./

RUN pip install -r requirements.txt

CMD ["sh", "-c", "python app.py"]