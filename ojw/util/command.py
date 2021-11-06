from typing import List, Optional
import pathlib

from ojw.util.log import log_red


def get_oj_command_test(command: str, tle: Optional[int]) -> List[str]:
    # def get_oj_command(command: str, test_directory: pathlib.Path) -> List[str]:
    if tle is None:
        tle = 10
    oj_command = [
        "oj",
        "test",
        "--command",
        command,
        # "--directory",
        # str(test_directory),
        "--tle",
        str(tle),
    ]
    return oj_command


def get_oj_command_submit(source: pathlib.Path) -> List[str]:
    oj_submit = [
        "oj",
        "submit",
        str(source),
    ]
    return oj_submit


def get_oj_command_bundle(source: pathlib.Path):
    oj_bundle = [
        "oj-bundle",
        "-I",
        str(pathlib.Path("/usr/local/include")),
        str(source),
    ]
    return oj_bundle


def get_exec_command(source: pathlib.Path) -> str:
    ext = source.suffix
    if ext == ".py":
        command = f"python {source}"

    elif ext == ".cpp":
        command = str(source.with_name("a.out"))

    else:
        log_red("unknown file type")
        raise ValueError

    return command


def get_gpp_compile_args(
    source: pathlib.Path, bin: pathlib.Path, optimize: bool
) -> List[str]:
    res = [
        "g++",
        str(source),
        "-o",
        str(bin),
        "-std=gnu++17",
        "-Wall",
        "-Wextra",
    ]
    if optimize:
        res += [
            "-O2",
        ]
    else:
        res += [
            "-D_GLIBCXX_DEBUG",
            "-DLOCAL",
            "-g",
            "-fsanitize=undefined",
        ]
    return res
