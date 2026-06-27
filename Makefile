.PHONY: help install-backend install-frontend backend-lint backend-format-check backend-typecheck backend-test backend-check frontend-lint frontend-typecheck frontend-check frontend-build check test build

help:
	@echo "Available targets:"
	@echo "  install-backend       Install backend dev dependencies"
	@echo "  install-frontend      Install frontend dependencies"
	@echo "  backend-check         Run backend lint, format check, typecheck, and tests"
	@echo "  frontend-check        Run frontend lint and typecheck"
	@echo "  check                 Run backend and frontend checks"
	@echo "  test                  Run backend tests"
	@echo "  build                 Build frontend"

install-backend:
	cd backend && uv sync --extra dev

install-frontend:
	cd frontend && npm install

backend-lint:
	cd backend && uv run ruff check .

backend-format-check:
	cd backend && uv run ruff format --check .

backend-typecheck:
	cd backend && uv run pyright

backend-test:
	cd backend && uv run pytest

backend-check: backend-lint backend-format-check backend-typecheck backend-test

frontend-lint:
	cd frontend && npm run lint

frontend-typecheck:
	cd frontend && npm run typecheck

frontend-check:
	cd frontend && npm run check

frontend-build:
	cd frontend && npm run build

check: backend-check frontend-check

test: backend-test

build: frontend-build
