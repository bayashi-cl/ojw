import pathlib
import shlex
import subprocess
import sys
import typing
from typing import Dict, List, Optional

from ojw.util.command import get_exec_command, get_oj_command_test
from ojw.util.compile import compile_
from ojw.util.exception import NotACCExeption
from ojw.util.info import find_task_dir, get_case, get_contest_info, get_task_info
from ojw.util.log import log_blue, log_red


def test(args) -> None:
    task_label: str = args.task
    filename: Optional[str] = args.filename
    passed: Optional[List[str]] = args.passed
    case: Optional[str] = args.case
    optimize: bool = args.optimize
    tle: Optional[int] = args.tle

    cwd = pathlib.Path.cwd()
    # ソースとサンプルディレクトリのパスが必要

    # atcoder-cli で作成されたとき
    try:
        contest_info = get_contest_info(cwd)
        task_info = get_task_info(contest_info, task_label)
        task_info_directory = task_info["directory"]
        task_info_directory = typing.cast(Dict[str, str], task_info_directory)

        task_directory = cwd / task_info_directory["path"]
        test_directory = task_directory / task_info_directory["testdir"]
        if filename is None:
            source_file = task_directory / task_info_directory["submit"]
        else:
            source_file = task_directory / filename

    # online-judge-toolで作成されたとき
    except NotACCExeption:
        if filename is None:
            filename = "main.cpp"
        task_directory = find_task_dir(task_label)
        source_file = task_directory / filename
        test_directory = task_directory / "test"

    if not source_file.exists():
        log_red("source file does not exist")
        sys.exit(1)
    if not test_directory.exists():
        log_red("test folder does not exist")
        sys.exit(1)

    log_blue(f"source file found: {source_file}")

    # コンパイル
    if source_file.suffix in {".cpp", ".kt", ".nim"}:
        compile_(source_file, optimize)

    exec_command = get_exec_command(source_file)
    oj_command = get_oj_command_test(exec_command, tle)

    if passed is not None:
        oj_command += passed

    if case is not None:
        case_in, case_out = get_case(case, test_directory)
        log_blue(f"case found {case_in}, {case_out}")
        oj_command += [str(case_in), str(case_out)]

    log_blue(f"test file found: {test_directory}")
    log_blue(f'run "{shlex.join(oj_command)}" at {task_directory}')
    subprocess.run(oj_command, cwd=task_directory)
