# This file was auto-generated by Fern from our API Definition.

import typing
import urllib.parse
from json.decoder import JSONDecodeError

import typing_extensions

from .....core.api_error import ApiError
from .....core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from .....core.remove_none_from_dict import remove_none_from_dict
from ...types.address import Address

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class AddressesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def retrieve(
        self,
        id: str,
        *,
        include_remote_data: typing.Optional[bool] = None,
        remote_fields: typing.Optional[typing_extensions.Literal["type"]] = None,
        show_enum_origins: typing.Optional[typing_extensions.Literal["type"]] = None,
    ) -> Address:
        """
        Returns an `Address` object with the given `id`.

        Parameters:
            - id: str.

            - include_remote_data: typing.Optional[bool]. Whether to include the original data Merge fetched from the third-party to produce these models.

            - remote_fields: typing.Optional[typing_extensions.Literal["type"]]. Deprecated. Use show_enum_origins.

            - show_enum_origins: typing.Optional[typing_extensions.Literal["type"]]. Which fields should be returned in non-normalized form.
        ---
        from merge.client import Merge

        client = Merge(
            account_token="YOUR_ACCOUNT_TOKEN",
            api_key="YOUR_API_KEY",
        )
        client.accounting.addresses.retrieve(
            id="id",
            remote_fields="type",
            show_enum_origins="type",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", f"api/accounting/v1/addresses/{id}"),
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
            return pydantic.parse_obj_as(Address, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)


class AsyncAddressesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def retrieve(
        self,
        id: str,
        *,
        include_remote_data: typing.Optional[bool] = None,
        remote_fields: typing.Optional[typing_extensions.Literal["type"]] = None,
        show_enum_origins: typing.Optional[typing_extensions.Literal["type"]] = None,
    ) -> Address:
        """
        Returns an `Address` object with the given `id`.

        Parameters:
            - id: str.

            - include_remote_data: typing.Optional[bool]. Whether to include the original data Merge fetched from the third-party to produce these models.

            - remote_fields: typing.Optional[typing_extensions.Literal["type"]]. Deprecated. Use show_enum_origins.

            - show_enum_origins: typing.Optional[typing_extensions.Literal["type"]]. Which fields should be returned in non-normalized form.
        ---
        from merge.client import AsyncMerge

        client = AsyncMerge(
            account_token="YOUR_ACCOUNT_TOKEN",
            api_key="YOUR_API_KEY",
        )
        await client.accounting.addresses.retrieve(
            id="id",
            remote_fields="type",
            show_enum_origins="type",
        )
        """
        _response = await self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", f"api/accounting/v1/addresses/{id}"),
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
            return pydantic.parse_obj_as(Address, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)
