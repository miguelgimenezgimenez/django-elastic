FROM python:3.6
ENV PYTHONUNBUFFERED 1

ARG build_env
ENV BUILD_ENV ${build_env}

RUN [ -d /api ] || mkdir /api;
COPY  ./ /api
WORKDIR /api
RUN pip install -r  requirements.txt
RUN  docker-compose run web python manage.py search_index --create