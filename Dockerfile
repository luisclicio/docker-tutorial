FROM python:3-alpine

WORKDIR /app

ENV FLASK_APP=src/app.py
ENV FLASK_RUN_HOST=0.0.0.0

# RUN pip install --upgrade pip
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

EXPOSE 5000

COPY . .

CMD [ "flask", "run"]
