# This file was auto-generated by Fern from our API Definition.

import urllib.parse
from json.decoder import JSONDecodeError

from .....core.api_error import ApiError
from .....core.client_wrapper import AsyncClientWrapper, SyncClientWrapper


class DeleteAccountClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def delete(self) -> None:
        """
        Delete a linked account.

        ---
        from merge.client import Merge

        client = Merge(
            account_token="YOUR_ACCOUNT_TOKEN",
            api_key="YOUR_API_KEY",
        )
        client.ats.delete_account.delete()
        """
        _response = self._client_wrapper.httpx_client.request(
            "POST",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "delete-account"),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)


class AsyncDeleteAccountClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def delete(self) -> None:
        """
        Delete a linked account.

        ---
        from merge.client import AsyncMerge

        client = AsyncMerge(
            account_token="YOUR_ACCOUNT_TOKEN",
            api_key="YOUR_API_KEY",
        )
        await client.ats.delete_account.delete()
        """
        _response = await self._client_wrapper.httpx_client.request(
            "POST",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "delete-account"),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)
