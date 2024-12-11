FROM python:3.13

RUN apt-get update && apt-get install -y --no-install-recommends curl ca-certificates

ADD https://astral.sh/uv/install.sh /uv-installer.sh

RUN sh /uv-installer.sh && rm /uv-installer.sh

ENV PATH="/root/.local/bin/:$PATH"

ADD . /app

WORKDIR /app
RUN uv sync --frozen

RUN uv run python manage.py migrate
RUN uv run python manage.py runscript -v3 auto_configure
RUN uv run python manage.py collectstatic

CMD [ "python", "./manage.py", "runserver", "0.0.0.0:8000" ]

EXPOSE 8000
