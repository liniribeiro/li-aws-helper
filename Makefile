
aws-configure:
	python3 licli/main.py aws config

aws-refresh:
	python3 licli/main.py aws auth refresh --code 079334


poetry-build-min-version:
	poetry version minor && poetry build

poetry-deploy-package:
	poetry publish