import argparse
import json
import pathlib
import subprocess
import sys
import typing
from typing import Dict, List, Optional, Union, Tuple

import colorama

TaskInfoJSON = Dict[str, Union[str, Dict[str, str]]]
ContestInfoJSON = Dict[str, Union[Dict[str, str], List[TaskInfoJSON]]]
CONTEST_ACC = "contest.acc.json"


def get_contest_info(cwd: pathlib.Path) -> ContestInfoJSON:
    file = cwd / CONTEST_ACC
    return json.load(file.open())


def get_task_info(contestinfo: ContestInfoJSON, task_label: str) -> TaskInfoJSON:
    for task in contestinfo["tasks"]:
        task = typing.cast(TaskInfoJSON, task)
        if task["label"] == task_label:
            task_info = task
            break
    else:
        raise ValueError

    return task_info


def get_case(
    case_name: str, test_dir: pathlib.Path
) -> Tuple[pathlib.Path, pathlib.Path]:
    if case_name.isdecimal():
        for case in test_dir.iterdir():
            if case_name in case.name:
                case_in = test_dir / (case.stem + ".in")
                case_out = test_dir / (case.stem + ".out")
                break
    else:
        case_in = test_dir / (case_name + ".in")
        case_out = test_dir / (case_name + ".out")

    if not (case_in.exists() and case_out.exists()):
        log_red(f"{case_name} does not exist")
        sys.exit(1)

    return (case_in, case_out)


def log_blue(msg: str) -> None:
    print("OJW: " + colorama.Fore.BLUE + msg + colorama.Style.RESET_ALL)


def log_red(msg: str) -> None:
    print("OJW: " + colorama.Fore.RED + msg + colorama.Style.RESET_ALL)


def cpp_compile(source_file: pathlib.Path) -> None:
    bin_file = source_file.parent / "a.out"
    if bin_file.exists():
        if source_file.stat().st_mtime < bin_file.stat().st_mtime:
            log_blue("Source file has already been compiled.")
            return

    gppargs = [
        "g++",
        str(source_file),
        "-o",
        str(bin_file),
        "-std=c++17",
        "-D_GLIBCXX_DEBUG",
        "-Wall",
        "-Wno-unknown-pragmas",
    ]
    log_blue("Starting build...")
    try:
        subprocess.run(gppargs, check=True)
    except subprocess.CalledProcessError:
        log_red("compile error")
        sys.exit(1)

    log_blue("Build finished successfully.")


def test(args) -> None:
    task_label: str = args.task.upper()
    filename: Optional[str] = args.filename
    passed: Optional[List[str]] = args.passed
    case: Optional[str] = args.case

    cwd = pathlib.Path.cwd()
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

    if not source_file.exists():
        log_red("source file does not exist")
        sys.exit(1)

    ext = source_file.suffix
    if ext == ".py":
        command = f"python {source_file}"

    elif ext == ".cpp":
        cpp_compile(source_file)
        command = f"{task_directory}/a.out"

    else:
        log_red("unknown file type")
        raise ValueError

    oj_command: List[str] = [
        "oj",
        "test",
        "--command",
        command,
        "--directory",
        str(test_directory),
    ]

    if passed is not None:
        oj_command += passed

    if case is not None:
        case_in, case_out = get_case(case, test_directory)
        oj_command += [str(case_in), str(case_out)]

    subprocess.run(oj_command)


def submit(args) -> None:
    task_label: str = args.task.upper()
    filename: Optional[str] = args.filename

    cwd = pathlib.Path.cwd()
    contest_info = get_contest_info(cwd)
    task_info = get_task_info(contest_info, task_label)
    task_info_directory = task_info["directory"]
    task_info_directory = typing.cast(Dict[str, str], task_info_directory)

    task_directory = cwd / task_info_directory["path"]
    if filename is None:
        source_file = task_directory / task_info_directory["submit"]
    else:
        source_file = task_directory / filename

    if not source_file.exists():
        log_red("source file does not exist")

    acc_command = [
        "acc",
        "submit",
    ]
    if filename is not None:
        acc_command.append(filename)

    subprocess.run(acc_command, cwd=task_directory)


def main():
    parser = argparse.ArgumentParser(prog="ojw")
    subparser = parser.add_subparsers()

    command_test = subparser.add_parser("test", aliases=["t"])
    command_test.add_argument("task")
    command_test.add_argument("filename", nargs="?")
    command_test.add_argument("--case", "-c")
    command_test.add_argument("--manual", "-m", action="store_true")
    command_test.add_argument("--passed", "-p", nargs="*")
    command_test.set_defaults(func=test)

    command_submit = subparser.add_parser("submit", aliases=["s"])
    command_submit.add_argument("task")
    command_submit.add_argument("filename", nargs="?")
    command_submit.set_defaults(func=submit)

    args = parser.parse_args()
    args.func(args)
