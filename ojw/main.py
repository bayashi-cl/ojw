import argparse
import json
import pathlib
import subprocess
import typing
from typing import Dict, List, Optional, Union

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


def test(args) -> None:
    task_label: str = args.task.upper()
    filename: Optional[str] = args.filename
    passed: Optional[List[str]] = args.passed

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

    python_command = "python {}".format(str(source_file))
    oj_command: List[str] = [
        "oj",
        "test",
        "--command",
        python_command,
        "--directory",
        str(test_directory),
    ]

    if passed is not None:
        oj_command += passed

    subprocess.run(oj_command)


def main():
    parser = argparse.ArgumentParser(prog="ojw")
    subparser = parser.add_subparsers()

    command_test = subparser.add_parser("test", aliases=["t"])
    command_test.add_argument("task")
    command_test.add_argument("filename", default=None)
    command_test.add_argument("--passed", nargs="*")
    command_test.set_defaults(func=test)

    args = parser.parse_args()
    args.func(args)
