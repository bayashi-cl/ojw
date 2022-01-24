import pathlib
import shlex
import subprocess
from logging import getLogger


from ojw.util.command import get_oj_command_bundle

logger = getLogger(__name__)


def bundle(source: pathlib.Path) -> pathlib.Path:
    com = get_oj_command_bundle(source)
    logger.info(f'run "{shlex.join(com)}"')
    proc = subprocess.run(com, encoding="utf-8", stdout=subprocess.PIPE)
    bundle_path = source.with_name(source.stem + "_bunde" + source.suffix)
    bundle_path.write_text(proc.stdout)
    return bundle_path
