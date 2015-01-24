test:
	@bin/test -v -w ./tests
	@flake8 --config .flake8 .
