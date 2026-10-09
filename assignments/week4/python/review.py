import os
import subprocess
import click


def create_greeting(name: str, repeat: int) -> str:
    """Create a repeated greeting message."""
    message = f"Hello, {name}! Python command-line arguments are working."
    return "\n".join([message] * repeat)


@click.group()
def cli():
    """Week 4 Python review commands."""
    pass


@cli.command()
@click.option("--name", required=True, help="Name to include in the greeting.")
@click.option(
    "--repeat",
    default=1,
    type=int,
    show_default=True,
    help="Number of times to display the greeting.",
)
def greet(name, repeat):
    """Demonstrate functions and command-line arguments."""
    print(create_greeting(name, repeat))


@cli.command("os-system")
def os_system_command():
    """Run a shell command using os.system()."""
    print("Running 'ls' with os.system():")
    os.system("ls")


@cli.command("subprocess")
def subprocess_command():
    """Run shell commands using subprocess.run()."""
    print("Current directory:")
    result = subprocess.run(
        ["pwd"],
        capture_output=True,
        text=True,
        check=True,
    )
    print(result.stdout.strip())

    print("\nSystem information:")
    subprocess.run(["uname", "-a"], check=True)


if __name__ == "__main__":
    cli()
