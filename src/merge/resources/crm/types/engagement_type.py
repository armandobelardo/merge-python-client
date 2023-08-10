# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

import pydantic

from ....core.datetime_utils import serialize_datetime
from .engagement_type_activity_type import EngagementTypeActivityType
from .remote_field import RemoteField


class EngagementType(pydantic.BaseModel):
    """
    # The Engagement Type Object
    ### Description
    The `Engagement Type` object is used to represent an interaction activity. A given `Engagement` typically has an `Engagement Type` object represented in the engagement_type field.
    ### Usage Example
    TODO
    """

    activity_type: typing.Optional[EngagementTypeActivityType] = pydantic.Field(
        description=(
            "The engagement type's activity type.\n"
            "\n"
            "* `CALL` - CALL\n"
            "* `MEETING` - MEETING\n"
            "* `EMAIL` - EMAIL\n"
        )
    )
    name: typing.Optional[str] = pydantic.Field(description="The engagement type's name.")
    id: typing.Optional[str]
    remote_id: typing.Optional[str] = pydantic.Field(description="The third-party API ID of the matching object.")
    modified_at: typing.Optional[dt.datetime] = pydantic.Field(
        description="This is the datetime that this object was last updated by Merge"
    )
    remote_fields: typing.Optional[typing.List[RemoteField]]

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Config:
        frozen = True
        json_encoders = {dt.datetime: serialize_datetime}
