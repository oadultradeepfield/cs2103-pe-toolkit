PY := python3
PIP := $(PY) -m pip
REQ := requirements.txt

.PHONY: help install lint format typecheck check clean

help:
	@echo "Usage:"
	@echo "  make install     Install dependencies"
	@echo "  make lint        Run ruff lint"
	@echo "  make format      Run ruff format --check"
	@echo "  make typecheck   Run mypy"
	@echo "  make check       Run all checks"
	@echo "  make clean       Remove compiled artifacts"

install:
	$(PIP) install --upgrade pip
	@if [ -f $(REQ) ]; then \
		$(PIP) install -r $(REQ); \
	else \
		echo "No $(REQ) found, skipping"; \
	fi

lint:
	ruff check .

format:
	ruff format --check .

typecheck:
	mypy .

check: install lint format typecheck

clean:
	@find . -type f -name "*.py[co]" -delete || true
	@find . -type d -name "__pycache__" -exec rm -rf {} + || true
