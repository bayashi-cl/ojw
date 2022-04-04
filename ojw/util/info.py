from __future__ import annotations

import sys
from logging import getLogger
from pathlib import Path

logger = getLogger(__name__)


def get_case(case_name: str, test_dir: Path) -> list[str]:
    res = []
    for case in test_dir.iterdir():
        if not case.is_file():
            continue
        if case.stem.endswith(case_name) or case.name.endswith(case_name):
            res.append(str(case))
            if case.with_suffix(".out").exists():
                res.append(str(case.with_suffix(".out")))
            break
    else:
        logger.error(f"{case_name} does not exist")
        sys.exit(1)

    return res
