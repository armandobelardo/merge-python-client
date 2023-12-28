# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ....core.datetime_utils import serialize_datetime
from .audit_log_event_event_type import AuditLogEventEventType
from .audit_log_event_role import AuditLogEventRole

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class AuditLogEvent(pydantic.BaseModel):
    id: typing.Optional[str]
    user_name: typing.Optional[str] = pydantic.Field(
        description="The User's full name at the time of this Event occurring."
    )
    user_email: typing.Optional[str] = pydantic.Field(
        description="The User's email at the time of this Event occurring."
    )
    role: AuditLogEventRole = pydantic.Field(
        description=(
            "Designates the role of the user (or SYSTEM/API if action not taken by a user) at the time of this Event occurring.\n"
            "\n"
            "- `ADMIN` - ADMIN\n"
            "- `DEVELOPER` - DEVELOPER\n"
            "- `MEMBER` - MEMBER\n"
            "- `API` - API\n"
            "- `SYSTEM` - SYSTEM\n"
            "- `MERGE_TEAM` - MERGE_TEAM\n"
        )
    )
    ip_address: str
    event_type: AuditLogEventEventType = pydantic.Field(
        description=(
            "Designates the type of event that occurred.\n"
            "\n"
            "- `CREATED_REMOTE_PRODUCTION_API_KEY` - CREATED_REMOTE_PRODUCTION_API_KEY\n"
            "- `DELETED_REMOTE_PRODUCTION_API_KEY` - DELETED_REMOTE_PRODUCTION_API_KEY\n"
            "- `CREATED_TEST_API_KEY` - CREATED_TEST_API_KEY\n"
            "- `DELETED_TEST_API_KEY` - DELETED_TEST_API_KEY\n"
            "- `REGENERATED_PRODUCTION_API_KEY` - REGENERATED_PRODUCTION_API_KEY\n"
            "- `INVITED_USER` - INVITED_USER\n"
            "- `TWO_FACTOR_AUTH_ENABLED` - TWO_FACTOR_AUTH_ENABLED\n"
            "- `TWO_FACTOR_AUTH_DISABLED` - TWO_FACTOR_AUTH_DISABLED\n"
            "- `DELETED_LINKED_ACCOUNT` - DELETED_LINKED_ACCOUNT\n"
            "- `CREATED_DESTINATION` - CREATED_DESTINATION\n"
            "- `DELETED_DESTINATION` - DELETED_DESTINATION\n"
            "- `CHANGED_SCOPES` - CHANGED_SCOPES\n"
            "- `CHANGED_PERSONAL_INFORMATION` - CHANGED_PERSONAL_INFORMATION\n"
            "- `CHANGED_ORGANIZATION_SETTINGS` - CHANGED_ORGANIZATION_SETTINGS\n"
            "- `ENABLED_INTEGRATION` - ENABLED_INTEGRATION\n"
            "- `DISABLED_INTEGRATION` - DISABLED_INTEGRATION\n"
            "- `ENABLED_CATEGORY` - ENABLED_CATEGORY\n"
            "- `DISABLED_CATEGORY` - DISABLED_CATEGORY\n"
            "- `CHANGED_PASSWORD` - CHANGED_PASSWORD\n"
            "- `RESET_PASSWORD` - RESET_PASSWORD\n"
            "- `ENABLED_REDACT_UNMAPPED_DATA_FOR_ORGANIZATION` - ENABLED_REDACT_UNMAPPED_DATA_FOR_ORGANIZATION\n"
            "- `ENABLED_REDACT_UNMAPPED_DATA_FOR_LINKED_ACCOUNT` - ENABLED_REDACT_UNMAPPED_DATA_FOR_LINKED_ACCOUNT\n"
            "- `DISABLED_REDACT_UNMAPPED_DATA_FOR_ORGANIZATION` - DISABLED_REDACT_UNMAPPED_DATA_FOR_ORGANIZATION\n"
            "- `DISABLED_REDACT_UNMAPPED_DATA_FOR_LINKED_ACCOUNT` - DISABLED_REDACT_UNMAPPED_DATA_FOR_LINKED_ACCOUNT\n"
            "- `CREATED_INTEGRATION_WIDE_FIELD_MAPPING` - CREATED_INTEGRATION_WIDE_FIELD_MAPPING\n"
            "- `CREATED_LINKED_ACCOUNT_FIELD_MAPPING` - CREATED_LINKED_ACCOUNT_FIELD_MAPPING\n"
            "- `CHANGED_INTEGRATION_WIDE_FIELD_MAPPING` - CHANGED_INTEGRATION_WIDE_FIELD_MAPPING\n"
            "- `CHANGED_LINKED_ACCOUNT_FIELD_MAPPING` - CHANGED_LINKED_ACCOUNT_FIELD_MAPPING\n"
            "- `DELETED_INTEGRATION_WIDE_FIELD_MAPPING` - DELETED_INTEGRATION_WIDE_FIELD_MAPPING\n"
            "- `DELETED_LINKED_ACCOUNT_FIELD_MAPPING` - DELETED_LINKED_ACCOUNT_FIELD_MAPPING\n"
        )
    )
    event_description: str
    created_at: typing.Optional[dt.datetime]

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
