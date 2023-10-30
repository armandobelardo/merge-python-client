# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class LocationsListRequestLocationType(str, enum.Enum):
    HOME = "HOME"
    WORK = "WORK"

    def visit(self, home: typing.Callable[[], T_Result], work: typing.Callable[[], T_Result]) -> T_Result:
        if self is LocationsListRequestLocationType.HOME:
            return home()
        if self is LocationsListRequestLocationType.WORK:
            return work()
