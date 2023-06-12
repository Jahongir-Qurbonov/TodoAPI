FROM python:3.11-slim

ENV PYTHONUNBUFFERED=1

RUN pip install poetry

WORKDIR /code
COPY poetry.lock pyproject.toml /code/

# Project initialization:
RUN poetry install

# Creating folders, and files for a project:
COPY . /code

RUN poetry run python manage.py migrate
RUN poetry run python manage.py runscript -v3 auto_configure
RUN poetry run python manage.py collectstatic

CMD [ "poetry", "run", "python", "./manage.py", "runserver", "0.0.0.0:8000" ]

EXPOSE 8000
