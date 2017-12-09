FROM python:3-alpine
MAINTAINER Duan Hongyi <duanhongyi@doopai.com>

ADD . /app
WORKDIR /app

RUN mkdir -p /var/lib/blog/media && \
    mkdir -p /var/lib/blog/database && \
    pip install -r requirements.txt  -i https://pypi.douban.com/simple --trusted-host pypi.douban.com && \
    python3 /app/manage.py migrate --run-syncdb

EXPOSE 18000
VOLUME ["/var/lib/blog"]
CMD ["gunicorn", "-b", "0.0.0.0:18000", "blog.wsgi:application"]
