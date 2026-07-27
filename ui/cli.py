from rich.console import Console

console = Console()


def user():

    return console.input("[cyan]You > [/]")


def ai(text):

    console.print(f"[green]Rocky > {text}[/]")