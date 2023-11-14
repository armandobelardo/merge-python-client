# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing
import urllib.parse
from json.decoder import JSONDecodeError

import typing_extensions

from .....core.api_error import ApiError
from .....core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from .....core.datetime_utils import serialize_datetime
from .....core.jsonable_encoder import jsonable_encoder
from .....core.remove_none_from_dict import remove_none_from_dict
from ...types.contact import Contact
from ...types.contact_request import ContactRequest
from ...types.crm_contact_response import CrmContactResponse
from ...types.ignore_common_model_request import IgnoreCommonModelRequest
from ...types.meta_response import MetaResponse
from ...types.paginated_contact_list import PaginatedContactList
from ...types.paginated_remote_field_class_list import PaginatedRemoteFieldClassList
from ...types.patched_contact_request import PatchedContactRequest

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class ContactsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list(
        self,
        *,
        account_id: typing.Optional[str] = None,
        created_after: typing.Optional[dt.datetime] = None,
        created_before: typing.Optional[dt.datetime] = None,
        cursor: typing.Optional[str] = None,
        email_addresses: typing.Optional[str] = None,
        expand: typing.Optional[typing_extensions.Literal["account"]] = None,
        include_deleted_data: typing.Optional[bool] = None,
        include_remote_data: typing.Optional[bool] = None,
        include_remote_fields: typing.Optional[bool] = None,
        modified_after: typing.Optional[dt.datetime] = None,
        modified_before: typing.Optional[dt.datetime] = None,
        page_size: typing.Optional[int] = None,
        phone_numbers: typing.Optional[str] = None,
        remote_id: typing.Optional[str] = None,
    ) -> PaginatedContactList:
        """
        Returns a list of `Contact` objects.

        Parameters:
            - account_id: typing.Optional[str]. If provided, will only return contacts with this account.

            - created_after: typing.Optional[dt.datetime]. If provided, will only return objects created after this datetime.

            - created_before: typing.Optional[dt.datetime]. If provided, will only return objects created before this datetime.

            - cursor: typing.Optional[str]. The pagination cursor value.

            - email_addresses: typing.Optional[str]. If provided, will only return contacts matching the email addresses; multiple email_addresses can be separated by commas.

            - expand: typing.Optional[typing_extensions.Literal["account"]]. Which relations should be returned in expanded form. Multiple relation names should be comma separated without spaces.

            - include_deleted_data: typing.Optional[bool]. Whether to include data that was marked as deleted by third party webhooks.

            - include_remote_data: typing.Optional[bool]. Whether to include the original data Merge fetched from the third-party to produce these models.

            - include_remote_fields: typing.Optional[bool]. Whether to include all remote fields, including fields that Merge did not map to common models, in a normalized format.

            - modified_after: typing.Optional[dt.datetime]. If provided, only objects synced by Merge after this date time will be returned.

            - modified_before: typing.Optional[dt.datetime]. If provided, only objects synced by Merge before this date time will be returned.

            - page_size: typing.Optional[int]. Number of results to return per page.

            - phone_numbers: typing.Optional[str]. If provided, will only return contacts matching the phone numbers; multiple phone numbers can be separated by commas.

            - remote_id: typing.Optional[str]. The API provider's ID for the given object.
        ---
        from merge.client import Merge

        client = Merge(
            account_token="YOUR_ACCOUNT_TOKEN",
            api_key="YOUR_API_KEY",
        )
        client.crm.contacts.list(
            expand="account",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "api/crm/v1/contacts"),
            params=remove_none_from_dict(
                {
                    "account_id": account_id,
                    "created_after": serialize_datetime(created_after) if created_after is not None else None,
                    "created_before": serialize_datetime(created_before) if created_before is not None else None,
                    "cursor": cursor,
                    "email_addresses": email_addresses,
                    "expand": expand,
                    "include_deleted_data": include_deleted_data,
                    "include_remote_data": include_remote_data,
                    "include_remote_fields": include_remote_fields,
                    "modified_after": serialize_datetime(modified_after) if modified_after is not None else None,
                    "modified_before": serialize_datetime(modified_before) if modified_before is not None else None,
                    "page_size": page_size,
                    "phone_numbers": phone_numbers,
                    "remote_id": remote_id,
                }
            ),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(PaginatedContactList, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def create(
        self,
        *,
        is_debug_mode: typing.Optional[bool] = None,
        run_async: typing.Optional[bool] = None,
        model: ContactRequest,
    ) -> CrmContactResponse:
        """
        Creates a `Contact` object with the given values.

        Parameters:
            - is_debug_mode: typing.Optional[bool]. Whether to include debug fields (such as log file links) in the response.

            - run_async: typing.Optional[bool]. Whether or not third-party updates should be run asynchronously.

            - model: ContactRequest.
        ---
        import datetime

        from merge.client import Merge
        from merge.resources.crm import (
            AddressRequest,
            ContactRequest,
            EmailAddressRequest,
            PhoneNumberRequest,
        )

        client = Merge(
            account_token="YOUR_ACCOUNT_TOKEN",
            api_key="YOUR_API_KEY",
        )
        client.crm.contacts.create(
            model=ContactRequest(
                first_name="Gil",
                last_name="Feig",
                addresses=[
                    AddressRequest(
                        street_1="50 Bowling Green Dr",
                        street_2="Golden Gate Park",
                        city="San Francisco",
                        state="CA",
                        postal_code="94122",
                    )
                ],
                email_addresses=[
                    EmailAddressRequest(
                        email_address="merge_is_hiring@merge.dev",
                        email_address_type="Work",
                    )
                ],
                phone_numbers=[
                    PhoneNumberRequest(
                        phone_number="+3198675309",
                        phone_number_type="Mobile",
                    )
                ],
                last_activity_at=datetime.datetime.fromisoformat(
                    "2022-02-10 00:00:00+00:00",
                ),
            ),
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            "POST",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "api/crm/v1/contacts"),
            params=remove_none_from_dict({"is_debug_mode": is_debug_mode, "run_async": run_async}),
            json=jsonable_encoder({"model": model}),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(CrmContactResponse, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def retrieve(
        self,
        id: str,
        *,
        expand: typing.Optional[typing_extensions.Literal["account"]] = None,
        include_remote_data: typing.Optional[bool] = None,
        include_remote_fields: typing.Optional[bool] = None,
    ) -> Contact:
        """
        Returns a `Contact` object with the given `id`.

        Parameters:
            - id: str.

            - expand: typing.Optional[typing_extensions.Literal["account"]]. Which relations should be returned in expanded form. Multiple relation names should be comma separated without spaces.

            - include_remote_data: typing.Optional[bool]. Whether to include the original data Merge fetched from the third-party to produce these models.

            - include_remote_fields: typing.Optional[bool]. Whether to include all remote fields, including fields that Merge did not map to common models, in a normalized format.
        ---
        from merge.client import Merge

        client = Merge(
            account_token="YOUR_ACCOUNT_TOKEN",
            api_key="YOUR_API_KEY",
        )
        client.crm.contacts.retrieve(
            id="id",
            expand="account",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", f"api/crm/v1/contacts/{id}"),
            params=remove_none_from_dict(
                {
                    "expand": expand,
                    "include_remote_data": include_remote_data,
                    "include_remote_fields": include_remote_fields,
                }
            ),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(Contact, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def partial_update(
        self,
        id: str,
        *,
        is_debug_mode: typing.Optional[bool] = None,
        run_async: typing.Optional[bool] = None,
        model: PatchedContactRequest,
    ) -> CrmContactResponse:
        """
        Updates a `Contact` object with the given `id`.

        Parameters:
            - id: str.

            - is_debug_mode: typing.Optional[bool]. Whether to include debug fields (such as log file links) in the response.

            - run_async: typing.Optional[bool]. Whether or not third-party updates should be run asynchronously.

            - model: PatchedContactRequest.
        ---
        import datetime

        from merge.client import Merge
        from merge.resources.crm import (
            AddressRequest,
            EmailAddressRequest,
            PatchedContactRequest,
            PhoneNumberRequest,
        )

        client = Merge(
            account_token="YOUR_ACCOUNT_TOKEN",
            api_key="YOUR_API_KEY",
        )
        client.crm.contacts.partial_update(
            id="id",
            model=PatchedContactRequest(
                first_name="Gil",
                last_name="Feig",
                account="0958cbc6-6040-430a-848e-aafacbadf4ae",
                addresses=[
                    AddressRequest(
                        street_1="50 Bowling Green Dr",
                        street_2="Golden Gate Park",
                        city="San Francisco",
                        state="CA",
                        postal_code="94122",
                    )
                ],
                email_addresses=[
                    EmailAddressRequest(
                        email_address="merge_is_hiring@merge.dev",
                        email_address_type="Work",
                    )
                ],
                phone_numbers=[
                    PhoneNumberRequest(
                        phone_number="+3198675309",
                        phone_number_type="Mobile",
                    )
                ],
                last_activity_at=datetime.datetime.fromisoformat(
                    "2022-02-10 00:00:00+00:00",
                ),
            ),
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            "PATCH",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", f"api/crm/v1/contacts/{id}"),
            params=remove_none_from_dict({"is_debug_mode": is_debug_mode, "run_async": run_async}),
            json=jsonable_encoder({"model": model}),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(CrmContactResponse, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def ignore_create(self, model_id: str, *, request: IgnoreCommonModelRequest) -> None:
        """
        Ignores a specific row based on the `model_id` in the url. These records will have their properties set to null, and will not be updated in future syncs. The "reason" and "message" fields in the request body will be stored for audit purposes.

        Parameters:
            - model_id: str.

            - request: IgnoreCommonModelRequest.
        ---
        from merge.client import Merge
        from merge.resources.crm import IgnoreCommonModelRequest, ReasonEnum

        client = Merge(
            account_token="YOUR_ACCOUNT_TOKEN",
            api_key="YOUR_API_KEY",
        )
        client.crm.contacts.ignore_create(
            model_id="model-id",
            request=IgnoreCommonModelRequest(
                reason=ReasonEnum.GENERAL_CUSTOMER_REQUEST,
                message="deletion request by user id 51903790-7dfe-4053-8d63-5a10cc4ffd39",
            ),
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            "POST",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", f"api/crm/v1/contacts/ignore/{model_id}"),
            json=jsonable_encoder(request),
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

    def meta_patch_retrieve(self, id: str) -> MetaResponse:
        """
        Returns metadata for `CRMContact` PATCHs.

        Parameters:
            - id: str.
        ---
        from merge.client import Merge

        client = Merge(
            account_token="YOUR_ACCOUNT_TOKEN",
            api_key="YOUR_API_KEY",
        )
        client.crm.contacts.meta_patch_retrieve(
            id="id",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", f"api/crm/v1/contacts/meta/patch/{id}"),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(MetaResponse, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def meta_post_retrieve(self) -> MetaResponse:
        """
        Returns metadata for `CRMContact` POSTs.

        ---
        from merge.client import Merge

        client = Merge(
            account_token="YOUR_ACCOUNT_TOKEN",
            api_key="YOUR_API_KEY",
        )
        client.crm.contacts.meta_post_retrieve()
        """
        _response = self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "api/crm/v1/contacts/meta/post"),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(MetaResponse, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def remote_field_classes_list(
        self,
        *,
        cursor: typing.Optional[str] = None,
        include_deleted_data: typing.Optional[bool] = None,
        include_remote_data: typing.Optional[bool] = None,
        include_remote_fields: typing.Optional[bool] = None,
        page_size: typing.Optional[int] = None,
    ) -> PaginatedRemoteFieldClassList:
        """
        Returns a list of `RemoteFieldClass` objects.

        Parameters:
            - cursor: typing.Optional[str]. The pagination cursor value.

            - include_deleted_data: typing.Optional[bool]. Whether to include data that was marked as deleted by third party webhooks.

            - include_remote_data: typing.Optional[bool]. Whether to include the original data Merge fetched from the third-party to produce these models.

            - include_remote_fields: typing.Optional[bool]. Whether to include all remote fields, including fields that Merge did not map to common models, in a normalized format.

            - page_size: typing.Optional[int]. Number of results to return per page.
        ---
        from merge.client import Merge

        client = Merge(
            account_token="YOUR_ACCOUNT_TOKEN",
            api_key="YOUR_API_KEY",
        )
        client.crm.contacts.remote_field_classes_list()
        """
        _response = self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "api/crm/v1/contacts/remote-field-classes"),
            params=remove_none_from_dict(
                {
                    "cursor": cursor,
                    "include_deleted_data": include_deleted_data,
                    "include_remote_data": include_remote_data,
                    "include_remote_fields": include_remote_fields,
                    "page_size": page_size,
                }
            ),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(PaginatedRemoteFieldClassList, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)


class AsyncContactsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def list(
        self,
        *,
        account_id: typing.Optional[str] = None,
        created_after: typing.Optional[dt.datetime] = None,
        created_before: typing.Optional[dt.datetime] = None,
        cursor: typing.Optional[str] = None,
        email_addresses: typing.Optional[str] = None,
        expand: typing.Optional[typing_extensions.Literal["account"]] = None,
        include_deleted_data: typing.Optional[bool] = None,
        include_remote_data: typing.Optional[bool] = None,
        include_remote_fields: typing.Optional[bool] = None,
        modified_after: typing.Optional[dt.datetime] = None,
        modified_before: typing.Optional[dt.datetime] = None,
        page_size: typing.Optional[int] = None,
        phone_numbers: typing.Optional[str] = None,
        remote_id: typing.Optional[str] = None,
    ) -> PaginatedContactList:
        """
        Returns a list of `Contact` objects.

        Parameters:
            - account_id: typing.Optional[str]. If provided, will only return contacts with this account.

            - created_after: typing.Optional[dt.datetime]. If provided, will only return objects created after this datetime.

            - created_before: typing.Optional[dt.datetime]. If provided, will only return objects created before this datetime.

            - cursor: typing.Optional[str]. The pagination cursor value.

            - email_addresses: typing.Optional[str]. If provided, will only return contacts matching the email addresses; multiple email_addresses can be separated by commas.

            - expand: typing.Optional[typing_extensions.Literal["account"]]. Which relations should be returned in expanded form. Multiple relation names should be comma separated without spaces.

            - include_deleted_data: typing.Optional[bool]. Whether to include data that was marked as deleted by third party webhooks.

            - include_remote_data: typing.Optional[bool]. Whether to include the original data Merge fetched from the third-party to produce these models.

            - include_remote_fields: typing.Optional[bool]. Whether to include all remote fields, including fields that Merge did not map to common models, in a normalized format.

            - modified_after: typing.Optional[dt.datetime]. If provided, only objects synced by Merge after this date time will be returned.

            - modified_before: typing.Optional[dt.datetime]. If provided, only objects synced by Merge before this date time will be returned.

            - page_size: typing.Optional[int]. Number of results to return per page.

            - phone_numbers: typing.Optional[str]. If provided, will only return contacts matching the phone numbers; multiple phone numbers can be separated by commas.

            - remote_id: typing.Optional[str]. The API provider's ID for the given object.
        ---
        from merge.client import AsyncMerge

        client = AsyncMerge(
            account_token="YOUR_ACCOUNT_TOKEN",
            api_key="YOUR_API_KEY",
        )
        await client.crm.contacts.list(
            expand="account",
        )
        """
        _response = await self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "api/crm/v1/contacts"),
            params=remove_none_from_dict(
                {
                    "account_id": account_id,
                    "created_after": serialize_datetime(created_after) if created_after is not None else None,
                    "created_before": serialize_datetime(created_before) if created_before is not None else None,
                    "cursor": cursor,
                    "email_addresses": email_addresses,
                    "expand": expand,
                    "include_deleted_data": include_deleted_data,
                    "include_remote_data": include_remote_data,
                    "include_remote_fields": include_remote_fields,
                    "modified_after": serialize_datetime(modified_after) if modified_after is not None else None,
                    "modified_before": serialize_datetime(modified_before) if modified_before is not None else None,
                    "page_size": page_size,
                    "phone_numbers": phone_numbers,
                    "remote_id": remote_id,
                }
            ),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(PaginatedContactList, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def create(
        self,
        *,
        is_debug_mode: typing.Optional[bool] = None,
        run_async: typing.Optional[bool] = None,
        model: ContactRequest,
    ) -> CrmContactResponse:
        """
        Creates a `Contact` object with the given values.

        Parameters:
            - is_debug_mode: typing.Optional[bool]. Whether to include debug fields (such as log file links) in the response.

            - run_async: typing.Optional[bool]. Whether or not third-party updates should be run asynchronously.

            - model: ContactRequest.
        ---
        import datetime

        from merge.client import AsyncMerge
        from merge.resources.crm import (
            AddressRequest,
            ContactRequest,
            EmailAddressRequest,
            PhoneNumberRequest,
        )

        client = AsyncMerge(
            account_token="YOUR_ACCOUNT_TOKEN",
            api_key="YOUR_API_KEY",
        )
        await client.crm.contacts.create(
            model=ContactRequest(
                first_name="Gil",
                last_name="Feig",
                addresses=[
                    AddressRequest(
                        street_1="50 Bowling Green Dr",
                        street_2="Golden Gate Park",
                        city="San Francisco",
                        state="CA",
                        postal_code="94122",
                    )
                ],
                email_addresses=[
                    EmailAddressRequest(
                        email_address="merge_is_hiring@merge.dev",
                        email_address_type="Work",
                    )
                ],
                phone_numbers=[
                    PhoneNumberRequest(
                        phone_number="+3198675309",
                        phone_number_type="Mobile",
                    )
                ],
                last_activity_at=datetime.datetime.fromisoformat(
                    "2022-02-10 00:00:00+00:00",
                ),
            ),
        )
        """
        _response = await self._client_wrapper.httpx_client.request(
            "POST",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "api/crm/v1/contacts"),
            params=remove_none_from_dict({"is_debug_mode": is_debug_mode, "run_async": run_async}),
            json=jsonable_encoder({"model": model}),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(CrmContactResponse, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def retrieve(
        self,
        id: str,
        *,
        expand: typing.Optional[typing_extensions.Literal["account"]] = None,
        include_remote_data: typing.Optional[bool] = None,
        include_remote_fields: typing.Optional[bool] = None,
    ) -> Contact:
        """
        Returns a `Contact` object with the given `id`.

        Parameters:
            - id: str.

            - expand: typing.Optional[typing_extensions.Literal["account"]]. Which relations should be returned in expanded form. Multiple relation names should be comma separated without spaces.

            - include_remote_data: typing.Optional[bool]. Whether to include the original data Merge fetched from the third-party to produce these models.

            - include_remote_fields: typing.Optional[bool]. Whether to include all remote fields, including fields that Merge did not map to common models, in a normalized format.
        ---
        from merge.client import AsyncMerge

        client = AsyncMerge(
            account_token="YOUR_ACCOUNT_TOKEN",
            api_key="YOUR_API_KEY",
        )
        await client.crm.contacts.retrieve(
            id="id",
            expand="account",
        )
        """
        _response = await self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", f"api/crm/v1/contacts/{id}"),
            params=remove_none_from_dict(
                {
                    "expand": expand,
                    "include_remote_data": include_remote_data,
                    "include_remote_fields": include_remote_fields,
                }
            ),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(Contact, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def partial_update(
        self,
        id: str,
        *,
        is_debug_mode: typing.Optional[bool] = None,
        run_async: typing.Optional[bool] = None,
        model: PatchedContactRequest,
    ) -> CrmContactResponse:
        """
        Updates a `Contact` object with the given `id`.

        Parameters:
            - id: str.

            - is_debug_mode: typing.Optional[bool]. Whether to include debug fields (such as log file links) in the response.

            - run_async: typing.Optional[bool]. Whether or not third-party updates should be run asynchronously.

            - model: PatchedContactRequest.
        ---
        import datetime

        from merge.client import AsyncMerge
        from merge.resources.crm import (
            AddressRequest,
            EmailAddressRequest,
            PatchedContactRequest,
            PhoneNumberRequest,
        )

        client = AsyncMerge(
            account_token="YOUR_ACCOUNT_TOKEN",
            api_key="YOUR_API_KEY",
        )
        await client.crm.contacts.partial_update(
            id="id",
            model=PatchedContactRequest(
                first_name="Gil",
                last_name="Feig",
                account="0958cbc6-6040-430a-848e-aafacbadf4ae",
                addresses=[
                    AddressRequest(
                        street_1="50 Bowling Green Dr",
                        street_2="Golden Gate Park",
                        city="San Francisco",
                        state="CA",
                        postal_code="94122",
                    )
                ],
                email_addresses=[
                    EmailAddressRequest(
                        email_address="merge_is_hiring@merge.dev",
                        email_address_type="Work",
                    )
                ],
                phone_numbers=[
                    PhoneNumberRequest(
                        phone_number="+3198675309",
                        phone_number_type="Mobile",
                    )
                ],
                last_activity_at=datetime.datetime.fromisoformat(
                    "2022-02-10 00:00:00+00:00",
                ),
            ),
        )
        """
        _response = await self._client_wrapper.httpx_client.request(
            "PATCH",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", f"api/crm/v1/contacts/{id}"),
            params=remove_none_from_dict({"is_debug_mode": is_debug_mode, "run_async": run_async}),
            json=jsonable_encoder({"model": model}),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(CrmContactResponse, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def ignore_create(self, model_id: str, *, request: IgnoreCommonModelRequest) -> None:
        """
        Ignores a specific row based on the `model_id` in the url. These records will have their properties set to null, and will not be updated in future syncs. The "reason" and "message" fields in the request body will be stored for audit purposes.

        Parameters:
            - model_id: str.

            - request: IgnoreCommonModelRequest.
        ---
        from merge.client import AsyncMerge
        from merge.resources.crm import IgnoreCommonModelRequest, ReasonEnum

        client = AsyncMerge(
            account_token="YOUR_ACCOUNT_TOKEN",
            api_key="YOUR_API_KEY",
        )
        await client.crm.contacts.ignore_create(
            model_id="model-id",
            request=IgnoreCommonModelRequest(
                reason=ReasonEnum.GENERAL_CUSTOMER_REQUEST,
                message="deletion request by user id 51903790-7dfe-4053-8d63-5a10cc4ffd39",
            ),
        )
        """
        _response = await self._client_wrapper.httpx_client.request(
            "POST",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", f"api/crm/v1/contacts/ignore/{model_id}"),
            json=jsonable_encoder(request),
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

    async def meta_patch_retrieve(self, id: str) -> MetaResponse:
        """
        Returns metadata for `CRMContact` PATCHs.

        Parameters:
            - id: str.
        ---
        from merge.client import AsyncMerge

        client = AsyncMerge(
            account_token="YOUR_ACCOUNT_TOKEN",
            api_key="YOUR_API_KEY",
        )
        await client.crm.contacts.meta_patch_retrieve(
            id="id",
        )
        """
        _response = await self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", f"api/crm/v1/contacts/meta/patch/{id}"),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(MetaResponse, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def meta_post_retrieve(self) -> MetaResponse:
        """
        Returns metadata for `CRMContact` POSTs.

        ---
        from merge.client import AsyncMerge

        client = AsyncMerge(
            account_token="YOUR_ACCOUNT_TOKEN",
            api_key="YOUR_API_KEY",
        )
        await client.crm.contacts.meta_post_retrieve()
        """
        _response = await self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "api/crm/v1/contacts/meta/post"),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(MetaResponse, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def remote_field_classes_list(
        self,
        *,
        cursor: typing.Optional[str] = None,
        include_deleted_data: typing.Optional[bool] = None,
        include_remote_data: typing.Optional[bool] = None,
        include_remote_fields: typing.Optional[bool] = None,
        page_size: typing.Optional[int] = None,
    ) -> PaginatedRemoteFieldClassList:
        """
        Returns a list of `RemoteFieldClass` objects.

        Parameters:
            - cursor: typing.Optional[str]. The pagination cursor value.

            - include_deleted_data: typing.Optional[bool]. Whether to include data that was marked as deleted by third party webhooks.

            - include_remote_data: typing.Optional[bool]. Whether to include the original data Merge fetched from the third-party to produce these models.

            - include_remote_fields: typing.Optional[bool]. Whether to include all remote fields, including fields that Merge did not map to common models, in a normalized format.

            - page_size: typing.Optional[int]. Number of results to return per page.
        ---
        from merge.client import AsyncMerge

        client = AsyncMerge(
            account_token="YOUR_ACCOUNT_TOKEN",
            api_key="YOUR_API_KEY",
        )
        await client.crm.contacts.remote_field_classes_list()
        """
        _response = await self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "api/crm/v1/contacts/remote-field-classes"),
            params=remove_none_from_dict(
                {
                    "cursor": cursor,
                    "include_deleted_data": include_deleted_data,
                    "include_remote_data": include_remote_data,
                    "include_remote_fields": include_remote_fields,
                    "page_size": page_size,
                }
            ),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(PaginatedRemoteFieldClassList, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)
