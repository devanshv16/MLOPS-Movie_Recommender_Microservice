install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

lint:
	pylint --disable=R,C .

format:
	black .

test:
	python -m pytest -vv -cov=src tests/*.py

all: install lint format test
