from rich.console import Console
console = Console()

def banner() -> str:
    " Prints Pinkerton's banner "

    console.print("""[bold yellow]
Pinkerton 1.7
Investigating JavaScript files since 1850
by 000pp
""")