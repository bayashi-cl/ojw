import shlex
import subprocess
from logging import getLogger
from pathlib import Path

from ojw.lang.guesslang import guess_lang

logger = getLogger(__name__)


def submit(args) -> None:
    source: Path = args.filename.resolve()

    if not source.exists():
        logger.error("Source does not exist.")
        raise FileNotFoundError
    if not source.is_file():
        logger.error("Source is not file.")
        raise FileNotFoundError

    logger.info(f"source file found: {source}")
    lang = guess_lang(source)
    bundle_flg = False
    try:
        source = lang.bundle(source)
        bundle_flg = True
    except Exception:
        pass

    oj_submit = ["oj", "submit", str(source)]
    if args.pypy:
        oj_submit += ["--guess-python-interpreter", "pypy"]

    logger.info(f'run "{shlex.join(oj_submit)}" at {source.parent}')
    subprocess.run(oj_submit, cwd=source.parent)
    if bundle_flg:
        source.unlink()
