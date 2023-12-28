# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class TransactionsListRequestExpand(str, enum.Enum):
    ACCOUNT = "account"
    ACCOUNT_ACCOUNTING_PERIOD = "account,accounting_period"
    ACCOUNTING_PERIOD = "accounting_period"
    CONTACT = "contact"
    CONTACT_ACCOUNT = "contact,account"
    CONTACT_ACCOUNT_ACCOUNTING_PERIOD = "contact,account,accounting_period"
    CONTACT_ACCOUNTING_PERIOD = "contact,accounting_period"
    LINE_ITEMS = "line_items"
    LINE_ITEMS_ACCOUNT = "line_items,account"
    LINE_ITEMS_ACCOUNT_ACCOUNTING_PERIOD = "line_items,account,accounting_period"
    LINE_ITEMS_ACCOUNTING_PERIOD = "line_items,accounting_period"
    LINE_ITEMS_CONTACT = "line_items,contact"
    LINE_ITEMS_CONTACT_ACCOUNT = "line_items,contact,account"
    LINE_ITEMS_CONTACT_ACCOUNT_ACCOUNTING_PERIOD = "line_items,contact,account,accounting_period"
    LINE_ITEMS_CONTACT_ACCOUNTING_PERIOD = "line_items,contact,accounting_period"
    LINE_ITEMS_TRACKING_CATEGORIES = "line_items,tracking_categories"
    LINE_ITEMS_TRACKING_CATEGORIES_ACCOUNT = "line_items,tracking_categories,account"
    LINE_ITEMS_TRACKING_CATEGORIES_ACCOUNT_ACCOUNTING_PERIOD = (
        "line_items,tracking_categories,account,accounting_period"
    )
    LINE_ITEMS_TRACKING_CATEGORIES_ACCOUNTING_PERIOD = "line_items,tracking_categories,accounting_period"
    LINE_ITEMS_TRACKING_CATEGORIES_CONTACT = "line_items,tracking_categories,contact"
    LINE_ITEMS_TRACKING_CATEGORIES_CONTACT_ACCOUNT = "line_items,tracking_categories,contact,account"
    LINE_ITEMS_TRACKING_CATEGORIES_CONTACT_ACCOUNT_ACCOUNTING_PERIOD = (
        "line_items,tracking_categories,contact,account,accounting_period"
    )
    LINE_ITEMS_TRACKING_CATEGORIES_CONTACT_ACCOUNTING_PERIOD = (
        "line_items,tracking_categories,contact,accounting_period"
    )
    TRACKING_CATEGORIES = "tracking_categories"
    TRACKING_CATEGORIES_ACCOUNT = "tracking_categories,account"
    TRACKING_CATEGORIES_ACCOUNT_ACCOUNTING_PERIOD = "tracking_categories,account,accounting_period"
    TRACKING_CATEGORIES_ACCOUNTING_PERIOD = "tracking_categories,accounting_period"
    TRACKING_CATEGORIES_CONTACT = "tracking_categories,contact"
    TRACKING_CATEGORIES_CONTACT_ACCOUNT = "tracking_categories,contact,account"
    TRACKING_CATEGORIES_CONTACT_ACCOUNT_ACCOUNTING_PERIOD = "tracking_categories,contact,account,accounting_period"
    TRACKING_CATEGORIES_CONTACT_ACCOUNTING_PERIOD = "tracking_categories,contact,accounting_period"

    def visit(
        self,
        account: typing.Callable[[], T_Result],
        account_accounting_period: typing.Callable[[], T_Result],
        accounting_period: typing.Callable[[], T_Result],
        contact: typing.Callable[[], T_Result],
        contact_account: typing.Callable[[], T_Result],
        contact_account_accounting_period: typing.Callable[[], T_Result],
        contact_accounting_period: typing.Callable[[], T_Result],
        line_items: typing.Callable[[], T_Result],
        line_items_account: typing.Callable[[], T_Result],
        line_items_account_accounting_period: typing.Callable[[], T_Result],
        line_items_accounting_period: typing.Callable[[], T_Result],
        line_items_contact: typing.Callable[[], T_Result],
        line_items_contact_account: typing.Callable[[], T_Result],
        line_items_contact_account_accounting_period: typing.Callable[[], T_Result],
        line_items_contact_accounting_period: typing.Callable[[], T_Result],
        line_items_tracking_categories: typing.Callable[[], T_Result],
        line_items_tracking_categories_account: typing.Callable[[], T_Result],
        line_items_tracking_categories_account_accounting_period: typing.Callable[[], T_Result],
        line_items_tracking_categories_accounting_period: typing.Callable[[], T_Result],
        line_items_tracking_categories_contact: typing.Callable[[], T_Result],
        line_items_tracking_categories_contact_account: typing.Callable[[], T_Result],
        line_items_tracking_categories_contact_account_accounting_period: typing.Callable[[], T_Result],
        line_items_tracking_categories_contact_accounting_period: typing.Callable[[], T_Result],
        tracking_categories: typing.Callable[[], T_Result],
        tracking_categories_account: typing.Callable[[], T_Result],
        tracking_categories_account_accounting_period: typing.Callable[[], T_Result],
        tracking_categories_accounting_period: typing.Callable[[], T_Result],
        tracking_categories_contact: typing.Callable[[], T_Result],
        tracking_categories_contact_account: typing.Callable[[], T_Result],
        tracking_categories_contact_account_accounting_period: typing.Callable[[], T_Result],
        tracking_categories_contact_accounting_period: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is TransactionsListRequestExpand.ACCOUNT:
            return account()
        if self is TransactionsListRequestExpand.ACCOUNT_ACCOUNTING_PERIOD:
            return account_accounting_period()
        if self is TransactionsListRequestExpand.ACCOUNTING_PERIOD:
            return accounting_period()
        if self is TransactionsListRequestExpand.CONTACT:
            return contact()
        if self is TransactionsListRequestExpand.CONTACT_ACCOUNT:
            return contact_account()
        if self is TransactionsListRequestExpand.CONTACT_ACCOUNT_ACCOUNTING_PERIOD:
            return contact_account_accounting_period()
        if self is TransactionsListRequestExpand.CONTACT_ACCOUNTING_PERIOD:
            return contact_accounting_period()
        if self is TransactionsListRequestExpand.LINE_ITEMS:
            return line_items()
        if self is TransactionsListRequestExpand.LINE_ITEMS_ACCOUNT:
            return line_items_account()
        if self is TransactionsListRequestExpand.LINE_ITEMS_ACCOUNT_ACCOUNTING_PERIOD:
            return line_items_account_accounting_period()
        if self is TransactionsListRequestExpand.LINE_ITEMS_ACCOUNTING_PERIOD:
            return line_items_accounting_period()
        if self is TransactionsListRequestExpand.LINE_ITEMS_CONTACT:
            return line_items_contact()
        if self is TransactionsListRequestExpand.LINE_ITEMS_CONTACT_ACCOUNT:
            return line_items_contact_account()
        if self is TransactionsListRequestExpand.LINE_ITEMS_CONTACT_ACCOUNT_ACCOUNTING_PERIOD:
            return line_items_contact_account_accounting_period()
        if self is TransactionsListRequestExpand.LINE_ITEMS_CONTACT_ACCOUNTING_PERIOD:
            return line_items_contact_accounting_period()
        if self is TransactionsListRequestExpand.LINE_ITEMS_TRACKING_CATEGORIES:
            return line_items_tracking_categories()
        if self is TransactionsListRequestExpand.LINE_ITEMS_TRACKING_CATEGORIES_ACCOUNT:
            return line_items_tracking_categories_account()
        if self is TransactionsListRequestExpand.LINE_ITEMS_TRACKING_CATEGORIES_ACCOUNT_ACCOUNTING_PERIOD:
            return line_items_tracking_categories_account_accounting_period()
        if self is TransactionsListRequestExpand.LINE_ITEMS_TRACKING_CATEGORIES_ACCOUNTING_PERIOD:
            return line_items_tracking_categories_accounting_period()
        if self is TransactionsListRequestExpand.LINE_ITEMS_TRACKING_CATEGORIES_CONTACT:
            return line_items_tracking_categories_contact()
        if self is TransactionsListRequestExpand.LINE_ITEMS_TRACKING_CATEGORIES_CONTACT_ACCOUNT:
            return line_items_tracking_categories_contact_account()
        if self is TransactionsListRequestExpand.LINE_ITEMS_TRACKING_CATEGORIES_CONTACT_ACCOUNT_ACCOUNTING_PERIOD:
            return line_items_tracking_categories_contact_account_accounting_period()
        if self is TransactionsListRequestExpand.LINE_ITEMS_TRACKING_CATEGORIES_CONTACT_ACCOUNTING_PERIOD:
            return line_items_tracking_categories_contact_accounting_period()
        if self is TransactionsListRequestExpand.TRACKING_CATEGORIES:
            return tracking_categories()
        if self is TransactionsListRequestExpand.TRACKING_CATEGORIES_ACCOUNT:
            return tracking_categories_account()
        if self is TransactionsListRequestExpand.TRACKING_CATEGORIES_ACCOUNT_ACCOUNTING_PERIOD:
            return tracking_categories_account_accounting_period()
        if self is TransactionsListRequestExpand.TRACKING_CATEGORIES_ACCOUNTING_PERIOD:
            return tracking_categories_accounting_period()
        if self is TransactionsListRequestExpand.TRACKING_CATEGORIES_CONTACT:
            return tracking_categories_contact()
        if self is TransactionsListRequestExpand.TRACKING_CATEGORIES_CONTACT_ACCOUNT:
            return tracking_categories_contact_account()
        if self is TransactionsListRequestExpand.TRACKING_CATEGORIES_CONTACT_ACCOUNT_ACCOUNTING_PERIOD:
            return tracking_categories_contact_account_accounting_period()
        if self is TransactionsListRequestExpand.TRACKING_CATEGORIES_CONTACT_ACCOUNTING_PERIOD:
            return tracking_categories_contact_accounting_period()