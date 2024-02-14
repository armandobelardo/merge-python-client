# This file was auto-generated by Fern from our API Definition.

import typing

from .group import Group
from .permission_request import PermissionRequest
from .permission_request_group import PermissionRequestGroup
from .permission_request_roles_item import PermissionRequestRolesItem
from .permission_request_type import PermissionRequestType
from .permission_request_user import PermissionRequestUser
from .roles_enum import RolesEnum
from .type_enum import TypeEnum
from .user import User

FileRequestPermissionsItem = typing.Union[str, PermissionRequest]
