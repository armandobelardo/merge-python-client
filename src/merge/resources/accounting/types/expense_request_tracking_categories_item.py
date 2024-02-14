# This file was auto-generated by Fern from our API Definition.

import typing

from .accounting_phone_number import AccountingPhoneNumber
from .address import Address
from .address_country import AddressCountry
from .address_type import AddressType
from .address_type_enum import AddressTypeEnum
from .category_type_enum import CategoryTypeEnum
from .company_info import CompanyInfo
from .company_info_currency import CompanyInfoCurrency
from .country_enum import CountryEnum
from .currency_enum import CurrencyEnum
from .remote_data import RemoteData
from .status_7_d_1_enum import Status7D1Enum
from .tracking_category import TrackingCategory
from .tracking_category_category_type import TrackingCategoryCategoryType
from .tracking_category_company import TrackingCategoryCompany
from .tracking_category_status import TrackingCategoryStatus

ExpenseRequestTrackingCategoriesItem = typing.Union[str, TrackingCategory]
