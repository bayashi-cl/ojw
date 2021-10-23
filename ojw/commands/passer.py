import pathlib
import subprocess
import sys
from typing import List
import shlex

from ojw.util.log import log_blue, log_red
from ojw.util.info import find_task_dir


def passer(args) -> None:
    task: str = args.task
    passed: List[str] = args.passed

    cwd = pathlib.Path.cwd()
    task_dir = find_task_dir(task)

    oj_command = ["oj"] + passed
    task_dir_relative = "./" + str(task_dir.relative_to(cwd))
    log_blue(f"problem directory found: {task_dir_relative}")
    log_blue(f'run "{shlex.join(oj_command)}" at {task_dir_relative}')
    subprocess.run(oj_command, cwd=task_dir)
