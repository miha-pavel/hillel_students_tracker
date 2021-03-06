run:
	./manage.py runserver

test:
	./manage.py test --keepdb

pep8:
	flake8

sh_p:
	./manage.py shell_plus

migrate:
	./manage.py migrate

celery:
	celery -A students_tracker worker -l info

celery_beat:
	celery -A students_tracker beat -l info

rabbit:
	rabbitmq-server
