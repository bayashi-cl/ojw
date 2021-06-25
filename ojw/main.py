# import sys
import argparse


def new(args: argparse.Namespace):
    print("new")


def test(args):
    print("test")


def submit(args):
    print("submit")


def main():
    parser = argparse.ArgumentParser(prog="ojw")
    subparser = parser.add_subparsers()

    command_new = subparser.add_parser("new", aliases=["n"])
    command_new.set_defaults(func=new)

    command_test = subparser.add_parser("test", aliases=["t"])
    command_test.set_defaults(func=test)

    command_submit = subparser.add_parser("submit", aliases=["s"])
    command_submit.set_defaults(func=submit)

    args = parser.parse_args()
    args.func(args)
