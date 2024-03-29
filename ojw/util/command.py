from typing import List, Optional, Tuple
import pathlib
from logging import getLogger

logger = getLogger(__name__)


def get_oj_command_test(command: str, tle: Optional[int]) -> List[str]:
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


def get_byslib_command_bundle(source: pathlib.Path):
    com = [
        "python",
        "-m",
        "expander",
        str(source),
        "--modules",
        "atcoder",
        "byslib",
    ]
    return com


def get_exec_command(source: pathlib.Path, ext: str) -> str:
    if ext == ".py":
        command = f"python {source}"

    elif ext == ".cpp":
        command = str(source)

    elif ext == ".kt":
        command = f"kotlin {source}"

    elif ext == ".nim":
        command = str(source)

    else:
        logger.error("unknown file type")
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
    bin_dir = pathlib.Path().cwd() / "bin"
    if not bin_dir.exists():
        bin_dir.mkdir(exist_ok=True)

    if ext == ".cpp":
        bin_file = bin_dir / "a.out"
        com = get_gpp_compile_args(source, bin_file, optimize)
    elif ext == ".kt":
        bin_file = bin_dir / "main.jar"
        com = get_kotlinc_compile_args(source, bin_file)
    elif ext == ".nim":
        bin_file = bin_dir / "a.out"
        com = get_nim_compile_args(source, bin_file, optimize)

    return com, bin_file
