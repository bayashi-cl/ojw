from typing import NamedTuple, Optional


class ArgsNew(NamedTuple):
    contest_id: str
    target: Optional[str]
    language: Optional[str]


class ArgsTest(NamedTuple):
    source: str
    case: Optional[str]
    interactive: bool
    error: bool


class ArgsSubmit(NamedTuple):
    source: str
    language: Optional[str]
    force: bool
