import argparse

import ojw.commands.submit
import ojw.commands.test
import ojw.commands.passer
import ojw.commands.compile


def main() -> None:

    parser = argparse.ArgumentParser(prog="ojw")
    subparser = parser.add_subparsers()

    # test
    command_test = subparser.add_parser("test", aliases=["t"])
    command_test.add_argument("task")
    command_test.add_argument("filename", nargs="?")
    command_test.add_argument("--case", "-c")
    command_test.add_argument("--manual", "-m", action="store_true")
    command_test.add_argument("--passed", "-p", nargs=argparse.REMAINDER)
    command_test.set_defaults(func=ojw.commands.test.test)

    # submit
    command_submit = subparser.add_parser("submit", aliases=["s"])
    command_submit.add_argument("task")
    command_submit.add_argument("filename", nargs="?")
    command_submit.set_defaults(func=ojw.commands.submit.submit)

    # passer
    command_passer = subparser.add_parser("passer", aliases=["p"])
    command_passer.add_argument("task", type=str)
    command_passer.add_argument("passed", nargs=argparse.REMAINDER)
    command_passer.set_defaults(func=ojw.commands.passer.passer)

    # compile
    command_compile = subparser.add_parser("compile", aliases=["c"])
    command_compile.add_argument("filename", type=str)
    command_compile.add_argument("--force", "-f", action="store_true")
    command_compile.set_defaults(func=ojw.commands.compile.compile)

    args = parser.parse_args()
    args.func(args)


def passer() -> None:
    print("use ojw")
