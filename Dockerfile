FROM python:3.6
ENV PYTHONUNBUFFERED 1

ARG build_env
ENV BUILD_ENV ${build_env}

RUN [ -d /bmatProject ] || mkdir /bmatProject;
COPY  ./ /bmatProject
WORKDIR /bmatProject
RUN pip install -r  requirements.txt
