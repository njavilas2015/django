VENV=../venv
PYTHON=python
PIP=$(VENV)/bin/pip

install:
	$(PIP) install -r requirements.txt
	$(PIP) install --upgrade pip

superuser:
	$(PYTHON) manage.py createsuperuser --noinput

run: migrate
	$(PYTHON) manage.py runserver

migrate:
	$(PYTHON) manage.py makemigrations
	$(PYTHON) manage.py migrate

test:
	$(PYTHON) manage.py test

lint:
	$(VENV)/bin/pylint

"import-sql":
	export PGPASSWORD=${DB_PASSWORD}

	pg_dump -U ${DB_USERNAME} -h ${DB_HOST} -p ${DB_PORT} ${DB_NAME} < db.sql

"export-sql":
	export PGPASSWORD=${DB_PASSWORD}

	pg_dump -U ${DB_USERNAME} -h ${DB_HOST} -p ${DB_PORT} ${DB_NAME} > db.sql

inject:
	wget https://drive.google.com/file/d/<hash>/view?usp=drive_link

	pv "${DIR_DB}" | <>

clean:
	find . -name '__pycache__' -exec rm -rf {} +
	find . -name '*.pyc' -delete

shell:
	$(PYTHON) manage.py shell

push:
	git add .
	git commit -m "auto update"
	git push origin main

build:
	docker build -t app:local .

drop: clean
	find . -path "*/migrations/*.py" -not -name "__init__.py" -delete
	python manage.py flush --no-input


env:
	echo "NATS_URL=nats://natsio.onbbu.ar:4220" > .env
	echo "" >> .env
	echo "DB_HOST=" >> .env
	echo "DB_PORT=" >> .env
	echo "DB_USERNAME=" >> .env
	echo "DB_PASSWORD=" >> .env
	echo "DB_NAME=" >> .env
	echo "" >> .env
	echo "SUPERUSER_USERNAME=admin" >> .env
	echo "SUPERUSER_EMAIL=admin@ejemplo.com" >> .env
	echo "SUPERUSER_PASSWORD=admin_password" >> .env
	echo "" >> .env
	echo "EMAIL_BACKEND='django.core.mail.backends.smtp.EmailBackend'" >> .env
	echo "EMAIL_HOST='smtp.gmail.com'" >> .env
	echo "EMAIL_PORT=587" >> .env
	echo "EMAIL_USE_TLS=True" >> .env
	echo "EMAIL_HOST_USER='tu_email@gmail.com'" >> .env
	echo "EMAIL_HOST_PASSWORD='tu_contraseña'" >> .env
	echo "DEFAULT_FROM_EMAIL='tu_email@gmail.com'" >> .env
