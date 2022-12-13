

import typer

from aws.config_commands import aws_app
from aws.secret_token.sts_commands import sts_app

app = typer.Typer()
app.add_typer(aws_app, name="aws")
aws_app.add_typer(sts_app, name="auth")


if __name__ == "__main__":
    app()
