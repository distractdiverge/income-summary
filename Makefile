PYTHON = python3

SRC_DIR = .
PY_FILES = $(shell find $(SRC_DIR) -name "*.py")

.PHONY: mypy pylint check clean help

mypy:
	mypy $(SRC_DIR)

pylint:
	pylint $(SRC_DIR)

check: mypy pylint

clean:
	find . -type f -name "*.pyc" -delete
	find . -type d -name "__pycache__" -exec rm -rf {} +

help:
	@echo "Available commands:"
	@echo "  make install   - Install dependencies (mypy, pylint)"
	@echo "  make mypy      - Run mypy type checker"
	@echo "  make pylint    - Run pylint linter"
	@echo "  make check     - Run both mypy and pylint"
	@echo "  make clean     - Remove __pycache__ and .pyc files"
