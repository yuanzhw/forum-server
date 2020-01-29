FROM python:3.7

WORKDIR /app

RUN git clone https://github.com/yuanzhw/forum-server.git

RUN pip3 install -e .

EXPOSE 2000

CMD ["gunicorn","wsgi","-w 4","--bind","0.0.0.0:2000"]