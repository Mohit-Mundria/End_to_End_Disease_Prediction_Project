FROM python:3.9.18
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
EXPOSE 5000
CMD gunicorn --timeout 120 --workers=4 --bind 0.0.0.0:5000 app:app