# This file was auto-generated by Fern from our API Definition.

from ...core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ...environment import MergeEnvironment
from .resources.account_details.client import AccountDetailsClient, AsyncAccountDetailsClient
from .resources.account_token.client import AccountTokenClient, AsyncAccountTokenClient
from .resources.accounts.client import AccountsClient, AsyncAccountsClient
from .resources.association_types.client import AssociationTypesClient, AsyncAssociationTypesClient
from .resources.associations.client import AssociationsClient, AsyncAssociationsClient
from .resources.async_passthrough.client import AsyncAsyncPassthroughClient
from .resources.async_passthrough.client import (
    AsyncPassthroughClient as resources_crm_resources_async_passthrough_client_AsyncPassthroughClient,
)
from .resources.available_actions.client import AsyncAvailableActionsClient, AvailableActionsClient
from .resources.contacts.client import AsyncContactsClient, ContactsClient
from .resources.custom_object_classes.client import AsyncCustomObjectClassesClient, CustomObjectClassesClient
from .resources.custom_objects.client import AsyncCustomObjectsClient, CustomObjectsClient
from .resources.delete_account.client import AsyncDeleteAccountClient, DeleteAccountClient
from .resources.engagement_types.client import AsyncEngagementTypesClient, EngagementTypesClient
from .resources.engagements.client import AsyncEngagementsClient, EngagementsClient
from .resources.force_resync.client import AsyncForceResyncClient, ForceResyncClient
from .resources.generate_key.client import AsyncGenerateKeyClient, GenerateKeyClient
from .resources.issues.client import AsyncIssuesClient, IssuesClient
from .resources.leads.client import AsyncLeadsClient, LeadsClient
from .resources.link_token.client import AsyncLinkTokenClient, LinkTokenClient
from .resources.linked_accounts.client import AsyncLinkedAccountsClient, LinkedAccountsClient
from .resources.notes.client import AsyncNotesClient, NotesClient
from .resources.opportunities.client import AsyncOpportunitiesClient, OpportunitiesClient
from .resources.passthrough.client import (
    AsyncPassthroughClient as resources_crm_resources_passthrough_client_AsyncPassthroughClient,
)
from .resources.passthrough.client import PassthroughClient
from .resources.regenerate_key.client import AsyncRegenerateKeyClient, RegenerateKeyClient
from .resources.selective_sync.client import AsyncSelectiveSyncClient, SelectiveSyncClient
from .resources.stages.client import AsyncStagesClient, StagesClient
from .resources.sync_status.client import AsyncSyncStatusClient, SyncStatusClient
from .resources.tasks.client import AsyncTasksClient, TasksClient
from .resources.users.client import AsyncUsersClient, UsersClient
from .resources.webhook_receivers.client import AsyncWebhookReceiversClient, WebhookReceiversClient


class CrmClient:
    def __init__(
        self, *, environment: MergeEnvironment = MergeEnvironment.PRODUCTION, client_wrapper: SyncClientWrapper
    ):
        self._environment = environment
        self._client_wrapper = client_wrapper
        self.account_details = AccountDetailsClient(environment=self._environment, client_wrapper=self._client_wrapper)
        self.account_token = AccountTokenClient(environment=self._environment, client_wrapper=self._client_wrapper)
        self.accounts = AccountsClient(environment=self._environment, client_wrapper=self._client_wrapper)
        self.async_passthrough = resources_crm_resources_async_passthrough_client_AsyncPassthroughClient(
            environment=self._environment, client_wrapper=self._client_wrapper
        )
        self.available_actions = AvailableActionsClient(
            environment=self._environment, client_wrapper=self._client_wrapper
        )
        self.contacts = ContactsClient(environment=self._environment, client_wrapper=self._client_wrapper)
        self.custom_object_classes = CustomObjectClassesClient(
            environment=self._environment, client_wrapper=self._client_wrapper
        )
        self.association_types = AssociationTypesClient(
            environment=self._environment, client_wrapper=self._client_wrapper
        )
        self.custom_objects = CustomObjectsClient(environment=self._environment, client_wrapper=self._client_wrapper)
        self.associations = AssociationsClient(environment=self._environment, client_wrapper=self._client_wrapper)
        self.delete_account = DeleteAccountClient(environment=self._environment, client_wrapper=self._client_wrapper)
        self.engagement_types = EngagementTypesClient(
            environment=self._environment, client_wrapper=self._client_wrapper
        )
        self.engagements = EngagementsClient(environment=self._environment, client_wrapper=self._client_wrapper)
        self.generate_key = GenerateKeyClient(environment=self._environment, client_wrapper=self._client_wrapper)
        self.issues = IssuesClient(environment=self._environment, client_wrapper=self._client_wrapper)
        self.leads = LeadsClient(environment=self._environment, client_wrapper=self._client_wrapper)
        self.link_token = LinkTokenClient(environment=self._environment, client_wrapper=self._client_wrapper)
        self.linked_accounts = LinkedAccountsClient(environment=self._environment, client_wrapper=self._client_wrapper)
        self.notes = NotesClient(environment=self._environment, client_wrapper=self._client_wrapper)
        self.opportunities = OpportunitiesClient(environment=self._environment, client_wrapper=self._client_wrapper)
        self.passthrough = PassthroughClient(environment=self._environment, client_wrapper=self._client_wrapper)
        self.regenerate_key = RegenerateKeyClient(environment=self._environment, client_wrapper=self._client_wrapper)
        self.selective_sync = SelectiveSyncClient(environment=self._environment, client_wrapper=self._client_wrapper)
        self.stages = StagesClient(environment=self._environment, client_wrapper=self._client_wrapper)
        self.sync_status = SyncStatusClient(environment=self._environment, client_wrapper=self._client_wrapper)
        self.force_resync = ForceResyncClient(environment=self._environment, client_wrapper=self._client_wrapper)
        self.tasks = TasksClient(environment=self._environment, client_wrapper=self._client_wrapper)
        self.users = UsersClient(environment=self._environment, client_wrapper=self._client_wrapper)
        self.webhook_receivers = WebhookReceiversClient(
            environment=self._environment, client_wrapper=self._client_wrapper
        )


