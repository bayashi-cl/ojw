import pathlib
import shlex
import subprocess
import sys

from ojw.util.command import get_compile_args_and_bin
from ojw.util.log import log_blue, log_red


def compile_(source_file: pathlib.Path, optimize: bool) -> pathlib.Path:
    com, bin_file = get_compile_args_and_bin(source_file, optimize)

    log_blue("Starting build...")
    try:
        log_blue(f'run "{shlex.join(com)}"')
        subprocess.run(com, check=True)
    except subprocess.CalledProcessError:
        log_red("compile error")
        sys.exit(1)

    log_blue("Build finished successfully.")
    return bin_file
