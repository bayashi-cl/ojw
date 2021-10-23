import colorama


def log_blue(msg: str) -> None:
    print(colorama.Fore.BLUE + "OJW" + colorama.Style.RESET_ALL + ": " + msg)


def log_red(msg: str) -> None:
    print(colorama.Fore.RED + "OJW" + colorama.Style.RESET_ALL + ": " + msg)
