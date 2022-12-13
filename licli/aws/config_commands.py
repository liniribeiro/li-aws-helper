import typer

from aws.config import AWSConfig
from exceptions import handle_exception

aws_app = typer.Typer()


@aws_app.command()
@handle_exception
def config():
    region_name = typer.prompt("Region", default='us-east-1', show_default=True)
    access_key = typer.prompt("Access Key")
    secret_key = typer.prompt("Secret Key")
    mfa_arn = typer.prompt("IAM ARN")

    AWSConfig().configure(region_name, access_key, secret_key, mfa_arn)
    message = typer.style("All Done!", fg=typer.colors.GREEN, bold=True)
    typer.echo(message)
