# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

import pydantic

from ....core.datetime_utils import serialize_datetime
from .application_request_candidate import ApplicationRequestCandidate
from .application_request_credited_to import ApplicationRequestCreditedTo
from .application_request_current_stage import ApplicationRequestCurrentStage
from .application_request_job import ApplicationRequestJob
from .application_request_reject_reason import ApplicationRequestRejectReason


class ApplicationRequest(pydantic.BaseModel):
    """
    # The Application Object
    ### Description
    The Application Object is used to represent a candidate's journey through a particular Job's recruiting process. If a Candidate applies for multiple Jobs, there will be a separate Application for each Job if the third-party integration allows it.

    ### Usage Example
    Fetch from the `LIST Applications` endpoint and filter by `ID` to show all applications.
    """

    candidate: typing.Optional[ApplicationRequestCandidate] = pydantic.Field(description="The candidate applying.")
    job: typing.Optional[ApplicationRequestJob] = pydantic.Field(description="The job being applied for.")
    applied_at: typing.Optional[dt.datetime] = pydantic.Field(description="When the application was submitted.")
    rejected_at: typing.Optional[dt.datetime] = pydantic.Field(description="When the application was rejected.")
    source: typing.Optional[str] = pydantic.Field(description="The application's source.")
    credited_to: typing.Optional[ApplicationRequestCreditedTo] = pydantic.Field(
        description="The user credited for this application."
    )
    current_stage: typing.Optional[ApplicationRequestCurrentStage] = pydantic.Field(
        description="The application's current stage."
    )
    reject_reason: typing.Optional[ApplicationRequestRejectReason] = pydantic.Field(
        description="The application's reason for rejection."
    )
    remote_template_id: typing.Optional[str] = pydantic.Field(
        description='<span style="white-space: nowrap">`non-empty`</span>'
    )
    integration_params: typing.Optional[typing.Dict[str, typing.Any]]
    linked_account_params: typing.Optional[typing.Dict[str, typing.Any]]

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Config:
        frozen = True
        json_encoders = {dt.datetime: serialize_datetime}
