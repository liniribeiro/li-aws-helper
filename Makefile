
aws-configure:
	python3 licli/main.py li config

aws-refresh:
	python3 li_aws_helper/main.py  refresh --token xxxx



poetry-build-min-version:
	poetry version minor && poetry build

poetry-deploy-package:
	poetry publish