from __future__ import annotations

import sys
from logging import getLogger
from pathlib import Path

from ojw.lang.base import LangBase

logger = getLogger(__name__)


class CPythonLang(LangBase):
    name = "cpython"

    def compile_command(self, source: Path, optimize: bool) -> tuple[list[str], Path]:
        return [], source

    def bundle_command(self, source: Path) -> list[str]:
        try:
            args: list[str] = self.config["bundle_command"]
        except KeyError:
            logger.error("Please specify bundle command for Python.")
            logger.error("oj-bundle does not support Python.")
            # for debug
            sys.exit(1)

        flags: list[str] = self.config.get("bundle_flags", [])

        # for debug
        # args = ["python", "-m", "expander"]
        # flags = ["-m", "byslib", "atcoder", "sortedcontainers", "more_itertools"]

        args.append(str(source))
        return args + flags

    def execute_command(self, exe: Path) -> str:
        return f"{sys.executable} {exe}"


class PypyLang(CPythonLang):
    name = "pypy"

    def execute_command(self, exe: Path) -> str:
        return f"pypy {exe}"
