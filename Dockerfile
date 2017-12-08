FROM python:3-alpine
MAINTAINER Duan Hongyi <duanhongyi@doopai.com>

ADD . /app
WORKDIR /app

RUN mkdir -p /var/lib/blog && \
    pip install -r requirements.txt  -i https://pypi.douban.com/simple --trusted-host pypi.douban.com && \
    python3 /app/manage.py migrate --run-syncdb

CMD ["gunicorn", "-b", "0.0.0.0:17000", "blog.wsgi:application"]
