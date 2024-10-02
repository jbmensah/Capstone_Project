VENV = venv
PYTHON = $(VENV)/bin/python
MANAGE = $(PYTHON) manage.py

# Migrations
migrate:
	$(MANAGE) makemigrations
	$(MANAGE) migrate

# Start the server
server:
	$(MANAGE) runserver

# Run tests
test:
	$(MANAGE) test

# Format code with black
format:
	$(VENV)/bin/black .

# Start interactive shell
shell:
	$(MANAGE) shell -i ipython

# Create superuser
superuser:
	$(MANAGE) createsuperuser
