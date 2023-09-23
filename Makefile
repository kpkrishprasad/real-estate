SHELL=bash

run:
	source venv/bin/activate; \
		python manage.py runserver
	
setup: 
	python3 -m venv venv
	source venv/bin/activate; \
		pip install -r requirements.txt; \

migrate:
	source venv/bin/activate; \
		python manage.py makemigrations; \
		python manage.py migrate


clean:
	rm -rf venv
	 	
freeze:
	source venv/bin/activate; \
		pip freeze > requirements.txt



