from logging import getLogger
from pathlib import Path

from ojw.lang.guesslang import guess_lang

logger = getLogger(__name__)


def compile_(args) -> None:
    source: Path = args.filename.resolve()
    optimize: bool = args.optimize

    if not source.exists():
        logger.error("Source does not exist.")
        raise FileNotFoundError
    if not source.is_file():
        logger.error("Source is not file.")
        raise FileNotFoundError

    logger.info(f"source file found: {source}")
    lang = guess_lang(source)
    exe = lang.compile(source, optimize)
    logger.info(f"executable: {exe}")
