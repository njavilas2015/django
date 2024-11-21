#!/bin/bash
echo "🔄 Running pre-push hook..."
if ! python manage.py makemigrations --check --dry-run; then
  echo "❌ Hay migraciones pendientes. Por favor, créalas antes de hacer push."
  exit 1
fi
pytest --cov=myapp --cov-report=term-missing
if [ $? -ne 0 ]; then
  echo "❌ Las pruebas fallaron. Por favor, revisa los errores."
  exit 1
fi