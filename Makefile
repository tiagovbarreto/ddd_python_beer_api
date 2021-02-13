.ONESHELL:

.PHONY: clean install tests run all

clean:
	find . -type f -name '*.pyc' -delete
	find . -type f -name '*.log' -delete

install:
	virtualenv venv; \
	. venv/bin/activate; \
	pip install -r requirements.txt;

test_unit:
	. venv/bin/activate; \
	python manage.py test_unit

test_integration:
	. venv/bin/activate; \
	python manage.py test_integration

run:
	. venv/bin/activate; \
	python manage.py run

all: clean install tests run