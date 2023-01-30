
run.local:
	python src/manage.py runserver 0.0.0.0:8000 --settings=config.settings.local

run.migration:
	python src/manage.py makemigrations && python src/manage.py migrate

