.DEFAULT_GOAL := help 

.PHONY: help
help:  ## Show this help.
	@grep -E '^\S+:.*?## .*$$' $(firstword $(MAKEFILE_LIST)) | \
		awk 'BEGIN {FS = ":.*?## "}; {printf "%-30s %s\n", $$1, $$2}'

.PHONY: slow-test
slow-test: ## Run slow tests.
	PYTHONPATH=. uv run pytest -x -ra tests/

.PHONY: fast-test
fast-test: ## Run fast tests.
	PYTHONPATH=. PROFILE=test uv run pytest -x -ra tests/