class AsyncCrmClient:
    def __init__(
        self, *, environment: MergeEnvironment = MergeEnvironment.PRODUCTION, client_wrapper: AsyncClientWrapper
    ):
        self._environment = environment
        self._client_wrapper = client_wrapper
        self.account_details = AsyncAccountDetailsClient(
            environment=self._environment, client_wrapper=self._client_wrapper
        )
        self.account_token = AsyncAccountTokenClient(environment=self._environment, client_wrapper=self._client_wrapper)
        self.accounts = AsyncAccountsClient(environment=self._environment, client_wrapper=self._client_wrapper)
        self.async_passthrough = AsyncAsyncPassthroughClient(
            environment=self._environment, client_wrapper=self._client_wrapper
        )
        self.available_actions = AsyncAvailableActionsClient(
            environment=self._environment, client_wrapper=self._client_wrapper
        )
        self.contacts = AsyncContactsClient(environment=self._environment, client_wrapper=self._client_wrapper)
        self.custom_object_classes = AsyncCustomObjectClassesClient(
            environment=self._environment, client_wrapper=self._client_wrapper
        )
        self.association_types = AsyncAssociationTypesClient(
            environment=self._environment, client_wrapper=self._client_wrapper
        )
        self.custom_objects = AsyncCustomObjectsClient(
            environment=self._environment, client_wrapper=self._client_wrapper
        )
        self.associations = AsyncAssociationsClient(environment=self._environment, client_wrapper=self._client_wrapper)
        self.delete_account = AsyncDeleteAccountClient(
            environment=self._environment, client_wrapper=self._client_wrapper
        )
        self.engagement_types = AsyncEngagementTypesClient(
            environment=self._environment, client_wrapper=self._client_wrapper
        )
        self.engagements = AsyncEngagementsClient(environment=self._environment, client_wrapper=self._client_wrapper)
        self.generate_key = AsyncGenerateKeyClient(environment=self._environment, client_wrapper=self._client_wrapper)
        self.issues = AsyncIssuesClient(environment=self._environment, client_wrapper=self._client_wrapper)
        self.leads = AsyncLeadsClient(environment=self._environment, client_wrapper=self._client_wrapper)
        self.link_token = AsyncLinkTokenClient(environment=self._environment, client_wrapper=self._client_wrapper)
        self.linked_accounts = AsyncLinkedAccountsClient(
            environment=self._environment, client_wrapper=self._client_wrapper
        )
        self.notes = AsyncNotesClient(environment=self._environment, client_wrapper=self._client_wrapper)
        self.opportunities = AsyncOpportunitiesClient(
            environment=self._environment, client_wrapper=self._client_wrapper
        )
        self.passthrough = resources_crm_resources_passthrough_client_AsyncPassthroughClient(
            environment=self._environment, client_wrapper=self._client_wrapper
        )
        self.regenerate_key = AsyncRegenerateKeyClient(
            environment=self._environment, client_wrapper=self._client_wrapper
        )
        self.selective_sync = AsyncSelectiveSyncClient(
            environment=self._environment, client_wrapper=self._client_wrapper
        )
        self.stages = AsyncStagesClient(environment=self._environment, client_wrapper=self._client_wrapper)
        self.sync_status = AsyncSyncStatusClient(environment=self._environment, client_wrapper=self._client_wrapper)
        self.force_resync = AsyncForceResyncClient(environment=self._environment, client_wrapper=self._client_wrapper)
        self.tasks = AsyncTasksClient(environment=self._environment, client_wrapper=self._client_wrapper)
        self.users = AsyncUsersClient(environment=self._environment, client_wrapper=self._client_wrapper)
        self.webhook_receivers = AsyncWebhookReceiversClient(
            environment=self._environment, client_wrapper=self._client_wrapper
        )
