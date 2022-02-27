VENV = venv
PYTHON = ${VENV}/bin/python3
PIP = ${VENV}/bin/pip3


.PHONY: help venv install flake8 isort black runserver makemigrations migrate shell_plus createsuperuser flush_db reset_db

venv:
	python3 -m venv venv

install: venv requirements/base.txt requirements/dev.txt requirements/lint.txt
	${PIP} install -r requirements/base.txt -r requirements/dev.txt -r requirements/lint.txt

makemigrations: install
	${PYTHON} manage.py makemigrations

migrate: install
	${PYTHON} manage.py migrate

createsuperuser: migrate
	${PYTHON} manage.py createsuperuser --email admin@example.com --username admin

runserver: createsuperuser
	${PYTHON} manage.py runserver

test: install
	${PYTHON} -m pytest caffe

format: install
	${PYTHON} -m black .

lint: install
	${PYTHON} -m flake8 caffe/.

isort: install
	${PYTHON} -m isort .

shell_plus: install
	${PYTHON} manage.py shell_plus

reset_db: install
	${PYTHON} manage.py reset_db

flush_db: install
	${PYTHON} manage.py flush --database=default --noinput
