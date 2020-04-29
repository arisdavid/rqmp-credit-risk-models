build:
	docker build -t credit-models:latest .

dev-configure:
	pip3 install -r dev-requirements.txt
	pip3 install -r requirements.txt
	pre-commit install
