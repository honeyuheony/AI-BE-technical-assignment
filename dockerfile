# with poetry
FROM python:3.13-alpine

WORKDIR /app

COPY pyproject.toml poetry.lock ./

RUN poetry install

COPY ./app /code/app
 
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
