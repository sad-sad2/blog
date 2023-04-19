FROM python:latest

COPY ./requirements.txt ./requirements.txt

RUN pip install -r requirements.txt

ENV ENV='DEV'
ENV SECRET_KEY='django-insecure-y^s(e-s_)uk*_kqi2&&yrb^z@nsrx3!dn^p2yg21l5-=8gnwdm'

COPY . . 

CMD ["gunicorn", "core.wsgi:application",  "--bind", "0.0.0.0:8000"]