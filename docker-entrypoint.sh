#!/bin/bash

# Apply database migrations
echo "Apply database migrations"
python manage.py migrate

# Start server
echo "Starting server"

# 开发环境
python manage.py runserver 0.0.0.0:8000

# 生产环境
# gunicorn tzfdapi.wsgi -b 0.0.0.0:8000