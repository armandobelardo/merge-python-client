# This file was auto-generated by Fern from our API Definition.

import typing

from .account import Account
from .account_owner import AccountOwner
from .address import Address
from .address_address_type import AddressAddressType
from .address_country import AddressCountry
from .address_type_enum import AddressTypeEnum
from .contact import Contact
from .contact_account import ContactAccount
from .contact_owner import ContactOwner
from .country_enum import CountryEnum
from .email_address import EmailAddress
from .field_format_enum import FieldFormatEnum
from .field_type_enum import FieldTypeEnum
from .item_format_enum import ItemFormatEnum
from .item_schema import ItemSchema
from .item_type_enum import ItemTypeEnum
from .phone_number import PhoneNumber
from .remote_data import RemoteData
from .remote_field import RemoteField
from .remote_field_class import RemoteFieldClass
from .remote_field_class_field_choices_item import RemoteFieldClassFieldChoicesItem
from .remote_field_class_field_format import RemoteFieldClassFieldFormat
from .remote_field_class_field_type import RemoteFieldClassFieldType
from .remote_field_remote_field_class import RemoteFieldRemoteFieldClass
from .user import User

LeadRequestConvertedContact = typing.Union[str, Contact]
