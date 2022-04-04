from __future__ import annotations

import shlex
import subprocess
from logging import getLogger
from pathlib import Path
from typing import Optional

from ojw.lang.guesslang import guess_lang
from ojw.util.info import get_case

logger = getLogger(__name__)


def test(args) -> None:
    source: Path = args.filename.resolve()
    optimize: bool = args.optimize
    tle: int = args.tle
    passed: list[str] = args.passed
    casename: Optional[str] = args.case

    if not source.exists():
        logger.error("Source does not exist.")
        raise FileNotFoundError
    if not source.is_file():
        logger.error("Source is not file.")
        raise FileNotFoundError

    test_directory = source.parent / "test"
    assert test_directory.exists()

    lang = guess_lang(source)
    exe = lang.compile(source, optimize)
    command = lang.execute_command(exe)

    oj_test = [
        "oj",
        "test",
        "--command",
        command,
        "--tle",
        str(tle),
        "--directory",
        str(test_directory),
    ]

    oj_test += passed

    if casename is not None:
        case = get_case(casename, test_directory)
        logger.info(f"case found {case}")
        oj_test += case

    logger.info(f'run "{shlex.join(oj_test)}" at {source.parent}.')
    subprocess.run(oj_test, cwd=source.parent)
