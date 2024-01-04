# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class CardinalityEnum(str, enum.Enum):
    """
    * `ONE_TO_ONE` - ONE_TO_ONE
    * `MANY_TO_ONE` - MANY_TO_ONE
    * `MANY_TO_MANY` - MANY_TO_MANY
    * `ONE_TO_MANY` - ONE_TO_MANY
    """

    ONE_TO_ONE = "ONE_TO_ONE"
    MANY_TO_ONE = "MANY_TO_ONE"
    MANY_TO_MANY = "MANY_TO_MANY"
    ONE_TO_MANY = "ONE_TO_MANY"

    def visit(
        self,
        one_to_one: typing.Callable[[], T_Result],
        many_to_one: typing.Callable[[], T_Result],
        many_to_many: typing.Callable[[], T_Result],
        one_to_many: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is CardinalityEnum.ONE_TO_ONE:
            return one_to_one()
        if self is CardinalityEnum.MANY_TO_ONE:
            return many_to_one()
        if self is CardinalityEnum.MANY_TO_MANY:
            return many_to_many()
        if self is CardinalityEnum.ONE_TO_MANY:
            return one_to_many()
