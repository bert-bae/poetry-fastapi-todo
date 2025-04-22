from cleo.commands.command import Command
from cleo.helpers import argument
import subprocess


class AlembicCommand(Command):
    """
    Run Alembic commands through Poetry.

    alembic
        {args* : Arguments to pass to the Alembic CLI.}
    """

    def handle(self):
        args = self.argument("args")
        try:
            subprocess.run(["alembic", *args], check=True)
            return 0  # Indicate success
        except subprocess.CalledProcessError as e:
            self.line_error(f"<error>Error: {e}</error>")
            return 1  # Indicate failure


def factory():
    return AlembicCommand()
