import logging

import colorama
from colorlog import ColoredFormatter


def log_blue(msg: str) -> None:
    print(colorama.Fore.BLUE + "OJW" + colorama.Style.RESET_ALL + ": " + msg)


def log_red(msg: str) -> None:
    print(colorama.Fore.RED + "OJW" + colorama.Style.RESET_ALL + ": " + msg)


def setup_logger(verbose: bool) -> None:
    formatter = ColoredFormatter(
        "%(log_color)s%(levelname)-8s%(reset)s %(message)s",
        datefmt=None,
        reset=True,
        log_colors={
            "DEBUG": "cyan",
            "INFO": "green",
            "WARNING": "yellow",
            "ERROR": "red",
            "CRITICAL": "red",
        },
    )
    handler = logging.StreamHandler()
    handler.setFormatter(formatter)
    if verbose:
        logging.basicConfig(level=logging.DEBUG, handlers=[handler])
    else:
        logging.basicConfig(level=logging.INFO, handlers=[handler])
