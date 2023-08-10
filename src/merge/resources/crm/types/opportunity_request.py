# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

import pydantic

from ....core.datetime_utils import serialize_datetime
from .opportunity_request_account import OpportunityRequestAccount
from .opportunity_request_owner import OpportunityRequestOwner
from .opportunity_request_stage import OpportunityRequestStage
from .opportunity_request_status import OpportunityRequestStatus
from .remote_field_request import RemoteFieldRequest


class OpportunityRequest(pydantic.BaseModel):
    """
    # The Opportunity Object
    ### Description
    The `Opportunity` object is used to represent a deal opportunity in a CRM system.
    ### Usage Example
    TODO
    """

    name: typing.Optional[str] = pydantic.Field(description="The opportunity's name.")
    description: typing.Optional[str] = pydantic.Field(description="The opportunity's description.")
    amount: typing.Optional[int] = pydantic.Field(description="The opportunity's amount.")
    owner: typing.Optional[OpportunityRequestOwner] = pydantic.Field(description="The opportunity's owner.")
    account: typing.Optional[OpportunityRequestAccount] = pydantic.Field(description="The account of the opportunity.")
    stage: typing.Optional[OpportunityRequestStage] = pydantic.Field(description="The stage of the opportunity.")
    status: typing.Optional[OpportunityRequestStatus] = pydantic.Field(
        description=("The opportunity's status.\n" "\n" "* `OPEN` - OPEN\n" "* `WON` - WON\n" "* `LOST` - LOST\n")
    )
    last_activity_at: typing.Optional[dt.datetime] = pydantic.Field(
        description="When the opportunity's last activity occurred."
    )
    close_date: typing.Optional[dt.datetime] = pydantic.Field(description="When the opportunity was closed.")
    integration_params: typing.Optional[typing.Dict[str, typing.Any]]
    linked_account_params: typing.Optional[typing.Dict[str, typing.Any]]
    remote_fields: typing.Optional[typing.List[RemoteFieldRequest]]

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Config:
        frozen = True
        json_encoders = {dt.datetime: serialize_datetime}
