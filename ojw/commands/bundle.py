import sys
from logging import getLogger
from typing import Optional

from ojw.util.bundle import bundle
from ojw.util.info import find_task_dir


logger = getLogger(__name__)


def bundle_(args):
    task_label: str = args.task
    filename: Optional[str] = args.filename

    if filename is None:
        filename = "main.cpp"
    task_directory = find_task_dir(task_label)
    source_file = task_directory / filename

    if source_file.suffix != ".cpp":
        logger.error("bundle is only for c++")
        sys.exit(1)

    if not source_file.exists():
        logger.error("source file does not exist")
        sys.exit(1)

    bundle(source_file)
