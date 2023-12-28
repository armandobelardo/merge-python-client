# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ....core.datetime_utils import serialize_datetime
from .phone_number_phone_number_type import PhoneNumberPhoneNumberType

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class PhoneNumber(pydantic.BaseModel):
    """
    # The PhoneNumber Object

    ### Description

    The `PhoneNumber` object is used to represent a candidate's phone number.

    ### Usage Example

    Fetch from the `GET Candidate` endpoint and view their phone numbers.
    """

    value: typing.Optional[str] = pydantic.Field(description="The phone number.")
    phone_number_type: typing.Optional[PhoneNumberPhoneNumberType] = pydantic.Field(
        description=(
            "The type of phone number.\n"
            "\n"
            "- `HOME` - HOME\n"
            "- `WORK` - WORK\n"
            "- `MOBILE` - MOBILE\n"
            "- `SKYPE` - SKYPE\n"
            "- `OTHER` - OTHER\n"
        )
    )
    created_at: typing.Optional[dt.datetime]
    modified_at: typing.Optional[dt.datetime] = pydantic.Field(
        description="This is the datetime that this object was last updated by Merge"
    )

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Config:
        frozen = True
        smart_union = True
        json_encoders = {dt.datetime: serialize_datetime}
