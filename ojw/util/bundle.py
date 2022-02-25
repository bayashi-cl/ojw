import pathlib
import shlex
import subprocess
import sys
from logging import getLogger

from ojw.util.command import get_byslib_command_bundle, get_oj_command_bundle

logger = getLogger(__name__)


def bundle(source: pathlib.Path) -> pathlib.Path:
    if source.suffix == ".cpp":
        com = get_oj_command_bundle(source)
    elif source.suffix == ".py":
        com = get_byslib_command_bundle(source)
    else:
        logger.error("unknown filetype")
        sys.exit(1)

    logger.info(f'run "{shlex.join(com)}"')
    proc = subprocess.run(com, encoding="utf-8", stdout=subprocess.PIPE)
    bundle_path = source.with_name(source.stem + "_bundle" + source.suffix)
    bundle_path.write_text(proc.stdout)
    return bundle_path
