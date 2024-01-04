# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ....core.datetime_utils import serialize_datetime

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class ModelOperation(pydantic.BaseModel):
    """
    # The ModelOperation Object
    ### Description
    The `ModelOperation` object is used to represent the operations that are currently supported for a given model.

    ### Usage Example
    View what operations are supported for the `Candidate` endpoint.
    """

    model_name: str
    available_operations: typing.List[str]
    required_post_parameters: typing.List[str]
    supported_fields: typing.List[str]

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
