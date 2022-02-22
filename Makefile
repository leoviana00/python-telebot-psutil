active_env:
	python3 -m venv .env
	source .env/bin/activate

init:
	pip install -r requirements.txt

run:
	python3 app.py

deactive_env:
	deactivate