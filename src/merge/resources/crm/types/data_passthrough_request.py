# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

import pydantic

from ....core.datetime_utils import serialize_datetime
from .method_enum import MethodEnum
from .multipart_form_field_request import MultipartFormFieldRequest
from .request_format_enum import RequestFormatEnum


class DataPassthroughRequest(pydantic.BaseModel):
    """
    # The DataPassthrough Object
    ### Description
    The `DataPassthrough` object is used to send information to an otherwise-unsupported third-party endpoint.

    ### Usage Example
    Create a `DataPassthrough` to get team hierarchies from your Rippling integration.
    """

    method: MethodEnum
    path: str = pydantic.Field(description='<span style="white-space: nowrap">`non-empty`</span>')
    base_url_override: typing.Optional[str] = pydantic.Field(
        description='<span style="white-space: nowrap">`non-empty`</span>'
    )
    data: typing.Optional[str] = pydantic.Field(description='<span style="white-space: nowrap">`non-empty`</span>')
    multipart_form_data: typing.Optional[typing.List[MultipartFormFieldRequest]] = pydantic.Field(
        description="Pass an array of `MultipartFormField` objects in here instead of using the `data` param if `request_format` is set to `MULTIPART`."
    )
    headers: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(
        description="The headers to use for the request (Merge will handle the account's authorization headers). `Content-Type` header is required for passthrough. Choose content type corresponding to expected format of receiving server."
    )
    request_format: typing.Optional[RequestFormatEnum]
    normalize_response: typing.Optional[bool] = pydantic.Field(
        description='Optional. If true, the response will always be an object of the form `{"type": T, "value": ...}` where `T` will be one of `string, boolean, number, null, array, object`.'
    )

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Config:
        frozen = True
        json_encoders = {dt.datetime: serialize_datetime}