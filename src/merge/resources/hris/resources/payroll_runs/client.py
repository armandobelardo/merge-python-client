# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing
import urllib.parse
from json.decoder import JSONDecodeError

from .....core.api_error import ApiError
from .....core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from .....core.datetime_utils import serialize_datetime
from .....core.remove_none_from_dict import remove_none_from_dict
from ...types.paginated_payroll_run_list import PaginatedPayrollRunList
from ...types.payroll_run import PayrollRun
from ...types.payroll_runs_list_request_remote_fields import PayrollRunsListRequestRemoteFields
from ...types.payroll_runs_list_request_run_type import PayrollRunsListRequestRunType
from ...types.payroll_runs_list_request_show_enum_origins import PayrollRunsListRequestShowEnumOrigins
from ...types.payroll_runs_retrieve_request_remote_fields import PayrollRunsRetrieveRequestRemoteFields
from ...types.payroll_runs_retrieve_request_show_enum_origins import PayrollRunsRetrieveRequestShowEnumOrigins

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class PayrollRunsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list(
        self,
        *,
        created_after: typing.Optional[dt.datetime] = None,
        created_before: typing.Optional[dt.datetime] = None,
        cursor: typing.Optional[str] = None,
        ended_after: typing.Optional[dt.datetime] = None,
        ended_before: typing.Optional[dt.datetime] = None,
        include_deleted_data: typing.Optional[bool] = None,
        include_remote_data: typing.Optional[bool] = None,
        modified_after: typing.Optional[dt.datetime] = None,
        modified_before: typing.Optional[dt.datetime] = None,
        page_size: typing.Optional[int] = None,
        remote_fields: typing.Optional[PayrollRunsListRequestRemoteFields] = None,
        remote_id: typing.Optional[str] = None,
        run_type: typing.Optional[PayrollRunsListRequestRunType] = None,
        show_enum_origins: typing.Optional[PayrollRunsListRequestShowEnumOrigins] = None,
        started_after: typing.Optional[dt.datetime] = None,
        started_before: typing.Optional[dt.datetime] = None,
    ) -> PaginatedPayrollRunList:
        """
        Returns a list of `PayrollRun` objects.

        Parameters:
            - created_after: typing.Optional[dt.datetime]. If provided, will only return objects created after this datetime.

            - created_before: typing.Optional[dt.datetime]. If provided, will only return objects created before this datetime.

            - cursor: typing.Optional[str]. The pagination cursor value.

            - ended_after: typing.Optional[dt.datetime]. If provided, will only return payroll runs ended after this datetime.

            - ended_before: typing.Optional[dt.datetime]. If provided, will only return payroll runs ended before this datetime.

            - include_deleted_data: typing.Optional[bool]. Whether to include data that was marked as deleted by third party webhooks.

            - include_remote_data: typing.Optional[bool]. Whether to include the original data Merge fetched from the third-party to produce these models.

            - modified_after: typing.Optional[dt.datetime]. If provided, only objects synced by Merge after this date time will be returned.

            - modified_before: typing.Optional[dt.datetime]. If provided, only objects synced by Merge before this date time will be returned.

            - page_size: typing.Optional[int]. Number of results to return per page.

            - remote_fields: typing.Optional[PayrollRunsListRequestRemoteFields]. Deprecated. Use show_enum_origins.

            - remote_id: typing.Optional[str]. The API provider's ID for the given object.

            - run_type: typing.Optional[PayrollRunsListRequestRunType]. If provided, will only return PayrollRun's with this status. Options: ('REGULAR', 'OFF_CYCLE', 'CORRECTION', 'TERMINATION', 'SIGN_ON_BONUS')

                                                                        * `REGULAR` - REGULAR
                                                                        * `OFF_CYCLE` - OFF_CYCLE
                                                                        * `CORRECTION` - CORRECTION
                                                                        * `TERMINATION` - TERMINATION
                                                                        * `SIGN_ON_BONUS` - SIGN_ON_BONUS
            - show_enum_origins: typing.Optional[PayrollRunsListRequestShowEnumOrigins]. Which fields should be returned in non-normalized form.

            - started_after: typing.Optional[dt.datetime]. If provided, will only return payroll runs started after this datetime.

            - started_before: typing.Optional[dt.datetime]. If provided, will only return payroll runs started before this datetime.
        ---
        from merge.client import Merge
        from merge.resources.hris import (
            PayrollRunsListRequestRemoteFields,
            PayrollRunsListRequestRunType,
            PayrollRunsListRequestShowEnumOrigins,
        )

        client = Merge(
            account_token="YOUR_ACCOUNT_TOKEN",
            api_key="YOUR_API_KEY",
        )
        client.hris.payroll_runs.list(
            remote_fields=PayrollRunsListRequestRemoteFields.RUN_STATE,
            run_type=PayrollRunsListRequestRunType.CORRECTION,
            show_enum_origins=PayrollRunsListRequestShowEnumOrigins.RUN_STATE,
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "api/hris/v1/payroll-runs"),
            params=remove_none_from_dict(
                {
                    "created_after": serialize_datetime(created_after) if created_after is not None else None,
                    "created_before": serialize_datetime(created_before) if created_before is not None else None,
                    "cursor": cursor,
                    "ended_after": serialize_datetime(ended_after) if ended_after is not None else None,
                    "ended_before": serialize_datetime(ended_before) if ended_before is not None else None,
                    "include_deleted_data": include_deleted_data,
                    "include_remote_data": include_remote_data,
                    "modified_after": serialize_datetime(modified_after) if modified_after is not None else None,
                    "modified_before": serialize_datetime(modified_before) if modified_before is not None else None,
                    "page_size": page_size,
                    "remote_fields": remote_fields,
                    "remote_id": remote_id,
                    "run_type": run_type,
                    "show_enum_origins": show_enum_origins,
                    "started_after": serialize_datetime(started_after) if started_after is not None else None,
                    "started_before": serialize_datetime(started_before) if started_before is not None else None,
                }
            ),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(PaginatedPayrollRunList, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def retrieve(
        self,
        id: str,
        *,
        include_remote_data: typing.Optional[bool] = None,
        remote_fields: typing.Optional[PayrollRunsRetrieveRequestRemoteFields] = None,
        show_enum_origins: typing.Optional[PayrollRunsRetrieveRequestShowEnumOrigins] = None,
    ) -> PayrollRun:
        """
        Returns a `PayrollRun` object with the given `id`.

        Parameters:
            - id: str.

            - include_remote_data: typing.Optional[bool]. Whether to include the original data Merge fetched from the third-party to produce these models.

            - remote_fields: typing.Optional[PayrollRunsRetrieveRequestRemoteFields]. Deprecated. Use show_enum_origins.

            - show_enum_origins: typing.Optional[PayrollRunsRetrieveRequestShowEnumOrigins]. Which fields should be returned in non-normalized form.
        ---
        from merge.client import Merge
        from merge.resources.hris import (
            PayrollRunsRetrieveRequestRemoteFields,
            PayrollRunsRetrieveRequestShowEnumOrigins,
        )

        client = Merge(
            account_token="YOUR_ACCOUNT_TOKEN",
            api_key="YOUR_API_KEY",
        )
        client.hris.payroll_runs.retrieve(
            id="id",
            remote_fields=PayrollRunsRetrieveRequestRemoteFields.RUN_STATE,
            show_enum_origins=PayrollRunsRetrieveRequestShowEnumOrigins.RUN_STATE,
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", f"api/hris/v1/payroll-runs/{id}"),
            params=remove_none_from_dict(
                {
                    "include_remote_data": include_remote_data,
                    "remote_fields": remote_fields,
                    "show_enum_origins": show_enum_origins,
                }
            ),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(PayrollRun, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)


class AsyncPayrollRunsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def list(
        self,
        *,
        created_after: typing.Optional[dt.datetime] = None,
        created_before: typing.Optional[dt.datetime] = None,
        cursor: typing.Optional[str] = None,
        ended_after: typing.Optional[dt.datetime] = None,
        ended_before: typing.Optional[dt.datetime] = None,
        include_deleted_data: typing.Optional[bool] = None,
        include_remote_data: typing.Optional[bool] = None,
        modified_after: typing.Optional[dt.datetime] = None,
        modified_before: typing.Optional[dt.datetime] = None,
        page_size: typing.Optional[int] = None,
        remote_fields: typing.Optional[PayrollRunsListRequestRemoteFields] = None,
        remote_id: typing.Optional[str] = None,
        run_type: typing.Optional[PayrollRunsListRequestRunType] = None,
        show_enum_origins: typing.Optional[PayrollRunsListRequestShowEnumOrigins] = None,
        started_after: typing.Optional[dt.datetime] = None,
        started_before: typing.Optional[dt.datetime] = None,
    ) -> PaginatedPayrollRunList:
        """
        Returns a list of `PayrollRun` objects.

        Parameters:
            - created_after: typing.Optional[dt.datetime]. If provided, will only return objects created after this datetime.

            - created_before: typing.Optional[dt.datetime]. If provided, will only return objects created before this datetime.

            - cursor: typing.Optional[str]. The pagination cursor value.

            - ended_after: typing.Optional[dt.datetime]. If provided, will only return payroll runs ended after this datetime.

            - ended_before: typing.Optional[dt.datetime]. If provided, will only return payroll runs ended before this datetime.

            - include_deleted_data: typing.Optional[bool]. Whether to include data that was marked as deleted by third party webhooks.

            - include_remote_data: typing.Optional[bool]. Whether to include the original data Merge fetched from the third-party to produce these models.

            - modified_after: typing.Optional[dt.datetime]. If provided, only objects synced by Merge after this date time will be returned.

            - modified_before: typing.Optional[dt.datetime]. If provided, only objects synced by Merge before this date time will be returned.

            - page_size: typing.Optional[int]. Number of results to return per page.

            - remote_fields: typing.Optional[PayrollRunsListRequestRemoteFields]. Deprecated. Use show_enum_origins.

            - remote_id: typing.Optional[str]. The API provider's ID for the given object.

            - run_type: typing.Optional[PayrollRunsListRequestRunType]. If provided, will only return PayrollRun's with this status. Options: ('REGULAR', 'OFF_CYCLE', 'CORRECTION', 'TERMINATION', 'SIGN_ON_BONUS')

                                                                        * `REGULAR` - REGULAR
                                                                        * `OFF_CYCLE` - OFF_CYCLE
                                                                        * `CORRECTION` - CORRECTION
                                                                        * `TERMINATION` - TERMINATION
                                                                        * `SIGN_ON_BONUS` - SIGN_ON_BONUS
            - show_enum_origins: typing.Optional[PayrollRunsListRequestShowEnumOrigins]. Which fields should be returned in non-normalized form.

            - started_after: typing.Optional[dt.datetime]. If provided, will only return payroll runs started after this datetime.

            - started_before: typing.Optional[dt.datetime]. If provided, will only return payroll runs started before this datetime.
        ---
        from merge.client import AsyncMerge
        from merge.resources.hris import (
            PayrollRunsListRequestRemoteFields,
            PayrollRunsListRequestRunType,
            PayrollRunsListRequestShowEnumOrigins,
        )

        client = AsyncMerge(
            account_token="YOUR_ACCOUNT_TOKEN",
            api_key="YOUR_API_KEY",
        )
        await client.hris.payroll_runs.list(
            remote_fields=PayrollRunsListRequestRemoteFields.RUN_STATE,
            run_type=PayrollRunsListRequestRunType.CORRECTION,
            show_enum_origins=PayrollRunsListRequestShowEnumOrigins.RUN_STATE,
        )
        """
        _response = await self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "api/hris/v1/payroll-runs"),
            params=remove_none_from_dict(
                {
                    "created_after": serialize_datetime(created_after) if created_after is not None else None,
                    "created_before": serialize_datetime(created_before) if created_before is not None else None,
                    "cursor": cursor,
                    "ended_after": serialize_datetime(ended_after) if ended_after is not None else None,
                    "ended_before": serialize_datetime(ended_before) if ended_before is not None else None,
                    "include_deleted_data": include_deleted_data,
                    "include_remote_data": include_remote_data,
                    "modified_after": serialize_datetime(modified_after) if modified_after is not None else None,
                    "modified_before": serialize_datetime(modified_before) if modified_before is not None else None,
                    "page_size": page_size,
                    "remote_fields": remote_fields,
                    "remote_id": remote_id,
                    "run_type": run_type,
                    "show_enum_origins": show_enum_origins,
                    "started_after": serialize_datetime(started_after) if started_after is not None else None,
                    "started_before": serialize_datetime(started_before) if started_before is not None else None,
                }
            ),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(PaginatedPayrollRunList, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def retrieve(
        self,
        id: str,
        *,
        include_remote_data: typing.Optional[bool] = None,
        remote_fields: typing.Optional[PayrollRunsRetrieveRequestRemoteFields] = None,
        show_enum_origins: typing.Optional[PayrollRunsRetrieveRequestShowEnumOrigins] = None,
    ) -> PayrollRun:
        """
        Returns a `PayrollRun` object with the given `id`.

        Parameters:
            - id: str.

            - include_remote_data: typing.Optional[bool]. Whether to include the original data Merge fetched from the third-party to produce these models.

            - remote_fields: typing.Optional[PayrollRunsRetrieveRequestRemoteFields]. Deprecated. Use show_enum_origins.

            - show_enum_origins: typing.Optional[PayrollRunsRetrieveRequestShowEnumOrigins]. Which fields should be returned in non-normalized form.
        ---
        from merge.client import AsyncMerge
        from merge.resources.hris import (
            PayrollRunsRetrieveRequestRemoteFields,
            PayrollRunsRetrieveRequestShowEnumOrigins,
        )

        client = AsyncMerge(
            account_token="YOUR_ACCOUNT_TOKEN",
            api_key="YOUR_API_KEY",
        )
        await client.hris.payroll_runs.retrieve(
            id="id",
            remote_fields=PayrollRunsRetrieveRequestRemoteFields.RUN_STATE,
            show_enum_origins=PayrollRunsRetrieveRequestShowEnumOrigins.RUN_STATE,
        )
        """
        _response = await self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", f"api/hris/v1/payroll-runs/{id}"),
            params=remove_none_from_dict(
                {
                    "include_remote_data": include_remote_data,
                    "remote_fields": remote_fields,
                    "show_enum_origins": show_enum_origins,
                }
            ),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(PayrollRun, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)
