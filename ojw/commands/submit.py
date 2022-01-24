import pathlib
import shlex
import subprocess
import sys
import typing
from logging import getLogger
from typing import Dict, List, Optional

from ojw.util.bundle import bundle
from ojw.util.command import get_oj_command_submit
from ojw.util.exception import NotACCExeption
from ojw.util.info import find_task_dir, get_contest_info, get_task_info

logger = getLogger(__name__)


def submit(args) -> None:
    task_label: str = args.task
    filename: Optional[str] = args.filename

    cwd = pathlib.Path.cwd()
    try:
        contest_info = get_contest_info(cwd)
        task_info = get_task_info(contest_info, task_label.upper())
        task_info_directory = task_info["directory"]
        task_info_directory = typing.cast(Dict[str, str], task_info_directory)

        task_directory = cwd / task_info_directory["path"]
        if filename is None:
            source_file = task_directory / task_info_directory["submit"]
        else:
            source_file = task_directory / filename
    except NotACCExeption:
        if filename is None:
            filename = "main.cpp"
        task_directory = find_task_dir(task_label)
        source_file = task_directory / filename

    if not source_file.exists():
        logger.error("source file does not exist")
        sys.exit(1)

    # if args.bundle:
    if source_file.suffix == ".cpp" or args.bundle:
        source_file = bundle(source_file)

    oj_submit = get_oj_command_submit(source_file)
    logger.info(f"source file found: {source_file}")
    logger.info(f'run "{shlex.join(oj_submit)}" at {task_directory}')
    subprocess.run(oj_submit, cwd=task_directory)
