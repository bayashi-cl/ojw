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


# def cpp_compile(source_file: pathlib.Path, optimize: bool) -> None:
#     bin_file = source_file.with_name("a.out")
#     log_blue("Starting build...")
#     try:
#         com = get_gpp_compile_args(source_file, bin_file, optimize)
#         log_blue(f'run "{shlex.join(com)}"')
#         subprocess.run(com, check=True)
#     except subprocess.CalledProcessError:
#         log_red("compile error")
#         sys.exit(1)

#     log_blue("Build finished successfully.")


# def kt_compile(source_file: pathlib.Path) -> None:
#     bin_file = source_file.with_name("main.jar")
#     log_blue("Starting build...")
#     try:
#         com = get_kotlinc_compile_args(source_file, bin_file)
#         log_blue(f'run "{shlex.join(com)}"')
#         subprocess.run(com, check=True)
#     except subprocess.CalledProcessError:
#         log_red("compile error")
#         sys.exit(1)

#     log_blue("Build finished successfully.")
