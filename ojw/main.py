import argparse
from logging import getLogger
from pathlib import Path

import ojw.commands.bundle
import ojw.commands.compile
import ojw.commands.submit
import ojw.commands.test
from ojw.util.config import get_config
from ojw.util.log import setup_logger

logger = getLogger(__name__)


def main() -> None:
    setup_logger(True)
    parser = argparse.ArgumentParser(prog="ojw")
    subparser = parser.add_subparsers()

    # test
    command_test = subparser.add_parser("test", aliases=["t"])
    command_test.add_argument("filename", type=Path)
    command_test.add_argument("--case", "-c")
    command_test.add_argument("--optimize", "-o", action="store_true")
    command_test.add_argument("--tle", "-t", default=10, type=int)
    command_test.add_argument("--passed", "-p", default=[], nargs=argparse.REMAINDER)
    command_test.set_defaults(func=ojw.commands.test.test)

    # submit
    command_submit = subparser.add_parser("submit", aliases=["s"])
    command_submit.add_argument("filename", type=Path)
    command_submit.add_argument("--no-bundle", "-nb", action="store_true")
    command_submit.add_argument("--pypy", action="store_true")
    command_submit.set_defaults(func=ojw.commands.submit.submit)

    # compile
    command_compile = subparser.add_parser("compile", aliases=["c"])
    command_compile.add_argument("filename", type=Path)
    command_compile.add_argument("--optimize", "-o", action="store_true")
    command_compile.set_defaults(func=ojw.commands.compile.compile_)

    # bundle
    command_bundle = subparser.add_parser("bundle", aliases=["b"])
    command_bundle.add_argument("filename", type=Path)
    command_bundle.set_defaults(func=ojw.commands.bundle.bundle)

    args = parser.parse_args()
    args.func(args)
