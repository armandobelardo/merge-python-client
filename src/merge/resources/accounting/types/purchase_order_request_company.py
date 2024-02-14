# This file was auto-generated by Fern from our API Definition.

import typing

from .accounting_phone_number import AccountingPhoneNumber
from .address import Address
from .address_country import AddressCountry
from .address_type import AddressType
from .address_type_enum import AddressTypeEnum
from .company_info import CompanyInfo
from .company_info_currency import CompanyInfoCurrency
from .country_enum import CountryEnum
from .currency_enum import CurrencyEnum
from .remote_data import RemoteData

PurchaseOrderRequestCompany = typing.Union[str, CompanyInfo]
