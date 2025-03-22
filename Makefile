PYTHON = python3

SRC_DIR = .
TEST_DIR = tests
TEST_FILES = $(TEST_DIR)/test*.py
PY_FILES = $(shell find $(SRC_DIR) -name "*.py")

.PHONY: run mypy lint check clean test testcov help

mypy:
	uv run mypy $(SRC_DIR)

lint:
	uv run pylint --ignore=.venv\
	 $(SRC_DIR) $(TEST_DIR) 

test:
	uv run pytest $(TEST_FILES)

testcov:
	uv run pytest --cov=$(SRC_DIR) --cov-report xml $(TEST_FILES)

htmltestcov:
	uv run pytest --cov=$(SRC_DIR) --cov-report html $(TEST_FILES)

check: mypy pylint

clean:
	find . -type f -name "*.pyc" -delete
	find . -type d -name "__pycache__" -exec rm -rf {} +

help:
	@echo "Available commands:"
	@echo "  make run   	- Run the main program to categorize & aggregate data"
	@echo "  make mypy      - Run mypy type checker"
	@echo "  make lint      - Run pylint linter"
	@echo "  make test    	- Run pytest"
	@echo "  make testcov   - Run pytest with test coverage"
	@echo "  make check     - Run both mypy and pylint"
	@echo "  make clean     - Remove __pycache__ and .pyc files"
