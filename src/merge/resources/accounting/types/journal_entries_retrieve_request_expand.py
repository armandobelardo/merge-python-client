# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class JournalEntriesRetrieveRequestExpand(str, enum.Enum):
    ACCOUNTING_PERIOD = "accounting_period"
    APPLIED_PAYMENTS = "applied_payments"
    APPLIED_PAYMENTS_ACCOUNTING_PERIOD = "applied_payments,accounting_period"
    APPLIED_PAYMENTS_COMPANY = "applied_payments,company"
    APPLIED_PAYMENTS_COMPANY_ACCOUNTING_PERIOD = "applied_payments,company,accounting_period"
    APPLIED_PAYMENTS_TRACKING_CATEGORIES = "applied_payments,tracking_categories"
    APPLIED_PAYMENTS_TRACKING_CATEGORIES_ACCOUNTING_PERIOD = "applied_payments,tracking_categories,accounting_period"
    APPLIED_PAYMENTS_TRACKING_CATEGORIES_COMPANY = "applied_payments,tracking_categories,company"
    APPLIED_PAYMENTS_TRACKING_CATEGORIES_COMPANY_ACCOUNTING_PERIOD = (
        "applied_payments,tracking_categories,company,accounting_period"
    )
    COMPANY = "company"
    COMPANY_ACCOUNTING_PERIOD = "company,accounting_period"
    LINES = "lines"
    LINES_ACCOUNTING_PERIOD = "lines,accounting_period"
    LINES_APPLIED_PAYMENTS = "lines,applied_payments"
    LINES_APPLIED_PAYMENTS_ACCOUNTING_PERIOD = "lines,applied_payments,accounting_period"
    LINES_APPLIED_PAYMENTS_COMPANY = "lines,applied_payments,company"
    LINES_APPLIED_PAYMENTS_COMPANY_ACCOUNTING_PERIOD = "lines,applied_payments,company,accounting_period"
    LINES_APPLIED_PAYMENTS_TRACKING_CATEGORIES = "lines,applied_payments,tracking_categories"
    LINES_APPLIED_PAYMENTS_TRACKING_CATEGORIES_ACCOUNTING_PERIOD = (
        "lines,applied_payments,tracking_categories,accounting_period"
    )
    LINES_APPLIED_PAYMENTS_TRACKING_CATEGORIES_COMPANY = "lines,applied_payments,tracking_categories,company"
    LINES_APPLIED_PAYMENTS_TRACKING_CATEGORIES_COMPANY_ACCOUNTING_PERIOD = (
        "lines,applied_payments,tracking_categories,company,accounting_period"
    )
    LINES_COMPANY = "lines,company"
    LINES_COMPANY_ACCOUNTING_PERIOD = "lines,company,accounting_period"
    LINES_PAYMENTS = "lines,payments"
    LINES_PAYMENTS_ACCOUNTING_PERIOD = "lines,payments,accounting_period"
    LINES_PAYMENTS_APPLIED_PAYMENTS = "lines,payments,applied_payments"
    LINES_PAYMENTS_APPLIED_PAYMENTS_ACCOUNTING_PERIOD = "lines,payments,applied_payments,accounting_period"
    LINES_PAYMENTS_APPLIED_PAYMENTS_COMPANY = "lines,payments,applied_payments,company"
    LINES_PAYMENTS_APPLIED_PAYMENTS_COMPANY_ACCOUNTING_PERIOD = (
        "lines,payments,applied_payments,company,accounting_period"
    )
    LINES_PAYMENTS_APPLIED_PAYMENTS_TRACKING_CATEGORIES = "lines,payments,applied_payments,tracking_categories"
    LINES_PAYMENTS_APPLIED_PAYMENTS_TRACKING_CATEGORIES_ACCOUNTING_PERIOD = (
        "lines,payments,applied_payments,tracking_categories,accounting_period"
    )
    LINES_PAYMENTS_APPLIED_PAYMENTS_TRACKING_CATEGORIES_COMPANY = (
        "lines,payments,applied_payments,tracking_categories,company"
    )
    LINES_PAYMENTS_APPLIED_PAYMENTS_TRACKING_CATEGORIES_COMPANY_ACCOUNTING_PERIOD = (
        "lines,payments,applied_payments,tracking_categories,company,accounting_period"
    )
    LINES_PAYMENTS_COMPANY = "lines,payments,company"
    LINES_PAYMENTS_COMPANY_ACCOUNTING_PERIOD = "lines,payments,company,accounting_period"
    LINES_PAYMENTS_TRACKING_CATEGORIES = "lines,payments,tracking_categories"
    LINES_PAYMENTS_TRACKING_CATEGORIES_ACCOUNTING_PERIOD = "lines,payments,tracking_categories,accounting_period"
    LINES_PAYMENTS_TRACKING_CATEGORIES_COMPANY = "lines,payments,tracking_categories,company"
    LINES_PAYMENTS_TRACKING_CATEGORIES_COMPANY_ACCOUNTING_PERIOD = (
        "lines,payments,tracking_categories,company,accounting_period"
    )
    LINES_TRACKING_CATEGORIES = "lines,tracking_categories"
    LINES_TRACKING_CATEGORIES_ACCOUNTING_PERIOD = "lines,tracking_categories,accounting_period"
    LINES_TRACKING_CATEGORIES_COMPANY = "lines,tracking_categories,company"
    LINES_TRACKING_CATEGORIES_COMPANY_ACCOUNTING_PERIOD = "lines,tracking_categories,company,accounting_period"
    PAYMENTS = "payments"
    PAYMENTS_ACCOUNTING_PERIOD = "payments,accounting_period"
    PAYMENTS_APPLIED_PAYMENTS = "payments,applied_payments"
    PAYMENTS_APPLIED_PAYMENTS_ACCOUNTING_PERIOD = "payments,applied_payments,accounting_period"
    PAYMENTS_APPLIED_PAYMENTS_COMPANY = "payments,applied_payments,company"
    PAYMENTS_APPLIED_PAYMENTS_COMPANY_ACCOUNTING_PERIOD = "payments,applied_payments,company,accounting_period"
    PAYMENTS_APPLIED_PAYMENTS_TRACKING_CATEGORIES = "payments,applied_payments,tracking_categories"
    PAYMENTS_APPLIED_PAYMENTS_TRACKING_CATEGORIES_ACCOUNTING_PERIOD = (
        "payments,applied_payments,tracking_categories,accounting_period"
    )
    PAYMENTS_APPLIED_PAYMENTS_TRACKING_CATEGORIES_COMPANY = "payments,applied_payments,tracking_categories,company"
    PAYMENTS_APPLIED_PAYMENTS_TRACKING_CATEGORIES_COMPANY_ACCOUNTING_PERIOD = (
        "payments,applied_payments,tracking_categories,company,accounting_period"
    )
    PAYMENTS_COMPANY = "payments,company"
    PAYMENTS_COMPANY_ACCOUNTING_PERIOD = "payments,company,accounting_period"
    PAYMENTS_TRACKING_CATEGORIES = "payments,tracking_categories"
    PAYMENTS_TRACKING_CATEGORIES_ACCOUNTING_PERIOD = "payments,tracking_categories,accounting_period"
    PAYMENTS_TRACKING_CATEGORIES_COMPANY = "payments,tracking_categories,company"
    PAYMENTS_TRACKING_CATEGORIES_COMPANY_ACCOUNTING_PERIOD = "payments,tracking_categories,company,accounting_period"
    TRACKING_CATEGORIES = "tracking_categories"
    TRACKING_CATEGORIES_ACCOUNTING_PERIOD = "tracking_categories,accounting_period"
    TRACKING_CATEGORIES_COMPANY = "tracking_categories,company"
    TRACKING_CATEGORIES_COMPANY_ACCOUNTING_PERIOD = "tracking_categories,company,accounting_period"

    def visit(
        self,
        accounting_period: typing.Callable[[], T_Result],
        applied_payments: typing.Callable[[], T_Result],
        applied_payments_accounting_period: typing.Callable[[], T_Result],
        applied_payments_company: typing.Callable[[], T_Result],
        applied_payments_company_accounting_period: typing.Callable[[], T_Result],
        applied_payments_tracking_categories: typing.Callable[[], T_Result],
        applied_payments_tracking_categories_accounting_period: typing.Callable[[], T_Result],
        applied_payments_tracking_categories_company: typing.Callable[[], T_Result],
        applied_payments_tracking_categories_company_accounting_period: typing.Callable[[], T_Result],
        company: typing.Callable[[], T_Result],
        company_accounting_period: typing.Callable[[], T_Result],
        lines: typing.Callable[[], T_Result],
        lines_accounting_period: typing.Callable[[], T_Result],
        lines_applied_payments: typing.Callable[[], T_Result],
        lines_applied_payments_accounting_period: typing.Callable[[], T_Result],
        lines_applied_payments_company: typing.Callable[[], T_Result],
        lines_applied_payments_company_accounting_period: typing.Callable[[], T_Result],
        lines_applied_payments_tracking_categories: typing.Callable[[], T_Result],
        lines_applied_payments_tracking_categories_accounting_period: typing.Callable[[], T_Result],
        lines_applied_payments_tracking_categories_company: typing.Callable[[], T_Result],
        lines_applied_payments_tracking_categories_company_accounting_period: typing.Callable[[], T_Result],
        lines_company: typing.Callable[[], T_Result],
        lines_company_accounting_period: typing.Callable[[], T_Result],
        lines_payments: typing.Callable[[], T_Result],
        lines_payments_accounting_period: typing.Callable[[], T_Result],
        lines_payments_applied_payments: typing.Callable[[], T_Result],
        lines_payments_applied_payments_accounting_period: typing.Callable[[], T_Result],
        lines_payments_applied_payments_company: typing.Callable[[], T_Result],
        lines_payments_applied_payments_company_accounting_period: typing.Callable[[], T_Result],
        lines_payments_applied_payments_tracking_categories: typing.Callable[[], T_Result],
        lines_payments_applied_payments_tracking_categories_accounting_period: typing.Callable[[], T_Result],
        lines_payments_applied_payments_tracking_categories_company: typing.Callable[[], T_Result],
        lines_payments_applied_payments_tracking_categories_company_accounting_period: typing.Callable[[], T_Result],
        lines_payments_company: typing.Callable[[], T_Result],
        lines_payments_company_accounting_period: typing.Callable[[], T_Result],
        lines_payments_tracking_categories: typing.Callable[[], T_Result],
        lines_payments_tracking_categories_accounting_period: typing.Callable[[], T_Result],
        lines_payments_tracking_categories_company: typing.Callable[[], T_Result],
        lines_payments_tracking_categories_company_accounting_period: typing.Callable[[], T_Result],
        lines_tracking_categories: typing.Callable[[], T_Result],
        lines_tracking_categories_accounting_period: typing.Callable[[], T_Result],
        lines_tracking_categories_company: typing.Callable[[], T_Result],
        lines_tracking_categories_company_accounting_period: typing.Callable[[], T_Result],
        payments: typing.Callable[[], T_Result],
        payments_accounting_period: typing.Callable[[], T_Result],
        payments_applied_payments: typing.Callable[[], T_Result],
        payments_applied_payments_accounting_period: typing.Callable[[], T_Result],
        payments_applied_payments_company: typing.Callable[[], T_Result],
        payments_applied_payments_company_accounting_period: typing.Callable[[], T_Result],
        payments_applied_payments_tracking_categories: typing.Callable[[], T_Result],
        payments_applied_payments_tracking_categories_accounting_period: typing.Callable[[], T_Result],
        payments_applied_payments_tracking_categories_company: typing.Callable[[], T_Result],
        payments_applied_payments_tracking_categories_company_accounting_period: typing.Callable[[], T_Result],
        payments_company: typing.Callable[[], T_Result],
        payments_company_accounting_period: typing.Callable[[], T_Result],
        payments_tracking_categories: typing.Callable[[], T_Result],
        payments_tracking_categories_accounting_period: typing.Callable[[], T_Result],
        payments_tracking_categories_company: typing.Callable[[], T_Result],
        payments_tracking_categories_company_accounting_period: typing.Callable[[], T_Result],
        tracking_categories: typing.Callable[[], T_Result],
        tracking_categories_accounting_period: typing.Callable[[], T_Result],
        tracking_categories_company: typing.Callable[[], T_Result],
        tracking_categories_company_accounting_period: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is JournalEntriesRetrieveRequestExpand.ACCOUNTING_PERIOD:
            return accounting_period()
        if self is JournalEntriesRetrieveRequestExpand.APPLIED_PAYMENTS:
            return applied_payments()
        if self is JournalEntriesRetrieveRequestExpand.APPLIED_PAYMENTS_ACCOUNTING_PERIOD:
            return applied_payments_accounting_period()
        if self is JournalEntriesRetrieveRequestExpand.APPLIED_PAYMENTS_COMPANY:
            return applied_payments_company()
        if self is JournalEntriesRetrieveRequestExpand.APPLIED_PAYMENTS_COMPANY_ACCOUNTING_PERIOD:
            return applied_payments_company_accounting_period()
        if self is JournalEntriesRetrieveRequestExpand.APPLIED_PAYMENTS_TRACKING_CATEGORIES:
            return applied_payments_tracking_categories()
        if self is JournalEntriesRetrieveRequestExpand.APPLIED_PAYMENTS_TRACKING_CATEGORIES_ACCOUNTING_PERIOD:
            return applied_payments_tracking_categories_accounting_period()
        if self is JournalEntriesRetrieveRequestExpand.APPLIED_PAYMENTS_TRACKING_CATEGORIES_COMPANY:
            return applied_payments_tracking_categories_company()
        if self is JournalEntriesRetrieveRequestExpand.APPLIED_PAYMENTS_TRACKING_CATEGORIES_COMPANY_ACCOUNTING_PERIOD:
            return applied_payments_tracking_categories_company_accounting_period()
        if self is JournalEntriesRetrieveRequestExpand.COMPANY:
            return company()
        if self is JournalEntriesRetrieveRequestExpand.COMPANY_ACCOUNTING_PERIOD:
            return company_accounting_period()
        if self is JournalEntriesRetrieveRequestExpand.LINES:
            return lines()
        if self is JournalEntriesRetrieveRequestExpand.LINES_ACCOUNTING_PERIOD:
            return lines_accounting_period()
        if self is JournalEntriesRetrieveRequestExpand.LINES_APPLIED_PAYMENTS:
            return lines_applied_payments()
        if self is JournalEntriesRetrieveRequestExpand.LINES_APPLIED_PAYMENTS_ACCOUNTING_PERIOD:
            return lines_applied_payments_accounting_period()
        if self is JournalEntriesRetrieveRequestExpand.LINES_APPLIED_PAYMENTS_COMPANY:
            return lines_applied_payments_company()
        if self is JournalEntriesRetrieveRequestExpand.LINES_APPLIED_PAYMENTS_COMPANY_ACCOUNTING_PERIOD:
            return lines_applied_payments_company_accounting_period()
        if self is JournalEntriesRetrieveRequestExpand.LINES_APPLIED_PAYMENTS_TRACKING_CATEGORIES:
            return lines_applied_payments_tracking_categories()
        if self is JournalEntriesRetrieveRequestExpand.LINES_APPLIED_PAYMENTS_TRACKING_CATEGORIES_ACCOUNTING_PERIOD:
            return lines_applied_payments_tracking_categories_accounting_period()
        if self is JournalEntriesRetrieveRequestExpand.LINES_APPLIED_PAYMENTS_TRACKING_CATEGORIES_COMPANY:
            return lines_applied_payments_tracking_categories_company()
        if (
            self
            is JournalEntriesRetrieveRequestExpand.LINES_APPLIED_PAYMENTS_TRACKING_CATEGORIES_COMPANY_ACCOUNTING_PERIOD
        ):
            return lines_applied_payments_tracking_categories_company_accounting_period()
        if self is JournalEntriesRetrieveRequestExpand.LINES_COMPANY:
            return lines_company()
        if self is JournalEntriesRetrieveRequestExpand.LINES_COMPANY_ACCOUNTING_PERIOD:
            return lines_company_accounting_period()
        if self is JournalEntriesRetrieveRequestExpand.LINES_PAYMENTS:
            return lines_payments()
        if self is JournalEntriesRetrieveRequestExpand.LINES_PAYMENTS_ACCOUNTING_PERIOD:
            return lines_payments_accounting_period()
        if self is JournalEntriesRetrieveRequestExpand.LINES_PAYMENTS_APPLIED_PAYMENTS:
            return lines_payments_applied_payments()
        if self is JournalEntriesRetrieveRequestExpand.LINES_PAYMENTS_APPLIED_PAYMENTS_ACCOUNTING_PERIOD:
            return lines_payments_applied_payments_accounting_period()
        if self is JournalEntriesRetrieveRequestExpand.LINES_PAYMENTS_APPLIED_PAYMENTS_COMPANY:
            return lines_payments_applied_payments_company()
        if self is JournalEntriesRetrieveRequestExpand.LINES_PAYMENTS_APPLIED_PAYMENTS_COMPANY_ACCOUNTING_PERIOD:
            return lines_payments_applied_payments_company_accounting_period()
        if self is JournalEntriesRetrieveRequestExpand.LINES_PAYMENTS_APPLIED_PAYMENTS_TRACKING_CATEGORIES:
            return lines_payments_applied_payments_tracking_categories()
        if (
            self
            is JournalEntriesRetrieveRequestExpand.LINES_PAYMENTS_APPLIED_PAYMENTS_TRACKING_CATEGORIES_ACCOUNTING_PERIOD
        ):
            return lines_payments_applied_payments_tracking_categories_accounting_period()
        if self is JournalEntriesRetrieveRequestExpand.LINES_PAYMENTS_APPLIED_PAYMENTS_TRACKING_CATEGORIES_COMPANY:
            return lines_payments_applied_payments_tracking_categories_company()
        if (
            self
            is JournalEntriesRetrieveRequestExpand.LINES_PAYMENTS_APPLIED_PAYMENTS_TRACKING_CATEGORIES_COMPANY_ACCOUNTING_PERIOD
        ):
            return lines_payments_applied_payments_tracking_categories_company_accounting_period()
        if self is JournalEntriesRetrieveRequestExpand.LINES_PAYMENTS_COMPANY:
            return lines_payments_company()
        if self is JournalEntriesRetrieveRequestExpand.LINES_PAYMENTS_COMPANY_ACCOUNTING_PERIOD:
            return lines_payments_company_accounting_period()
        if self is JournalEntriesRetrieveRequestExpand.LINES_PAYMENTS_TRACKING_CATEGORIES:
            return lines_payments_tracking_categories()
        if self is JournalEntriesRetrieveRequestExpand.LINES_PAYMENTS_TRACKING_CATEGORIES_ACCOUNTING_PERIOD:
            return lines_payments_tracking_categories_accounting_period()
        if self is JournalEntriesRetrieveRequestExpand.LINES_PAYMENTS_TRACKING_CATEGORIES_COMPANY:
            return lines_payments_tracking_categories_company()
        if self is JournalEntriesRetrieveRequestExpand.LINES_PAYMENTS_TRACKING_CATEGORIES_COMPANY_ACCOUNTING_PERIOD:
            return lines_payments_tracking_categories_company_accounting_period()
        if self is JournalEntriesRetrieveRequestExpand.LINES_TRACKING_CATEGORIES:
            return lines_tracking_categories()
        if self is JournalEntriesRetrieveRequestExpand.LINES_TRACKING_CATEGORIES_ACCOUNTING_PERIOD:
            return lines_tracking_categories_accounting_period()
        if self is JournalEntriesRetrieveRequestExpand.LINES_TRACKING_CATEGORIES_COMPANY:
            return lines_tracking_categories_company()
        if self is JournalEntriesRetrieveRequestExpand.LINES_TRACKING_CATEGORIES_COMPANY_ACCOUNTING_PERIOD:
            return lines_tracking_categories_company_accounting_period()
        if self is JournalEntriesRetrieveRequestExpand.PAYMENTS:
            return payments()
        if self is JournalEntriesRetrieveRequestExpand.PAYMENTS_ACCOUNTING_PERIOD:
            return payments_accounting_period()
        if self is JournalEntriesRetrieveRequestExpand.PAYMENTS_APPLIED_PAYMENTS:
            return payments_applied_payments()
        if self is JournalEntriesRetrieveRequestExpand.PAYMENTS_APPLIED_PAYMENTS_ACCOUNTING_PERIOD:
            return payments_applied_payments_accounting_period()
        if self is JournalEntriesRetrieveRequestExpand.PAYMENTS_APPLIED_PAYMENTS_COMPANY:
            return payments_applied_payments_company()
        if self is JournalEntriesRetrieveRequestExpand.PAYMENTS_APPLIED_PAYMENTS_COMPANY_ACCOUNTING_PERIOD:
            return payments_applied_payments_company_accounting_period()
        if self is JournalEntriesRetrieveRequestExpand.PAYMENTS_APPLIED_PAYMENTS_TRACKING_CATEGORIES:
            return payments_applied_payments_tracking_categories()
        if self is JournalEntriesRetrieveRequestExpand.PAYMENTS_APPLIED_PAYMENTS_TRACKING_CATEGORIES_ACCOUNTING_PERIOD:
            return payments_applied_payments_tracking_categories_accounting_period()
        if self is JournalEntriesRetrieveRequestExpand.PAYMENTS_APPLIED_PAYMENTS_TRACKING_CATEGORIES_COMPANY:
            return payments_applied_payments_tracking_categories_company()
        if (
            self
            is JournalEntriesRetrieveRequestExpand.PAYMENTS_APPLIED_PAYMENTS_TRACKING_CATEGORIES_COMPANY_ACCOUNTING_PERIOD
        ):
            return payments_applied_payments_tracking_categories_company_accounting_period()
        if self is JournalEntriesRetrieveRequestExpand.PAYMENTS_COMPANY:
            return payments_company()
        if self is JournalEntriesRetrieveRequestExpand.PAYMENTS_COMPANY_ACCOUNTING_PERIOD:
            return payments_company_accounting_period()
        if self is JournalEntriesRetrieveRequestExpand.PAYMENTS_TRACKING_CATEGORIES:
            return payments_tracking_categories()
        if self is JournalEntriesRetrieveRequestExpand.PAYMENTS_TRACKING_CATEGORIES_ACCOUNTING_PERIOD:
            return payments_tracking_categories_accounting_period()
        if self is JournalEntriesRetrieveRequestExpand.PAYMENTS_TRACKING_CATEGORIES_COMPANY:
            return payments_tracking_categories_company()
        if self is JournalEntriesRetrieveRequestExpand.PAYMENTS_TRACKING_CATEGORIES_COMPANY_ACCOUNTING_PERIOD:
            return payments_tracking_categories_company_accounting_period()
        if self is JournalEntriesRetrieveRequestExpand.TRACKING_CATEGORIES:
            return tracking_categories()
        if self is JournalEntriesRetrieveRequestExpand.TRACKING_CATEGORIES_ACCOUNTING_PERIOD:
            return tracking_categories_accounting_period()
        if self is JournalEntriesRetrieveRequestExpand.TRACKING_CATEGORIES_COMPANY:
            return tracking_categories_company()
        if self is JournalEntriesRetrieveRequestExpand.TRACKING_CATEGORIES_COMPANY_ACCOUNTING_PERIOD:
            return tracking_categories_company_accounting_period()
