build: test lint

test:
	@bin/test -v -w ./tests

lint:
	@flake8 --config .flake8 .

release:
	python setup.py register
	python setup.py bdist_egg upload
	python setup.py bdist_wininst upload
	python setup.py sdist upload

.PHONY: build
