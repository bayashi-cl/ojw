from __future__ import annotations

import shlex
import subprocess
import sys
from abc import ABC, abstractmethod
from logging import getLogger
from pathlib import Path
from typing import Any

from ojw.util.config import get_config

logger = getLogger(__name__)


class LangBase(ABC):
    name = "base"

    def __init__(self, *, config: dict[str, Any] = None) -> None:
        if config is None:
            self.config = get_config(self.name)
        else:
            self.config = config

    @abstractmethod
    def compile_command(self, source: Path, optimize: bool) -> tuple[list[str], Path]:
        """get compile command

        Args:
            source (Path): Path of source code.
            optimize (bool): Optimize binary.

        Returns:
            tuple[list[str], Path]: (command, outfile)
        """
        raise NotImplementedError

    def compile(self, source: Path, optimize: bool) -> Path:
        """compile source

        Args:
            source (Path): Path of source code.
            optimize (bool): Optimize binary.

        Returns:
            Path: executable file
        """
        args, out = self.compile_command(source, optimize)
        if args:
            if not out.parent.exists():
                out.parent.mkdir(parents=True, exist_ok=True)
            try:
                logger.info(f'run "{shlex.join(args)}"')
                subprocess.run(args, check=True)
            except subprocess.CalledProcessError:
                logger.error("compile error")
                sys.exit(1)

        return out

    @abstractmethod
    def bundle_command(self, source: Path) -> list[str]:
        """get bundle command

        Args:
            source (Path): source file

        Returns:
            list[str]: command
        """
        raise NotImplementedError

    def bundle(self, source: Path) -> Path:
        """bundle source

        Args:
            source (Path): source code path

        Returns:
            Path: bundled file
        """

        args = self.bundle_command(source)
        logger.info(f'run "{shlex.join(args)}"')
        code = subprocess.check_output(args, text=True)

        bundled = source.with_name(source.stem + "_bundle" + source.suffix)
        bundled.write_text(code)

        return bundled

    @abstractmethod
    def execute_command(self, exe: Path) -> str:
        """get execute command

        Args:
            exe (Path): executable file

        Returns:
            list[str]: command to run
        """
        raise NotImplementedError
