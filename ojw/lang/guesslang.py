from logging import getLogger
from pathlib import Path

from ojw.lang.base import LangBase
from ojw.lang.cplusplus import ClangLang, GCCLang
from ojw.lang.python import CPythonLang, PypyLang
from ojw.util.config import get_config

logger = getLogger(__name__)


class LanguageError(Exception):
    pass


def guess_lang(source: Path) -> LangBase:
    # config = get_config()
    ext = source.suffix
    if ext == ".py":
        return CPythonLang()
    elif ext in (".cpp", ".hpp"):
        return GCCLang()
    else:
        logger.error("Unknown extention.")
        raise LanguageError
