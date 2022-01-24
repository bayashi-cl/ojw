import json
import pathlib
import sys
import typing
from typing import Dict, List, Tuple, Union
from logging import getLogger

logger = getLogger(__name__)


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

    problem_dir: List[pathlib.Path] = []
    for dir in subdir:
        if dir.name.startswith("."):
            continue
        if str(dir).endswith(task):
            problem_dir.append(dir)

    if len(problem_dir) == 0:
        logger.error("cannot find such problem.")
        sys.exit(1)
    elif len(problem_dir) == 1:
        return problem_dir[0]
    else:
        logger.error("Multiple directories applied.")
        logger.error(" ".join(dir.name for dir in problem_dir))
        sys.exit(1)
