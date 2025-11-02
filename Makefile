.PHONY: test run
test:
	PYTHONPATH=./src pytest -s -W ignore::DeprecationWarning
run:
	python ./src/draughts/main.py
