import sys
from typing import Optional

from ojw.util.bundle import bundle
from ojw.util.info import find_task_dir
from ojw.util.log import log_red


def bundle_(args):
    task_label: str = args.task
    filename: Optional[str] = args.filename

    if filename is None:
        filename = "main.cpp"
    task_directory = find_task_dir(task_label)
    source_file = task_directory / filename

    if source_file.suffix != ".cpp":
        log_red("bundle is only for c++")
        sys.exit(1)

    if not source_file.exists():
        log_red("source file does not exist")
        sys.exit(1)

    bundle(source_file)
