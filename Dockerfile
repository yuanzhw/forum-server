FROM python:3.7

WORKDIR /app

COPY . .

RUN pip3 install -e .

EXPOSE 2000

CMD ["gunicorn","wsgi","-w 4","--bind","0.0.0.0:2000"]