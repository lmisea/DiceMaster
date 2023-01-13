import os


def clear_terminal() -> None:
    """Clears the terminal."""
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")


starting: bool = False
display_instructions: bool = False
