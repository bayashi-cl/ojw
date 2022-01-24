import pathlib
import shlex
import subprocess
import sys
from logging import getLogger
from typing import List

from ojw.util.info import find_task_dir

logger = getLogger(__name__)


def passer(args) -> None:
    task: str = args.task
    passed: List[str] = args.passed

    cwd = pathlib.Path.cwd()
    task_dir = find_task_dir(task)

    oj_command = ["oj"] + passed
    task_dir_relative = "./" + str(task_dir.relative_to(cwd))
    logger.info(f"problem directory found: {task_dir_relative}")
    logger.info(f'run "{shlex.join(oj_command)}" at {task_dir_relative}')
    subprocess.run(oj_command, cwd=task_dir)
