from typing import NamedTuple, Optional, List, Callable


class ArgsTest(NamedTuple):
    filename: str
    passed: List[str]


# class ArgsSubmit(NamedTuple):
#     source: str
#     language: Optional[str]
#     force: bool
