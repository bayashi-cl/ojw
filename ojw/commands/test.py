import pathlib
import shlex
import subprocess
import sys
import typing
from logging import getLogger
from typing import Dict, List, Optional

from ojw.util.command import get_exec_command, get_oj_command_test
from ojw.util.compile import compile_
from ojw.util.info import find_task_dir, get_case

logger = getLogger(__name__)


def test(args) -> None:
    task_label: str = args.task
    filename: Optional[str] = args.filename
    passed: Optional[List[str]] = args.passed
    case: Optional[str] = args.case
    optimize: bool = args.optimize
    tle: Optional[int] = args.tle

    # ソースとサンプルディレクトリのパスが必要
    if filename is None:
        filename = "main.cpp"
    task_directory = find_task_dir(task_label)
    source_file = task_directory / filename
    test_directory = task_directory / "test"

    if not source_file.exists():
        logger.error("source file does not exist")
        sys.exit(1)
    if not test_directory.exists():
        logger.error("test folder does not exist")
        sys.exit(1)

    logger.info(f"source file found: {source_file}")

    # コンパイル
    if source_file.suffix in {".cpp", ".kt", ".nim"}:
        compile_(source_file, optimize)

    exec_command = get_exec_command(source_file)
    oj_command = get_oj_command_test(exec_command, tle)

    if passed is not None:
        oj_command += passed

    if case is not None:
        case_in, case_out = get_case(case, test_directory)
        logger.info(f"case found {case_in}, {case_out}")
        oj_command += [str(case_in), str(case_out)]

    logger.info(f"test file found: {test_directory}")
    logger.info(f'run "{shlex.join(oj_command)}" at {task_directory}')
    subprocess.run(oj_command, cwd=task_directory)
