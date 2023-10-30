# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ....core.datetime_utils import serialize_datetime
from .permission_group import PermissionGroup
from .permission_roles_item import PermissionRolesItem
from .permission_type import PermissionType
from .permission_user import PermissionUser

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class Permission(pydantic.BaseModel):
    """
    # The Permission Object
    ### Description
    The Permission object is used to represent a user's or group's access to a File or Folder. Permissions are unexpanded by default.

    ### Usage Example
    Fetch from the `GET Files` or `GET Folders` endpoint. Permissions are unexpanded by default. Use the query param `expand=permissions` to see more details.
    """

    id: typing.Optional[str]
    remote_id: typing.Optional[str] = pydantic.Field(description="The third-party API ID of the matching object.")
    user: typing.Optional[PermissionUser] = pydantic.Field(description="The user that is granted this permission.")
    group: typing.Optional[PermissionGroup] = pydantic.Field(description="The group that is granted this permission.")
    type: typing.Optional[PermissionType] = pydantic.Field(
        description=(
            "Denotes what type of people have access to the file.\n"
            "\n"
            "* `USER` - USER\n"
            "* `GROUP` - GROUP\n"
            "* `COMPANY` - COMPANY\n"
            "* `ANYONE` - ANYONE\n"
        )
    )
    roles: typing.Optional[typing.List[typing.Optional[PermissionRolesItem]]] = pydantic.Field(
        description="The permissions that the user or group has for the File or Folder. It is possible for a user or group to have multiple roles, such as viewing & uploading. Possible values include: `READ`, `WRITE`, `OWNER`. In cases where there is no clear mapping, the original value passed through will be returned."
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
