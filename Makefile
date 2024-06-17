.PHONY: install test run api-test

install:
	@echo "Installing dependencies..."
	pip install -r requirements.txt

test:
	@echo "Running unit tests..."
	python -m unittest discover

run:
	@echo "Running application..."
	python app.py

api-test:
	@echo "Running API tests..."
	python plik.py
