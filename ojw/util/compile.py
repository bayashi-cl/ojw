import pathlib
import shlex
import subprocess
import sys
from logging import getLogger

from ojw.util.command import get_compile_args_and_bin

logger = getLogger(__name__)


def compile_(source_file: pathlib.Path, optimize: bool) -> pathlib.Path:
    com, bin_file = get_compile_args_and_bin(source_file, optimize)

    logger.info("Starting build...")
    try:
        logger.info(f'run "{shlex.join(com)}"')
        subprocess.run(com, check=True)
    except subprocess.CalledProcessError:
        logger.error("compile error")
        sys.exit(1)

    logger.info("Build finished successfully.")
    return bin_file
