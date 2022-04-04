from logging import getLogger
from pathlib import Path

from ojw.lang.guesslang import guess_lang

logger = getLogger(__name__)


def bundle(args):
    source: Path = args.filename.resolve()

    if not source.exists():
        logger.error("Source does not exist.")
        raise FileNotFoundError
    if not source.is_file():
        logger.error("Source is not file.")
        raise FileNotFoundError

    logger.info(f"source file found: {source}")
    lang = guess_lang(source)
    lang.bundle(source)
