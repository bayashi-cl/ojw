import json
import pathlib
import sys
import typing
from typing import Dict, List, Tuple, Union
from logging import getLogger

from ojw.util.const import CONTEST_ACC
from ojw.util.exception import NotACCExeption

logger = getLogger(__name__)

TaskInfoJSON = Dict[str, Union[str, Dict[str, str]]]
ContestInfoJSON = Dict[str, Union[Dict[str, str], List[TaskInfoJSON]]]


def get_contest_info(cwd: pathlib.Path) -> ContestInfoJSON:
    file = cwd / CONTEST_ACC
    if not file.exists():
        raise NotACCExeption
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
        logger.error(f"{case_name} does not exist")
        sys.exit(1)

    return (case_in, case_out)


def find_task_dir(task: str) -> pathlib.Path:
    cwd = pathlib.Path.cwd()
    subdir = [x for x in cwd.iterdir() if x.is_dir()]

    for dir in subdir:
        if dir.name.startswith("."):
            continue
        if str(dir).endswith(task):
            problem_dir = dir
            break
    else:
        logger.error("cannot find such problem.")
        sys.exit(1)

    return problem_dir
