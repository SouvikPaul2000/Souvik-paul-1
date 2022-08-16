FROM python:3.8

COPY . .
RUN  pip install -r requirement.txt

CMD gunicorn --bind 0.0.0.0:5000 wsgi:app
