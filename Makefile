```makefile
###############################################################################
# FIFA Player Analytics
# Makefile
###############################################################################

.DEFAULT_GOAL := help

PYTHON := python3
PIP := pip
VENV := .venv
SRC := src
TESTS := tests
NOTEBOOKS := notebooks

###############################################################################
# Help
###############################################################################

.PHONY: help

help:
	@echo ""
	@echo "=============================================================="
	@echo " FIFA Player Analytics - Available Commands"
	@echo "=============================================================="
	@echo ""
	@echo "Environment"
	@echo "  make venv           Create virtual environment"
	@echo "  make install        Install project dependencies"
	@echo "  make dev            Install development dependencies"
	@echo ""
	@echo "Jupyter"
	@echo "  make lab            Launch JupyterLab"
	@echo "  make notebook       Launch Jupyter Notebook"
	@echo ""
	@echo "Formatting & Quality"
	@echo "  make format         Format code using Black and Ruff"
	@echo "  make lint           Run Ruff lint checks"
	@echo "  make typecheck      Run MyPy"
	@echo "  make check          Run format, lint, typecheck and tests"
	@echo ""
	@echo "Testing"
	@echo "  make test           Run pytest"
	@echo "  make coverage       Run pytest with coverage"
	@echo ""
	@echo "Cleaning"
	@echo "  make clean          Remove caches and temporary files"
	@echo ""
	@echo "Packaging"
	@echo "  make freeze         Export installed packages"
	@echo ""

###############################################################################
# Environment
###############################################################################

.PHONY: venv

venv:
	$(PYTHON) -m venv $(VENV)

.PHONY: install

install:
	$(PIP) install --upgrade pip
	$(PIP) install -r requirements.txt

.PHONY: dev

dev: install
	$(PIP) install -e ".[dev]"

###############################################################################
# Notebook
###############################################################################

.PHONY: lab

lab:
	jupyter lab

.PHONY: notebook

notebook:
	jupyter notebook

###############################################################################
# Formatting
###############################################################################

.PHONY: format

format:
	black $(SRC)
	ruff check $(SRC) --fix

###############################################################################
# Linting
###############################################################################

.PHONY: lint

lint:
	ruff check $(SRC)

###############################################################################
# Type Checking
###############################################################################

.PHONY: typecheck

typecheck:
	mypy $(SRC)

###############################################################################
# Testing
###############################################################################

.PHONY: test

test:
	pytest

.PHONY: coverage

coverage:
	pytest --cov=$(SRC) --cov-report=term-missing

###############################################################################
# Combined Checks
###############################################################################

.PHONY: check

check: format lint typecheck test

###############################################################################
# Export Requirements
###############################################################################

.PHONY: freeze

freeze:
	pip freeze > requirements-lock.txt

###############################################################################
# Clean
###############################################################################

.PHONY: clean

clean:
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type d -name ".pytest_cache" -exec rm -rf {} +
	find . -type d -name ".ruff_cache" -exec rm -rf {} +
	find . -type d -name ".mypy_cache" -exec rm -rf {} +
	find . -type d -name ".ipynb_checkpoints" -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
	find . -type f -name "*.pyo" -delete
	find . -type f -name "*.coverage" -delete
	rm -rf htmlcov
	rm -rf build
	rm -rf dist
	rm -rf .coverage

###############################################################################
# End of File
###############################################################################
```