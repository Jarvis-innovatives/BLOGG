#!/usr/bin/env bash
set -e

# Run database migrations and collect static files, then start Gunicorn
echo "Running migrations..."
python manage.py migrate --noinput

echo "Collecting static files..."
python manage.py collectstatic --noinput

echo "Starting Gunicorn..."
exec gunicorn portfolio_project.wsgi:application --bind 0.0.0.0:${PORT:-10000} --workers 3
