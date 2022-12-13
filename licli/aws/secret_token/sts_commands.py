
import typer

from aws.secret_token.sts_client import refresh_token
from exceptions import handle_exception

sts_app = typer.Typer()


@sts_app.command()
@handle_exception
def refresh(code: str = typer.Option("", help="Token code")):
    refresh_token(code)
    message = typer.style("Tokens refreshed", fg=typer.colors.GREEN, bold=True)
    typer.echo(message)