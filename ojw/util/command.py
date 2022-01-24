from typing import List, Optional, Tuple
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

    elif ext == ".kt":
        command = f"kotlin {source.with_name('main.jar')}"

    elif ext == ".nim":
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


def get_kotlinc_compile_args(source: pathlib.Path, bin: pathlib.Path) -> List[str]:
    res = [
        "kotlinc",
        str(source),
        "-include-runtime",
        "-d",
        str(bin),
    ]
    return res


def get_nim_compile_args(
    source: pathlib.Path, bin: pathlib.Path, optimize: bool
) -> List[str]:
    res = [
        "nim",
        "cpp",
    ]
    if optimize:
        res += [
            "-d:release",
            "--opt:speed",
            "--multimethods:on",
        ]
    res += [
        "--verbosity:0",
        "--hints:off",
        "--out:" + str(bin),
        str(source),
    ]
    return res


def get_compile_args_and_bin(
    source: pathlib.Path, optimize: bool
) -> Tuple[List[str], pathlib.Path]:
    ext = source.suffix
    if ext == ".cpp":
        bin_file = source.with_name("a.out")
        com = get_gpp_compile_args(source, bin_file, optimize)
    elif ext == ".kt":
        bin_file = source.with_name("main.jar")
        com = get_kotlinc_compile_args(source, bin_file)
    elif ext == ".nim":
        bin_file = source.with_name("a.out")
        com = get_nim_compile_args(source, bin_file, optimize)

    return com, bin_file
