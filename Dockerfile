FROM python:3.10-alpine

ARG IMAGE_USER="user"
ENV PUID=1000 PGID=1000 PUSER=$IMAGE_USER
ENV POETRY_HOME=/etc/poetry PYTHONUNBUFFERED=1

RUN apk add --no-cache  \
    curl \
    build-base \
    openssl-dev \
    libjpeg-turbo-dev \
    libwebp-dev \
    zlib-dev

WORKDIR /var/app

RUN addgroup -S -g $PGID $IMAGE_USER &&  \
    adduser -S -s /bin/sh -G $IMAGE_USER -u $PGID $IMAGE_USER && \
    chown -R $PUID:$PGID /var/app

RUN curl -sSL https://install.python-poetry.org | python -
ENV PATH=$PATH:$POETRY_HOME/bin:/var/app

COPY --chown=$IMAGE_USER:$IMAGE_USER . .

RUN POETRY_VIRTUALENVS_CREATE=false poetry install --no-root
USER $IMAGE_USER

RUN python manage.py migrate
RUN python manage.py runscript -v3 auto_configure
RUN python manage.py collectstatic

CMD [ "python", "./manage.py", "runserver", "0.0.0.0:8000" ]

EXPOSE 8000
