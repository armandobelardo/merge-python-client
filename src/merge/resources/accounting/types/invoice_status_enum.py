# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class InvoiceStatusEnum(str, enum.Enum):
    """
    * `PAID` - PAID
    * `DRAFT` - DRAFT
    * `SUBMITTED` - SUBMITTED
    * `PARTIALLY_PAID` - PARTIALLY_PAID
    * `OPEN` - OPEN
    * `VOID` - VOID
    """

    PAID = "PAID"
    DRAFT = "DRAFT"
    SUBMITTED = "SUBMITTED"
    PARTIALLY_PAID = "PARTIALLY_PAID"
    OPEN = "OPEN"
    VOID = "VOID"

    def visit(
        self,
        paid: typing.Callable[[], T_Result],
        draft: typing.Callable[[], T_Result],
        submitted: typing.Callable[[], T_Result],
        partially_paid: typing.Callable[[], T_Result],
        open: typing.Callable[[], T_Result],
        void: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is InvoiceStatusEnum.PAID:
            return paid()
        if self is InvoiceStatusEnum.DRAFT:
            return draft()
        if self is InvoiceStatusEnum.SUBMITTED:
            return submitted()
        if self is InvoiceStatusEnum.PARTIALLY_PAID:
            return partially_paid()
        if self is InvoiceStatusEnum.OPEN:
            return open()
        if self is InvoiceStatusEnum.VOID:
            return void()
