from __future__ import annotations

from functools import lru_cache
from logging import getLogger
from pathlib import Path
from typing import Any, Optional

import toml

logger = getLogger(__name__)


@lru_cache(maxsize=10)
def get_config(name: Optional[str] = None) -> dict[str, Any]:
    config_file = Path.home() / ".config" / "ojw" / "config.toml"
    if not config_file.exists():
        config_file.parent.mkdir(parents=True, exist_ok=True)
        config_file.touch()

    logger.info(f"load config from {config_file}")
    config = toml.loads(config_file.read_text())

    if name is None:
        return config
    else:
        return config.get(name, dict())
