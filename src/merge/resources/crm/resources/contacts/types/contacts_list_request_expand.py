# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class ContactsListRequestExpand(str, enum.Enum):
    ACCOUNT = "account"
    ACCOUNT_OWNER = "account,owner"
    OWNER = "owner"

    def visit(
        self,
        account: typing.Callable[[], T_Result],
        account_owner: typing.Callable[[], T_Result],
        owner: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ContactsListRequestExpand.ACCOUNT:
            return account()
        if self is ContactsListRequestExpand.ACCOUNT_OWNER:
            return account_owner()
        if self is ContactsListRequestExpand.OWNER:
            return owner()
