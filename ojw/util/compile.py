import pathlib
import subprocess
import sys

from ojw.util.log import log_blue, log_red
from ojw.util.command import get_gpp_compile_args


def cpp_compile(source_file: pathlib.Path) -> None:
    # bin_file = source_file.parent / "a.out"
    bin_file = source_file.with_name("a.out")
    if bin_file.exists():
        if source_file.stat().st_mtime < bin_file.stat().st_mtime:
            log_blue("Source file has already been compiled.")
            return
    log_blue("Starting build...")
    try:
        subprocess.run(get_gpp_compile_args(source_file, bin_file), check=True)
    except subprocess.CalledProcessError:
        log_red("compile error")
        sys.exit(1)

    log_blue("Build finished successfully.")
