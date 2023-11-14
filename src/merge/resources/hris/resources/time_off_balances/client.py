# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing
import urllib.parse
from json.decoder import JSONDecodeError

import typing_extensions

from .....core.api_error import ApiError
from .....core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from .....core.datetime_utils import serialize_datetime
from .....core.remove_none_from_dict import remove_none_from_dict
from ...types.paginated_time_off_balance_list import PaginatedTimeOffBalanceList
from ...types.time_off_balance import TimeOffBalance
from ...types.time_off_balances_list_request_policy_type import TimeOffBalancesListRequestPolicyType

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class TimeOffBalancesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list(
        self,
        *,
        created_after: typing.Optional[dt.datetime] = None,
        created_before: typing.Optional[dt.datetime] = None,
        cursor: typing.Optional[str] = None,
        employee_id: typing.Optional[str] = None,
        expand: typing.Optional[typing_extensions.Literal["employee"]] = None,
        include_deleted_data: typing.Optional[bool] = None,
        include_remote_data: typing.Optional[bool] = None,
        modified_after: typing.Optional[dt.datetime] = None,
        modified_before: typing.Optional[dt.datetime] = None,
        page_size: typing.Optional[int] = None,
        policy_type: typing.Optional[TimeOffBalancesListRequestPolicyType] = None,
        remote_fields: typing.Optional[typing_extensions.Literal["policy_type"]] = None,
        remote_id: typing.Optional[str] = None,
        show_enum_origins: typing.Optional[typing_extensions.Literal["policy_type"]] = None,
    ) -> PaginatedTimeOffBalanceList:
        """
        Returns a list of `TimeOffBalance` objects.

        Parameters:
            - created_after: typing.Optional[dt.datetime]. If provided, will only return objects created after this datetime.

            - created_before: typing.Optional[dt.datetime]. If provided, will only return objects created before this datetime.

            - cursor: typing.Optional[str]. The pagination cursor value.

            - employee_id: typing.Optional[str]. If provided, will only return time off balances for this employee.

            - expand: typing.Optional[typing_extensions.Literal["employee"]]. Which relations should be returned in expanded form. Multiple relation names should be comma separated without spaces.

            - include_deleted_data: typing.Optional[bool]. Whether to include data that was marked as deleted by third party webhooks.

            - include_remote_data: typing.Optional[bool]. Whether to include the original data Merge fetched from the third-party to produce these models.

            - modified_after: typing.Optional[dt.datetime]. If provided, only objects synced by Merge after this date time will be returned.

            - modified_before: typing.Optional[dt.datetime]. If provided, only objects synced by Merge before this date time will be returned.

            - page_size: typing.Optional[int]. Number of results to return per page.

            - policy_type: typing.Optional[TimeOffBalancesListRequestPolicyType]. If provided, will only return TimeOffBalance with this policy type. Options: ('VACATION', 'SICK', 'PERSONAL', 'JURY_DUTY', 'VOLUNTEER', 'BEREAVEMENT')

                                                                                  * `VACATION` - VACATION
                                                                                  * `SICK` - SICK
                                                                                  * `PERSONAL` - PERSONAL
                                                                                  * `JURY_DUTY` - JURY_DUTY
                                                                                  * `VOLUNTEER` - VOLUNTEER
                                                                                  * `BEREAVEMENT` - BEREAVEMENT
            - remote_fields: typing.Optional[typing_extensions.Literal["policy_type"]]. Deprecated. Use show_enum_origins.

            - remote_id: typing.Optional[str]. The API provider's ID for the given object.

            - show_enum_origins: typing.Optional[typing_extensions.Literal["policy_type"]]. Which fields should be returned in non-normalized form.
        ---
        from merge.client import Merge
        from merge.resources.hris import TimeOffBalancesListRequestPolicyType

        client = Merge(
            account_token="YOUR_ACCOUNT_TOKEN",
            api_key="YOUR_API_KEY",
        )
        client.hris.time_off_balances.list(
            expand="employee",
            policy_type=TimeOffBalancesListRequestPolicyType.BEREAVEMENT,
            remote_fields="policy_type",
            show_enum_origins="policy_type",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "api/hris/v1/time-off-balances"),
            params=remove_none_from_dict(
                {
                    "created_after": serialize_datetime(created_after) if created_after is not None else None,
                    "created_before": serialize_datetime(created_before) if created_before is not None else None,
                    "cursor": cursor,
                    "employee_id": employee_id,
                    "expand": expand,
                    "include_deleted_data": include_deleted_data,
                    "include_remote_data": include_remote_data,
                    "modified_after": serialize_datetime(modified_after) if modified_after is not None else None,
                    "modified_before": serialize_datetime(modified_before) if modified_before is not None else None,
                    "page_size": page_size,
                    "policy_type": policy_type,
                    "remote_fields": remote_fields,
                    "remote_id": remote_id,
                    "show_enum_origins": show_enum_origins,
                }
            ),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(PaginatedTimeOffBalanceList, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def retrieve(
        self,
        id: str,
        *,
        expand: typing.Optional[typing_extensions.Literal["employee"]] = None,
        include_remote_data: typing.Optional[bool] = None,
        remote_fields: typing.Optional[typing_extensions.Literal["policy_type"]] = None,
        show_enum_origins: typing.Optional[typing_extensions.Literal["policy_type"]] = None,
    ) -> TimeOffBalance:
        """
        Returns a `TimeOffBalance` object with the given `id`.

        Parameters:
            - id: str.

            - expand: typing.Optional[typing_extensions.Literal["employee"]]. Which relations should be returned in expanded form. Multiple relation names should be comma separated without spaces.

            - include_remote_data: typing.Optional[bool]. Whether to include the original data Merge fetched from the third-party to produce these models.

            - remote_fields: typing.Optional[typing_extensions.Literal["policy_type"]]. Deprecated. Use show_enum_origins.

            - show_enum_origins: typing.Optional[typing_extensions.Literal["policy_type"]]. Which fields should be returned in non-normalized form.
        ---
        from merge.client import Merge

        client = Merge(
            account_token="YOUR_ACCOUNT_TOKEN",
            api_key="YOUR_API_KEY",
        )
        client.hris.time_off_balances.retrieve(
            id="id",
            expand="employee",
            remote_fields="policy_type",
            show_enum_origins="policy_type",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", f"api/hris/v1/time-off-balances/{id}"),
            params=remove_none_from_dict(
                {
                    "expand": expand,
                    "include_remote_data": include_remote_data,
                    "remote_fields": remote_fields,
                    "show_enum_origins": show_enum_origins,
                }
            ),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(TimeOffBalance, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)


class AsyncTimeOffBalancesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def list(
        self,
        *,
        created_after: typing.Optional[dt.datetime] = None,
        created_before: typing.Optional[dt.datetime] = None,
        cursor: typing.Optional[str] = None,
        employee_id: typing.Optional[str] = None,
        expand: typing.Optional[typing_extensions.Literal["employee"]] = None,
        include_deleted_data: typing.Optional[bool] = None,
        include_remote_data: typing.Optional[bool] = None,
        modified_after: typing.Optional[dt.datetime] = None,
        modified_before: typing.Optional[dt.datetime] = None,
        page_size: typing.Optional[int] = None,
        policy_type: typing.Optional[TimeOffBalancesListRequestPolicyType] = None,
        remote_fields: typing.Optional[typing_extensions.Literal["policy_type"]] = None,
        remote_id: typing.Optional[str] = None,
        show_enum_origins: typing.Optional[typing_extensions.Literal["policy_type"]] = None,
    ) -> PaginatedTimeOffBalanceList:
        """
        Returns a list of `TimeOffBalance` objects.

        Parameters:
            - created_after: typing.Optional[dt.datetime]. If provided, will only return objects created after this datetime.

            - created_before: typing.Optional[dt.datetime]. If provided, will only return objects created before this datetime.

            - cursor: typing.Optional[str]. The pagination cursor value.

            - employee_id: typing.Optional[str]. If provided, will only return time off balances for this employee.

            - expand: typing.Optional[typing_extensions.Literal["employee"]]. Which relations should be returned in expanded form. Multiple relation names should be comma separated without spaces.

            - include_deleted_data: typing.Optional[bool]. Whether to include data that was marked as deleted by third party webhooks.

            - include_remote_data: typing.Optional[bool]. Whether to include the original data Merge fetched from the third-party to produce these models.

            - modified_after: typing.Optional[dt.datetime]. If provided, only objects synced by Merge after this date time will be returned.

            - modified_before: typing.Optional[dt.datetime]. If provided, only objects synced by Merge before this date time will be returned.

            - page_size: typing.Optional[int]. Number of results to return per page.

            - policy_type: typing.Optional[TimeOffBalancesListRequestPolicyType]. If provided, will only return TimeOffBalance with this policy type. Options: ('VACATION', 'SICK', 'PERSONAL', 'JURY_DUTY', 'VOLUNTEER', 'BEREAVEMENT')

                                                                                  * `VACATION` - VACATION
                                                                                  * `SICK` - SICK
                                                                                  * `PERSONAL` - PERSONAL
                                                                                  * `JURY_DUTY` - JURY_DUTY
                                                                                  * `VOLUNTEER` - VOLUNTEER
                                                                                  * `BEREAVEMENT` - BEREAVEMENT
            - remote_fields: typing.Optional[typing_extensions.Literal["policy_type"]]. Deprecated. Use show_enum_origins.

            - remote_id: typing.Optional[str]. The API provider's ID for the given object.

            - show_enum_origins: typing.Optional[typing_extensions.Literal["policy_type"]]. Which fields should be returned in non-normalized form.
        ---
        from merge.client import AsyncMerge
        from merge.resources.hris import TimeOffBalancesListRequestPolicyType

        client = AsyncMerge(
            account_token="YOUR_ACCOUNT_TOKEN",
            api_key="YOUR_API_KEY",
        )
        await client.hris.time_off_balances.list(
            expand="employee",
            policy_type=TimeOffBalancesListRequestPolicyType.BEREAVEMENT,
            remote_fields="policy_type",
            show_enum_origins="policy_type",
        )
        """
        _response = await self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "api/hris/v1/time-off-balances"),
            params=remove_none_from_dict(
                {
                    "created_after": serialize_datetime(created_after) if created_after is not None else None,
                    "created_before": serialize_datetime(created_before) if created_before is not None else None,
                    "cursor": cursor,
                    "employee_id": employee_id,
                    "expand": expand,
                    "include_deleted_data": include_deleted_data,
                    "include_remote_data": include_remote_data,
                    "modified_after": serialize_datetime(modified_after) if modified_after is not None else None,
                    "modified_before": serialize_datetime(modified_before) if modified_before is not None else None,
                    "page_size": page_size,
                    "policy_type": policy_type,
                    "remote_fields": remote_fields,
                    "remote_id": remote_id,
                    "show_enum_origins": show_enum_origins,
                }
            ),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(PaginatedTimeOffBalanceList, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def retrieve(
        self,
        id: str,
        *,
        expand: typing.Optional[typing_extensions.Literal["employee"]] = None,
        include_remote_data: typing.Optional[bool] = None,
        remote_fields: typing.Optional[typing_extensions.Literal["policy_type"]] = None,
        show_enum_origins: typing.Optional[typing_extensions.Literal["policy_type"]] = None,
    ) -> TimeOffBalance:
        """
        Returns a `TimeOffBalance` object with the given `id`.

        Parameters:
            - id: str.

            - expand: typing.Optional[typing_extensions.Literal["employee"]]. Which relations should be returned in expanded form. Multiple relation names should be comma separated without spaces.

            - include_remote_data: typing.Optional[bool]. Whether to include the original data Merge fetched from the third-party to produce these models.

            - remote_fields: typing.Optional[typing_extensions.Literal["policy_type"]]. Deprecated. Use show_enum_origins.

            - show_enum_origins: typing.Optional[typing_extensions.Literal["policy_type"]]. Which fields should be returned in non-normalized form.
        ---
        from merge.client import AsyncMerge

        client = AsyncMerge(
            account_token="YOUR_ACCOUNT_TOKEN",
            api_key="YOUR_API_KEY",
        )
        await client.hris.time_off_balances.retrieve(
            id="id",
            expand="employee",
            remote_fields="policy_type",
            show_enum_origins="policy_type",
        )
        """
        _response = await self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", f"api/hris/v1/time-off-balances/{id}"),
            params=remove_none_from_dict(
                {
                    "expand": expand,
                    "include_remote_data": include_remote_data,
                    "remote_fields": remote_fields,
                    "show_enum_origins": show_enum_origins,
                }
            ),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(TimeOffBalance, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)
