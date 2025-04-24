.DEFAULT_GOAL := help 

.PHONY: help
help:  ## Show this help.
	@grep -E '^\S+:.*?## .*$$' $(firstword $(MAKEFILE_LIST)) | \
		awk 'BEGIN {FS = ":.*?## "}; {printf "%-30s %s\n", $$1, $$2}'

pre-requirements:
	@scripts/pre-requirements.sh

.PHONY: local-setup
local-setup: pre-requirements ## Install hooks and packages
	scripts/local-setup.sh


.PHONY: install
install: build ## Install the app packages
	uv python install 3.12.8
	uv python pin 3.12.8
	uv sync

.PHONY: update
update: ## Updates the app packages
	uv lock --upgrade

.PHONY: add-package
add-package: ## Installs a new package in the app. ex: make add-package package=XXX
	uv add $(package)
	make build

.PHONY: check-typing
check-typing:  ## Run a static analyzer over the code to find issues
	uv run mypy .

.PHONY: check-lint
check-lint: ## Checks the code style
	uv run ruff check --fix

.PHONY: lint
lint: ## Lints the code format
	uv run ruff check --fix

.PHONY: check-format
check-format:  ## Check format python code
	uv run ruff format --check

.PHONY: format
format:  ## Format python code
	uv run ruff format

.PHONY: slow-test
slow-test: ## Run slow tests.
	PYTHONPATH=. uv run pytest -x -ra tests/

.PHONY: fast-test
fast-test: ## Run fast tests.
	PYTHONPATH=. PROFILE=test uv run pytest -x -ra tests/

.PHONY: pre-commit
pre-commit: check-typing check-format fast-test
