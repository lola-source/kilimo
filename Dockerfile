FROM python:3.9-alpine3.13
LABEL maintaine='lola-source'

RUN apk add --no-cache \
    bash \
    busybox-static

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV PATH="/py/bin:/usr/local/bin:/usr/bin:/bin:$PATH"

COPY ./requirements.txt /tmp/requirements.txt
COPY ./requirements.dev.txt /tmp/requirements.dev.txt
COPY ./backnd /backnd
WORKDIR /backnd
EXPOSE 8000

ARG DEV=false

RUN python -m venv /py && \
    /py/bin/pip install --upgrade pip && \
    /py/bin/pip install -r /tmp/requirements.txt && \
    if [ "$DEV" = "true" ] ; then \
    /py/bin/pip install -r /tmp/requirements.dev.txt ; \
    fi && \    
    rm -rf /tmp && \
    adduser \
        --disabled-password \
        --no-create-home \
        django-user

ENV PATH='/py/bin:$PATH'

USER django-user

SHELL ["/bin/bash", "-c"]

