# This file was auto-generated by Fern from our API Definition.

import typing

import httpx


class BaseClientWrapper:
    def __init__(
        self,
        *,
        account_token: typing.Optional[str] = None,
        api_key: typing.Union[str, typing.Callable[[], str]],
        base_url: str,
    ):
        self._account_token = account_token
        self._api_key = api_key
        self._base_url = base_url

    def get_headers(self) -> typing.Dict[str, str]:
        headers: typing.Dict[str, str] = {
            "X-Fern-Language": "Python",
            "X-Fern-SDK-Name": "MergePythonClient",
            "X-Fern-SDK-Version": "1.0.3",
        }
        if self._account_token is not None:
            headers["X-Account-Token"] = self._account_token
        headers["Authorization"] = f"Bearer {self._get_api_key()}"
        return headers

    def _get_api_key(self) -> str:
        if isinstance(self._api_key, str):
            return self._api_key
        else:
            return self._api_key()

    def get_base_url(self) -> str:
        return self._base_url


class SyncClientWrapper(BaseClientWrapper):
    def __init__(
        self,
        *,
        account_token: typing.Optional[str] = None,
        api_key: typing.Union[str, typing.Callable[[], str]],
        base_url: str,
        httpx_client: httpx.Client,
    ):
        super().__init__(account_token=account_token, api_key=api_key, base_url=base_url)
        self.httpx_client = httpx_client


class AsyncClientWrapper(BaseClientWrapper):
    def __init__(
        self,
        *,
        account_token: typing.Optional[str] = None,
        api_key: typing.Union[str, typing.Callable[[], str]],
        base_url: str,
        httpx_client: httpx.AsyncClient,
    ):
        super().__init__(account_token=account_token, api_key=api_key, base_url=base_url)
        self.httpx_client = httpx_client
