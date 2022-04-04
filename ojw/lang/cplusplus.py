from __future__ import annotations

from logging import getLogger
from pathlib import Path

from ojw.lang.base import LangBase

logger = getLogger(__name__)


class GCCLang(LangBase):
    name = "gcc"

    def compile_command(self, source: Path, optimize: bool) -> tuple[list[str], Path]:
        out = Path.cwd() / "bin" / "a.out"
        args = ["g++", str(source), "-o", str(out)]
        if "compile_flags" in self.config:
            flags: list[str] = self.config["compile_flags"]
        else:
            flags = ["-std=gnu++17", "-Wall", "-Wextra"]
            if optimize:
                flags += [
                    "-O2",
                ]
            else:
                flags += [
                    "-D_GLIBCXX_DEBUG",
                    "-DLOCAL",
                    "-g",
                    "-fsanitize=undefined",
                ]

        return args + flags, out

    def bundle_command(self, source: Path) -> list[str]:
        args = self.config.get("bundle_command", ["oj-bundle"])
        flags = self.config.get("bundle_flags", [])

        # for debug
        # flags = ["--release", "-I", "/usr/local/include"]

        args.append(str(source))

        return args + flags

    def execute_command(self, exe: Path) -> str:
        return str(exe)


class ClangLang(LangBase):
    name = "clang"
