import pathlib
import subprocess
import sys
import typing
from typing import Dict, List, Optional

# from util.const import CONTEST_ACC
from ojw.util.info import get_case, get_contest_info, get_task_info
from ojw.util.log import log_blue, log_red
from ojw.util.compile import cpp_compile
from ojw.util.command import get_oj_command_test, get_exec_command
from ojw.util.exception import NotACCExeption
from ojw.util.info import find_task_dir


def test(args) -> None:
    task_label: str = args.task.upper()
    filename: Optional[str] = args.filename
    passed: Optional[List[str]] = args.passed
    case: Optional[str] = args.case

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
        task_directory = find_task_dir(task_label.lower())
        source_file = task_directory / filename
        test_directory = task_directory / "test"

    if not source_file.exists():
        log_red("source file does not exist")
        sys.exit(1)
    if not test_directory.exists():
        log_red("test folder does not exist")
        sys.exit(1)

    # コンパイル
    if source_file.suffix == ".cpp":
        cpp_compile(source_file)

    exec_command = get_exec_command(source_file)
    oj_command = get_oj_command_test(exec_command)

    if passed is not None:
        oj_command += passed

    if case is not None:
        case_in, case_out = get_case(case, test_directory)
        oj_command += [str(case_in), str(case_out)]

    subprocess.run(oj_command, cwd=task_directory)
