FROM python:3.10.14-slim

WORKDIR /app

# Install system dependencies for PostgreSQL
RUN apt-get update && apt-get install -y \
    libpq-dev \
    gcc \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Collect static files (Whitenoise handles serving them)
RUN python manage.py collectstatic --noinput || true

CMD ["gunicorn", "cheese_beer.wsgi:application", "--bind", "0.0.0.0:8000"]