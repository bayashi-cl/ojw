import pathlib
import shlex
import subprocess
import sys
import typing
from logging import getLogger
from typing import Dict, List, Optional

from ojw.util.bundle import bundle
from ojw.util.command import get_oj_command_submit
from ojw.util.info import find_task_dir

logger = getLogger(__name__)


def submit(args) -> None:
    task_label: str = args.task
    filename: Optional[str] = args.filename

    if filename is None:
        filename = "main.cpp"
    task_directory = find_task_dir(task_label)
    source_file = task_directory / filename

    if not source_file.exists():
        logger.error("source file does not exist")
        sys.exit(1)

    # if args.bundle:
    bundle_flg = False
    if source_file.suffix in {".cpp", ".py"} and args.no_bundle:
        bundle_flg = True
        source_file = bundle(source_file)

    oj_submit = get_oj_command_submit(source_file)
    if args.pypy:
        oj_submit += ["--guess-python-interpreter", "pypy"]
    logger.info(f"source file found: {source_file}")
    logger.info(f'run "{shlex.join(oj_submit)}" at {task_directory}')
    subprocess.run(oj_submit, cwd=task_directory)
    if bundle_flg:
        source_file.unlink()
