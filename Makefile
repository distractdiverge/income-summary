PYTHON = python3

SRC_DIR = .
PY_FILES = $(shell find $(SRC_DIR) -name "*.py")

.PHONY: mypy pylint check clean test help

run:
	$(PYTHON) main.py > output.txt

mypy:
	mypy $(SRC_DIR)

pylint:
	pylint $(SRC_DIR)

test:
	pytest

testcov:
	pytest --cov=. --cov-report html test*.py

check: mypy pylint

clean:
	find . -type f -name "*.pyc" -delete
	find . -type d -name "__pycache__" -exec rm -rf {} +

help:
	@echo "Available commands:"
	@echo "  make run   	- Run the main program to categorize & aggregate data"
	@echo "  make mypy      - Run mypy type checker"
	@echo "  make pylint    - Run pylint linter"
	@echo "  make test    	- Run pytest"
	@echo "  make check     - Run both mypy and pylint"
	@echo "  make clean     - Remove __pycache__ and .pyc files"
