import argparse
import json
import pathlib
import subprocess


def test(args):
    file: pathlib.Path = args.filename.resolve()

    # testdirを取得
    dir_name = file.parent.name
    info_file = file.parents[1] / "contest.acc.json"
    info = json.load(info_file.open())
    for task in info["tasks"]:
        if task["directory"]["path"] == dir_name:
            test_directory = task["directory"]["testdir"]
            break
    else:
        raise ValueError

    python_command = '"python {}"'.format(str(file))
    oj_command = [
        "oj",
        "test",
        "-c",
        python_command,
        "--directory",
        test_directory,
    ]
    subprocess.run(" ".join(oj_command), shell=True)


def main():
    parser = argparse.ArgumentParser(prog="ojw")
    subparser = parser.add_subparsers()

    command_test = subparser.add_parser("test", aliases=["t"])
    command_test.add_argument("filename", type=pathlib.Path)
    command_test.set_defaults(func=test)

    args = parser.parse_args()
    args.func(args)
