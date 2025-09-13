# Use official Python image
FROM python:3.12-slim

# Set working directory
WORKDIR /app

# Install Poetry
RUN pip install poetry

# Copy Poetry files
COPY pyproject.toml poetry.lock* /app/

# Install dependencies (including yfinance)
RUN poetry install --no-root

# Copy ingestion script
COPY data_ingestion.py .
COPY clickhouse_connection.py .



# Run the script
CMD ["poetry", "run", "python", "data_ingestion.py"]
