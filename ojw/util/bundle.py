import pathlib
import shlex
import subprocess

from ojw.util.command import get_oj_command_bundle
from ojw.util.log import log_blue


def bundle(source: pathlib.Path) -> pathlib.Path:
    com = get_oj_command_bundle(source)
    log_blue(f'run "{shlex.join(com)}"')
    proc = subprocess.run(com, encoding="utf-8", stdout=subprocess.PIPE)
    out = proc.stdout.replace("/home/bayashi/dev/byslib/", "")
    bundle_path = source.with_name(source.stem + "_bunde" + source.suffix)
    bundle_path.write_text(out)
    return bundle_path
