.PHONY: help install dev lint type test docker clean

help:
	@echo "install  install the package"
	@echo "dev      install with dev extras"
	@echo "lint     ruff + black + isort checks"
	@echo "type     mypy type check"
	@echo "test     run the test suite"
	@echo "docker   build the container image"
	@echo "clean    remove build and run artifacts"

install:
	pip install .

dev:
	pip install -e ".[dev]"

lint:
	ruff check .
	black --check .
	isort --check-only .

type:
	python -m mypy chronorisk

test:
	pytest

docker:
	docker build -t chronorisk .

clean:
	rm -rf runs build dist *.egg-info .pytest_cache .mypy_cache
	find . -name __pycache__ -type d -prune -exec rm -rf {} +
