.PHONY: test run
test:
	PYTHONPATH=./src pytest -W ignore::DeprecationWarning
run:
	python ./src/draughts/main.py
