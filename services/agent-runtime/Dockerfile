FROM python:3.11-slim
WORKDIR /app
COPY pyproject.toml poetry.lock* /app/
RUN pip install poetry && poetry config virtualenvs.create false && poetry install --no-root --no-interaction --no-ansi
COPY src /app/src
ENV PYTHONPATH=/app
CMD ["python", "-c", "from src.app import run; print(run())"]
