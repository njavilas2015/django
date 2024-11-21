#!/bin/bash
echo "🔄 Running pre-commit hook..."
black .
isort .
flake8 .
python manage.py check