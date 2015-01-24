build: test lint

test:
	@bin/test -v -w ./tests

lint:
	@flake8 --config .flake8 .

.PHONY: build
