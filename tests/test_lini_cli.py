from typer.testing import CliRunner

from main import app

runner = CliRunner()


def test_refresh():
    args = ["aws", "auth", "refresh", "--code", "111111"]

    result = runner.invoke(app, args)
    assert result.exit_code == 0
