# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class SelectiveSyncConfigurationsUsageEnum(str, enum.Enum):
    """
    * `IN_NEXT_SYNC` - IN_NEXT_SYNC
    * `IN_LAST_SYNC` - IN_LAST_SYNC
    """

    IN_NEXT_SYNC = "IN_NEXT_SYNC"
    IN_LAST_SYNC = "IN_LAST_SYNC"

    def visit(
        self, in_next_sync: typing.Callable[[], T_Result], in_last_sync: typing.Callable[[], T_Result]
    ) -> T_Result:
        if self is SelectiveSyncConfigurationsUsageEnum.IN_NEXT_SYNC:
            return in_next_sync()
        if self is SelectiveSyncConfigurationsUsageEnum.IN_LAST_SYNC:
            return in_last_sync()
