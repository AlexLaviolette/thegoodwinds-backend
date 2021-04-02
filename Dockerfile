FROM python:3.8-alpine3.12

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

CMD ["./gunicorn.sh"]