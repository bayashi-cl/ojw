from typing import List
import pathlib

from ojw.util.log import log_red


def get_oj_command_test(command: str) -> List[str]:
    # def get_oj_command(command: str, test_directory: pathlib.Path) -> List[str]:
    oj_command = [
        "oj",
        "test",
        "--command",
        command,
        # "--directory",
        # str(test_directory),
        "--tle",
        "3",
    ]
    return oj_command


def get_oj_command_submit(source: pathlib.Path) -> List[str]:
    oj_submit = [
        "oj",
        "submit",
        str(source),
    ]
    return oj_submit


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


def get_gpp_compile_args(source: pathlib.Path, bin: pathlib.Path) -> List[str]:
    res = [
        "g++",
        str(source),
        "-o",
        str(bin),
        "-std=c++17",
        "-D_GLIBCXX_DEBUG",
        "-DLOCAL",
        "-Wall",
        "-Wno-unknown-pragmas",
        "-g",
        "-fsanitize=undefined",
    ]
    return res
