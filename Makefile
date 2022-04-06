.PHONY: check-typing format-code prepare-env

# Checks typing
check-typing:
	mypy --install-types --ignore-missing-imports .

# Check and formats code syntax with flake8 and black
format-code:
	flake8 --exclude=.venv --max-line-length=120 .
	black .

# Removes the existing virtualenv, creates a new one, install dependencies.
prepare-env:
	rm -rf .venv
	python3.8 -m venv .venv
	.venv/bin/pip install -r requirements.txt
