# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class CreditNotesRetrieveRequestExpand(str, enum.Enum):
    ACCOUNTING_PERIOD = "accounting_period"
    COMPANY = "company"
    COMPANY_ACCOUNTING_PERIOD = "company,accounting_period"
    CONTACT = "contact"
    CONTACT_ACCOUNTING_PERIOD = "contact,accounting_period"
    CONTACT_COMPANY = "contact,company"
    CONTACT_COMPANY_ACCOUNTING_PERIOD = "contact,company,accounting_period"
    LINE_ITEMS = "line_items"
    LINE_ITEMS_ACCOUNTING_PERIOD = "line_items,accounting_period"
    LINE_ITEMS_COMPANY = "line_items,company"
    LINE_ITEMS_COMPANY_ACCOUNTING_PERIOD = "line_items,company,accounting_period"
    LINE_ITEMS_CONTACT = "line_items,contact"
    LINE_ITEMS_CONTACT_ACCOUNTING_PERIOD = "line_items,contact,accounting_period"
    LINE_ITEMS_CONTACT_COMPANY = "line_items,contact,company"
    LINE_ITEMS_CONTACT_COMPANY_ACCOUNTING_PERIOD = "line_items,contact,company,accounting_period"
    LINE_ITEMS_TRACKING_CATEGORIES = "line_items,tracking_categories"
    LINE_ITEMS_TRACKING_CATEGORIES_ACCOUNTING_PERIOD = "line_items,tracking_categories,accounting_period"
    LINE_ITEMS_TRACKING_CATEGORIES_COMPANY = "line_items,tracking_categories,company"
    LINE_ITEMS_TRACKING_CATEGORIES_COMPANY_ACCOUNTING_PERIOD = (
        "line_items,tracking_categories,company,accounting_period"
    )
    LINE_ITEMS_TRACKING_CATEGORIES_CONTACT = "line_items,tracking_categories,contact"
    LINE_ITEMS_TRACKING_CATEGORIES_CONTACT_ACCOUNTING_PERIOD = (
        "line_items,tracking_categories,contact,accounting_period"
    )
    LINE_ITEMS_TRACKING_CATEGORIES_CONTACT_COMPANY = "line_items,tracking_categories,contact,company"
    LINE_ITEMS_TRACKING_CATEGORIES_CONTACT_COMPANY_ACCOUNTING_PERIOD = (
        "line_items,tracking_categories,contact,company,accounting_period"
    )
    PAYMENTS = "payments"
    PAYMENTS_ACCOUNTING_PERIOD = "payments,accounting_period"
    PAYMENTS_COMPANY = "payments,company"
    PAYMENTS_COMPANY_ACCOUNTING_PERIOD = "payments,company,accounting_period"
    PAYMENTS_CONTACT = "payments,contact"
    PAYMENTS_CONTACT_ACCOUNTING_PERIOD = "payments,contact,accounting_period"
    PAYMENTS_CONTACT_COMPANY = "payments,contact,company"
    PAYMENTS_CONTACT_COMPANY_ACCOUNTING_PERIOD = "payments,contact,company,accounting_period"
    PAYMENTS_LINE_ITEMS = "payments,line_items"
    PAYMENTS_LINE_ITEMS_ACCOUNTING_PERIOD = "payments,line_items,accounting_period"
    PAYMENTS_LINE_ITEMS_COMPANY = "payments,line_items,company"
    PAYMENTS_LINE_ITEMS_COMPANY_ACCOUNTING_PERIOD = "payments,line_items,company,accounting_period"
    PAYMENTS_LINE_ITEMS_CONTACT = "payments,line_items,contact"
    PAYMENTS_LINE_ITEMS_CONTACT_ACCOUNTING_PERIOD = "payments,line_items,contact,accounting_period"
    PAYMENTS_LINE_ITEMS_CONTACT_COMPANY = "payments,line_items,contact,company"
    PAYMENTS_LINE_ITEMS_CONTACT_COMPANY_ACCOUNTING_PERIOD = "payments,line_items,contact,company,accounting_period"
    PAYMENTS_LINE_ITEMS_TRACKING_CATEGORIES = "payments,line_items,tracking_categories"
    PAYMENTS_LINE_ITEMS_TRACKING_CATEGORIES_ACCOUNTING_PERIOD = (
        "payments,line_items,tracking_categories,accounting_period"
    )
    PAYMENTS_LINE_ITEMS_TRACKING_CATEGORIES_COMPANY = "payments,line_items,tracking_categories,company"
    PAYMENTS_LINE_ITEMS_TRACKING_CATEGORIES_COMPANY_ACCOUNTING_PERIOD = (
        "payments,line_items,tracking_categories,company,accounting_period"
    )
    PAYMENTS_LINE_ITEMS_TRACKING_CATEGORIES_CONTACT = "payments,line_items,tracking_categories,contact"
    PAYMENTS_LINE_ITEMS_TRACKING_CATEGORIES_CONTACT_ACCOUNTING_PERIOD = (
        "payments,line_items,tracking_categories,contact,accounting_period"
    )
    PAYMENTS_LINE_ITEMS_TRACKING_CATEGORIES_CONTACT_COMPANY = "payments,line_items,tracking_categories,contact,company"
    PAYMENTS_LINE_ITEMS_TRACKING_CATEGORIES_CONTACT_COMPANY_ACCOUNTING_PERIOD = (
        "payments,line_items,tracking_categories,contact,company,accounting_period"
    )
    PAYMENTS_TRACKING_CATEGORIES = "payments,tracking_categories"
    PAYMENTS_TRACKING_CATEGORIES_ACCOUNTING_PERIOD = "payments,tracking_categories,accounting_period"
    PAYMENTS_TRACKING_CATEGORIES_COMPANY = "payments,tracking_categories,company"
    PAYMENTS_TRACKING_CATEGORIES_COMPANY_ACCOUNTING_PERIOD = "payments,tracking_categories,company,accounting_period"
    PAYMENTS_TRACKING_CATEGORIES_CONTACT = "payments,tracking_categories,contact"
    PAYMENTS_TRACKING_CATEGORIES_CONTACT_ACCOUNTING_PERIOD = "payments,tracking_categories,contact,accounting_period"
    PAYMENTS_TRACKING_CATEGORIES_CONTACT_COMPANY = "payments,tracking_categories,contact,company"
    PAYMENTS_TRACKING_CATEGORIES_CONTACT_COMPANY_ACCOUNTING_PERIOD = (
        "payments,tracking_categories,contact,company,accounting_period"
    )
    TRACKING_CATEGORIES = "tracking_categories"
    TRACKING_CATEGORIES_ACCOUNTING_PERIOD = "tracking_categories,accounting_period"
    TRACKING_CATEGORIES_COMPANY = "tracking_categories,company"
    TRACKING_CATEGORIES_COMPANY_ACCOUNTING_PERIOD = "tracking_categories,company,accounting_period"
    TRACKING_CATEGORIES_CONTACT = "tracking_categories,contact"
    TRACKING_CATEGORIES_CONTACT_ACCOUNTING_PERIOD = "tracking_categories,contact,accounting_period"
    TRACKING_CATEGORIES_CONTACT_COMPANY = "tracking_categories,contact,company"
    TRACKING_CATEGORIES_CONTACT_COMPANY_ACCOUNTING_PERIOD = "tracking_categories,contact,company,accounting_period"

    def visit(
        self,
        accounting_period: typing.Callable[[], T_Result],
        company: typing.Callable[[], T_Result],
        company_accounting_period: typing.Callable[[], T_Result],
        contact: typing.Callable[[], T_Result],
        contact_accounting_period: typing.Callable[[], T_Result],
        contact_company: typing.Callable[[], T_Result],
        contact_company_accounting_period: typing.Callable[[], T_Result],
        line_items: typing.Callable[[], T_Result],
        line_items_accounting_period: typing.Callable[[], T_Result],
        line_items_company: typing.Callable[[], T_Result],
        line_items_company_accounting_period: typing.Callable[[], T_Result],
        line_items_contact: typing.Callable[[], T_Result],
        line_items_contact_accounting_period: typing.Callable[[], T_Result],
        line_items_contact_company: typing.Callable[[], T_Result],
        line_items_contact_company_accounting_period: typing.Callable[[], T_Result],
        line_items_tracking_categories: typing.Callable[[], T_Result],
        line_items_tracking_categories_accounting_period: typing.Callable[[], T_Result],
        line_items_tracking_categories_company: typing.Callable[[], T_Result],
        line_items_tracking_categories_company_accounting_period: typing.Callable[[], T_Result],
        line_items_tracking_categories_contact: typing.Callable[[], T_Result],
        line_items_tracking_categories_contact_accounting_period: typing.Callable[[], T_Result],
        line_items_tracking_categories_contact_company: typing.Callable[[], T_Result],
        line_items_tracking_categories_contact_company_accounting_period: typing.Callable[[], T_Result],
        payments: typing.Callable[[], T_Result],
        payments_accounting_period: typing.Callable[[], T_Result],
        payments_company: typing.Callable[[], T_Result],
        payments_company_accounting_period: typing.Callable[[], T_Result],
        payments_contact: typing.Callable[[], T_Result],
        payments_contact_accounting_period: typing.Callable[[], T_Result],
        payments_contact_company: typing.Callable[[], T_Result],
        payments_contact_company_accounting_period: typing.Callable[[], T_Result],
        payments_line_items: typing.Callable[[], T_Result],
        payments_line_items_accounting_period: typing.Callable[[], T_Result],
        payments_line_items_company: typing.Callable[[], T_Result],
        payments_line_items_company_accounting_period: typing.Callable[[], T_Result],
        payments_line_items_contact: typing.Callable[[], T_Result],
        payments_line_items_contact_accounting_period: typing.Callable[[], T_Result],
        payments_line_items_contact_company: typing.Callable[[], T_Result],
        payments_line_items_contact_company_accounting_period: typing.Callable[[], T_Result],
        payments_line_items_tracking_categories: typing.Callable[[], T_Result],
        payments_line_items_tracking_categories_accounting_period: typing.Callable[[], T_Result],
        payments_line_items_tracking_categories_company: typing.Callable[[], T_Result],
        payments_line_items_tracking_categories_company_accounting_period: typing.Callable[[], T_Result],
        payments_line_items_tracking_categories_contact: typing.Callable[[], T_Result],
        payments_line_items_tracking_categories_contact_accounting_period: typing.Callable[[], T_Result],
        payments_line_items_tracking_categories_contact_company: typing.Callable[[], T_Result],
        payments_line_items_tracking_categories_contact_company_accounting_period: typing.Callable[[], T_Result],
        payments_tracking_categories: typing.Callable[[], T_Result],
        payments_tracking_categories_accounting_period: typing.Callable[[], T_Result],
        payments_tracking_categories_company: typing.Callable[[], T_Result],
        payments_tracking_categories_company_accounting_period: typing.Callable[[], T_Result],
        payments_tracking_categories_contact: typing.Callable[[], T_Result],
        payments_tracking_categories_contact_accounting_period: typing.Callable[[], T_Result],
        payments_tracking_categories_contact_company: typing.Callable[[], T_Result],
        payments_tracking_categories_contact_company_accounting_period: typing.Callable[[], T_Result],
        tracking_categories: typing.Callable[[], T_Result],
        tracking_categories_accounting_period: typing.Callable[[], T_Result],
        tracking_categories_company: typing.Callable[[], T_Result],
        tracking_categories_company_accounting_period: typing.Callable[[], T_Result],
        tracking_categories_contact: typing.Callable[[], T_Result],
        tracking_categories_contact_accounting_period: typing.Callable[[], T_Result],
        tracking_categories_contact_company: typing.Callable[[], T_Result],
        tracking_categories_contact_company_accounting_period: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is CreditNotesRetrieveRequestExpand.ACCOUNTING_PERIOD:
            return accounting_period()
        if self is CreditNotesRetrieveRequestExpand.COMPANY:
            return company()
        if self is CreditNotesRetrieveRequestExpand.COMPANY_ACCOUNTING_PERIOD:
            return company_accounting_period()
        if self is CreditNotesRetrieveRequestExpand.CONTACT:
            return contact()
        if self is CreditNotesRetrieveRequestExpand.CONTACT_ACCOUNTING_PERIOD:
            return contact_accounting_period()
        if self is CreditNotesRetrieveRequestExpand.CONTACT_COMPANY:
            return contact_company()
        if self is CreditNotesRetrieveRequestExpand.CONTACT_COMPANY_ACCOUNTING_PERIOD:
            return contact_company_accounting_period()
        if self is CreditNotesRetrieveRequestExpand.LINE_ITEMS:
            return line_items()
        if self is CreditNotesRetrieveRequestExpand.LINE_ITEMS_ACCOUNTING_PERIOD:
            return line_items_accounting_period()
        if self is CreditNotesRetrieveRequestExpand.LINE_ITEMS_COMPANY:
            return line_items_company()
        if self is CreditNotesRetrieveRequestExpand.LINE_ITEMS_COMPANY_ACCOUNTING_PERIOD:
            return line_items_company_accounting_period()
        if self is CreditNotesRetrieveRequestExpand.LINE_ITEMS_CONTACT:
            return line_items_contact()
        if self is CreditNotesRetrieveRequestExpand.LINE_ITEMS_CONTACT_ACCOUNTING_PERIOD:
            return line_items_contact_accounting_period()
        if self is CreditNotesRetrieveRequestExpand.LINE_ITEMS_CONTACT_COMPANY:
            return line_items_contact_company()
        if self is CreditNotesRetrieveRequestExpand.LINE_ITEMS_CONTACT_COMPANY_ACCOUNTING_PERIOD:
            return line_items_contact_company_accounting_period()
        if self is CreditNotesRetrieveRequestExpand.LINE_ITEMS_TRACKING_CATEGORIES:
            return line_items_tracking_categories()
        if self is CreditNotesRetrieveRequestExpand.LINE_ITEMS_TRACKING_CATEGORIES_ACCOUNTING_PERIOD:
            return line_items_tracking_categories_accounting_period()
        if self is CreditNotesRetrieveRequestExpand.LINE_ITEMS_TRACKING_CATEGORIES_COMPANY:
            return line_items_tracking_categories_company()
        if self is CreditNotesRetrieveRequestExpand.LINE_ITEMS_TRACKING_CATEGORIES_COMPANY_ACCOUNTING_PERIOD:
            return line_items_tracking_categories_company_accounting_period()
        if self is CreditNotesRetrieveRequestExpand.LINE_ITEMS_TRACKING_CATEGORIES_CONTACT:
            return line_items_tracking_categories_contact()
        if self is CreditNotesRetrieveRequestExpand.LINE_ITEMS_TRACKING_CATEGORIES_CONTACT_ACCOUNTING_PERIOD:
            return line_items_tracking_categories_contact_accounting_period()
        if self is CreditNotesRetrieveRequestExpand.LINE_ITEMS_TRACKING_CATEGORIES_CONTACT_COMPANY:
            return line_items_tracking_categories_contact_company()
        if self is CreditNotesRetrieveRequestExpand.LINE_ITEMS_TRACKING_CATEGORIES_CONTACT_COMPANY_ACCOUNTING_PERIOD:
            return line_items_tracking_categories_contact_company_accounting_period()
        if self is CreditNotesRetrieveRequestExpand.PAYMENTS:
            return payments()
        if self is CreditNotesRetrieveRequestExpand.PAYMENTS_ACCOUNTING_PERIOD:
            return payments_accounting_period()
        if self is CreditNotesRetrieveRequestExpand.PAYMENTS_COMPANY:
            return payments_company()
        if self is CreditNotesRetrieveRequestExpand.PAYMENTS_COMPANY_ACCOUNTING_PERIOD:
            return payments_company_accounting_period()
        if self is CreditNotesRetrieveRequestExpand.PAYMENTS_CONTACT:
            return payments_contact()
        if self is CreditNotesRetrieveRequestExpand.PAYMENTS_CONTACT_ACCOUNTING_PERIOD:
            return payments_contact_accounting_period()
        if self is CreditNotesRetrieveRequestExpand.PAYMENTS_CONTACT_COMPANY:
            return payments_contact_company()
        if self is CreditNotesRetrieveRequestExpand.PAYMENTS_CONTACT_COMPANY_ACCOUNTING_PERIOD:
            return payments_contact_company_accounting_period()
        if self is CreditNotesRetrieveRequestExpand.PAYMENTS_LINE_ITEMS:
            return payments_line_items()
        if self is CreditNotesRetrieveRequestExpand.PAYMENTS_LINE_ITEMS_ACCOUNTING_PERIOD:
            return payments_line_items_accounting_period()
        if self is CreditNotesRetrieveRequestExpand.PAYMENTS_LINE_ITEMS_COMPANY:
            return payments_line_items_company()
        if self is CreditNotesRetrieveRequestExpand.PAYMENTS_LINE_ITEMS_COMPANY_ACCOUNTING_PERIOD:
            return payments_line_items_company_accounting_period()
        if self is CreditNotesRetrieveRequestExpand.PAYMENTS_LINE_ITEMS_CONTACT:
            return payments_line_items_contact()
        if self is CreditNotesRetrieveRequestExpand.PAYMENTS_LINE_ITEMS_CONTACT_ACCOUNTING_PERIOD:
            return payments_line_items_contact_accounting_period()
        if self is CreditNotesRetrieveRequestExpand.PAYMENTS_LINE_ITEMS_CONTACT_COMPANY:
            return payments_line_items_contact_company()
        if self is CreditNotesRetrieveRequestExpand.PAYMENTS_LINE_ITEMS_CONTACT_COMPANY_ACCOUNTING_PERIOD:
            return payments_line_items_contact_company_accounting_period()
        if self is CreditNotesRetrieveRequestExpand.PAYMENTS_LINE_ITEMS_TRACKING_CATEGORIES:
            return payments_line_items_tracking_categories()
        if self is CreditNotesRetrieveRequestExpand.PAYMENTS_LINE_ITEMS_TRACKING_CATEGORIES_ACCOUNTING_PERIOD:
            return payments_line_items_tracking_categories_accounting_period()
        if self is CreditNotesRetrieveRequestExpand.PAYMENTS_LINE_ITEMS_TRACKING_CATEGORIES_COMPANY:
            return payments_line_items_tracking_categories_company()
        if self is CreditNotesRetrieveRequestExpand.PAYMENTS_LINE_ITEMS_TRACKING_CATEGORIES_COMPANY_ACCOUNTING_PERIOD:
            return payments_line_items_tracking_categories_company_accounting_period()
        if self is CreditNotesRetrieveRequestExpand.PAYMENTS_LINE_ITEMS_TRACKING_CATEGORIES_CONTACT:
            return payments_line_items_tracking_categories_contact()
        if self is CreditNotesRetrieveRequestExpand.PAYMENTS_LINE_ITEMS_TRACKING_CATEGORIES_CONTACT_ACCOUNTING_PERIOD:
            return payments_line_items_tracking_categories_contact_accounting_period()
        if self is CreditNotesRetrieveRequestExpand.PAYMENTS_LINE_ITEMS_TRACKING_CATEGORIES_CONTACT_COMPANY:
            return payments_line_items_tracking_categories_contact_company()
        if (
            self
            is CreditNotesRetrieveRequestExpand.PAYMENTS_LINE_ITEMS_TRACKING_CATEGORIES_CONTACT_COMPANY_ACCOUNTING_PERIOD
        ):
            return payments_line_items_tracking_categories_contact_company_accounting_period()
        if self is CreditNotesRetrieveRequestExpand.PAYMENTS_TRACKING_CATEGORIES:
            return payments_tracking_categories()
        if self is CreditNotesRetrieveRequestExpand.PAYMENTS_TRACKING_CATEGORIES_ACCOUNTING_PERIOD:
            return payments_tracking_categories_accounting_period()
        if self is CreditNotesRetrieveRequestExpand.PAYMENTS_TRACKING_CATEGORIES_COMPANY:
            return payments_tracking_categories_company()
        if self is CreditNotesRetrieveRequestExpand.PAYMENTS_TRACKING_CATEGORIES_COMPANY_ACCOUNTING_PERIOD:
            return payments_tracking_categories_company_accounting_period()
        if self is CreditNotesRetrieveRequestExpand.PAYMENTS_TRACKING_CATEGORIES_CONTACT:
            return payments_tracking_categories_contact()
        if self is CreditNotesRetrieveRequestExpand.PAYMENTS_TRACKING_CATEGORIES_CONTACT_ACCOUNTING_PERIOD:
            return payments_tracking_categories_contact_accounting_period()
        if self is CreditNotesRetrieveRequestExpand.PAYMENTS_TRACKING_CATEGORIES_CONTACT_COMPANY:
            return payments_tracking_categories_contact_company()
        if self is CreditNotesRetrieveRequestExpand.PAYMENTS_TRACKING_CATEGORIES_CONTACT_COMPANY_ACCOUNTING_PERIOD:
            return payments_tracking_categories_contact_company_accounting_period()
        if self is CreditNotesRetrieveRequestExpand.TRACKING_CATEGORIES:
            return tracking_categories()
        if self is CreditNotesRetrieveRequestExpand.TRACKING_CATEGORIES_ACCOUNTING_PERIOD:
            return tracking_categories_accounting_period()
        if self is CreditNotesRetrieveRequestExpand.TRACKING_CATEGORIES_COMPANY:
            return tracking_categories_company()
        if self is CreditNotesRetrieveRequestExpand.TRACKING_CATEGORIES_COMPANY_ACCOUNTING_PERIOD:
            return tracking_categories_company_accounting_period()
        if self is CreditNotesRetrieveRequestExpand.TRACKING_CATEGORIES_CONTACT:
            return tracking_categories_contact()
        if self is CreditNotesRetrieveRequestExpand.TRACKING_CATEGORIES_CONTACT_ACCOUNTING_PERIOD:
            return tracking_categories_contact_accounting_period()
        if self is CreditNotesRetrieveRequestExpand.TRACKING_CATEGORIES_CONTACT_COMPANY:
            return tracking_categories_contact_company()
        if self is CreditNotesRetrieveRequestExpand.TRACKING_CATEGORIES_CONTACT_COMPANY_ACCOUNTING_PERIOD:
            return tracking_categories_contact_company_accounting_period()
