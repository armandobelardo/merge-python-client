# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class PurchaseOrderStatusEnum(str, enum.Enum):
    """
    * `DRAFT` - DRAFT
    * `SUBMITTED` - SUBMITTED
    * `AUTHORIZED` - AUTHORIZED
    * `BILLED` - BILLED
    * `DELETED` - DELETED
    """

    DRAFT = "DRAFT"
    SUBMITTED = "SUBMITTED"
    AUTHORIZED = "AUTHORIZED"
    BILLED = "BILLED"
    DELETED = "DELETED"

    def visit(
        self,
        draft: typing.Callable[[], T_Result],
        submitted: typing.Callable[[], T_Result],
        authorized: typing.Callable[[], T_Result],
        billed: typing.Callable[[], T_Result],
        deleted: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is PurchaseOrderStatusEnum.DRAFT:
            return draft()
        if self is PurchaseOrderStatusEnum.SUBMITTED:
            return submitted()
        if self is PurchaseOrderStatusEnum.AUTHORIZED:
            return authorized()
        if self is PurchaseOrderStatusEnum.BILLED:
            return billed()
        if self is PurchaseOrderStatusEnum.DELETED:
            return deleted()