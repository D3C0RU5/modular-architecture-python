.PHONY: help setup install-dev install-prod compile upgrade lint format typecheck check run docker-build docker-up docker-down clean migrate-create migrate-upgrade debug

# ----------------------------
# Config
# ----------------------------

VENV := .venv
PYTHON := $(VENV)/bin/python
PIP := $(VENV)/bin/pip
PIP_COMPILE := $(VENV)/bin/pip-compile
export PYTHONPATH := $(PYTHONPATH):/app/app/module

# ----------------------------
# Virtual environment (Create only if not exists)
# ----------------------------

$(VENV)/bin/python:
	python3 -m venv $(VENV)
	$(PIP) install --upgrade pip pip-tools

# ----------------------------
# Help
# ----------------------------

help:
	@echo "setup               Create venv and install dev dependencies"
	@echo "compile             Compile requirements"
	@echo "upgrade             Upgrade dependencies"
	@echo "run                 Run FastAPI"
	@echo "check               Run format + lint + typecheck"
	@echo "migrate-create      Create migration for a module (MODULE=<name>)"
	@echo "migrate-upgrade     Apply migrations for a module (MODULE=<name>)"

# ----------------------------
# Setup
# ----------------------------

setup: $(VENV)/bin/python install-dev

install-dev: $(VENV)/bin/python
	$(PIP) install -r requirements-dev.txt

install-prod: $(VENV)/bin/python
	$(PIP) install -r requirements.txt

# ----------------------------
# Dependencies
# ----------------------------

compile: $(VENV)/bin/python
	$(PIP_COMPILE) -o requirements.txt requirements.in
	$(PIP_COMPILE) -o requirements-dev.txt requirements-dev.in

upgrade: $(VENV)/bin/python
	$(PIP_COMPILE) --upgrade requirements.in
	$(PIP_COMPILE) --upgrade requirements-dev.in

# ----------------------------
# Code Quality
# ----------------------------

lint: $(VENV)/bin/python
	$(PYTHON) -m ruff check .

format: $(VENV)/bin/python
	$(PYTHON) -m black .

typecheck: $(VENV)/bin/python
	$(PYTHON) -m pyright

check: format lint typecheck

# ----------------------------
# Application
# ----------------------------

debug: $(VENV)/bin/python
	$(PYTHON) -m debugpy --listen 0.0.0.0:5678 -m uvicorn app.main:app --host 0.0.0.0 --port 3000 --reload

run: $(VENV)/bin/python
	$(PYTHON) -m uvicorn app.main:app --host 0.0.0.0 --port 3001 --reload

# ----------------------------
# Docker
# ----------------------------

docker-build:
	docker compose build

docker-up:
	docker compose up

docker-down:
	docker compose down

# ----------------------------
# Cleanup
# ----------------------------

clean:
	find . -type d -name "__pycache__" -exec rm -r {} +
	find . -type d -name ".pytest_cache" -exec rm -r {} +

# ----------------------------
# Migrations (by module)
# ----------------------------

migrate-create:
ifndef MODULE
	$(error MODULE not defined. Ex: make migrate-create MODULE=template)
endif
	@echo "Creating migration for module $(MODULE)..."
	@export PYTHONPATH=$$PYTHONPATH:/app/app/module && \
	alembic -c app/module/$(MODULE)/infra/db/alembic/alembic.ini revision --autogenerate -m "autogenerate $(MODULE) tables"

migrate-upgrade:
ifndef MODULE
	$(error MODULE not defined. Ex: make migrate-upgrade MODULE=template)
endif
	@echo "Applying migrations for module $(MODULE)..."
	@export PYTHONPATH=$$PYTHONPATH:/app/app/module && \
	alembic -c app/module/$(MODULE)/infra/db/alembic/alembic.ini upgrade head

migrate-downgrade:
ifndef MODULE
	$(error MODULE not defined. Ex: make migrate-downgrade MODULE=template)
endif
ifndef REV
	$(error REV not defined. Ex: make migrate-downgrade MODULE=template REV=-1)
endif
	@echo "Reverting migrations for module $(MODULE) to revision $(REV)..."
	@export PYTHONPATH=$$PYTHONPATH:/app/app/module && \
	alembic -c app/module/$(MODULE)/infra/db/alembic/alembic.ini downgrade $(REV)

test:
	$(PYTHON) -m pytest