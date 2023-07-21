# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class TicketsListRequestExpand(str, enum.Enum):
    ACCOUNT = "account"
    ACCOUNT_CONTACT = "account,contact"
    ACCOUNT_CONTACT_CREATOR = "account,contact,creator"
    ACCOUNT_CONTACT_CREATOR_PARENT_TICKET = "account,contact,creator,parent_ticket"
    ACCOUNT_CONTACT_PARENT_TICKET = "account,contact,parent_ticket"
    ACCOUNT_CREATOR = "account,creator"
    ACCOUNT_CREATOR_PARENT_TICKET = "account,creator,parent_ticket"
    ACCOUNT_PARENT_TICKET = "account,parent_ticket"
    ASSIGNEES = "assignees"
    ASSIGNEES_ACCOUNT = "assignees,account"
    ASSIGNEES_ACCOUNT_CONTACT = "assignees,account,contact"
    ASSIGNEES_ACCOUNT_CONTACT_CREATOR = "assignees,account,contact,creator"
    ASSIGNEES_ACCOUNT_CONTACT_CREATOR_PARENT_TICKET = "assignees,account,contact,creator,parent_ticket"
    ASSIGNEES_ACCOUNT_CONTACT_PARENT_TICKET = "assignees,account,contact,parent_ticket"
    ASSIGNEES_ACCOUNT_CREATOR = "assignees,account,creator"
    ASSIGNEES_ACCOUNT_CREATOR_PARENT_TICKET = "assignees,account,creator,parent_ticket"
    ASSIGNEES_ACCOUNT_PARENT_TICKET = "assignees,account,parent_ticket"
    ASSIGNEES_COLLECTIONS = "assignees,collections"
    ASSIGNEES_COLLECTIONS_ACCOUNT = "assignees,collections,account"
    ASSIGNEES_COLLECTIONS_ACCOUNT_CONTACT = "assignees,collections,account,contact"
    ASSIGNEES_COLLECTIONS_ACCOUNT_CONTACT_CREATOR = "assignees,collections,account,contact,creator"
    ASSIGNEES_COLLECTIONS_ACCOUNT_CONTACT_CREATOR_PARENT_TICKET = (
        "assignees,collections,account,contact,creator,parent_ticket"
    )
    ASSIGNEES_COLLECTIONS_ACCOUNT_CONTACT_PARENT_TICKET = "assignees,collections,account,contact,parent_ticket"
    ASSIGNEES_COLLECTIONS_ACCOUNT_CREATOR = "assignees,collections,account,creator"
    ASSIGNEES_COLLECTIONS_ACCOUNT_CREATOR_PARENT_TICKET = "assignees,collections,account,creator,parent_ticket"
    ASSIGNEES_COLLECTIONS_ACCOUNT_PARENT_TICKET = "assignees,collections,account,parent_ticket"
    ASSIGNEES_COLLECTIONS_CONTACT = "assignees,collections,contact"
    ASSIGNEES_COLLECTIONS_CONTACT_CREATOR = "assignees,collections,contact,creator"
    ASSIGNEES_COLLECTIONS_CONTACT_CREATOR_PARENT_TICKET = "assignees,collections,contact,creator,parent_ticket"
    ASSIGNEES_COLLECTIONS_CONTACT_PARENT_TICKET = "assignees,collections,contact,parent_ticket"
    ASSIGNEES_COLLECTIONS_CREATOR = "assignees,collections,creator"
    ASSIGNEES_COLLECTIONS_CREATOR_PARENT_TICKET = "assignees,collections,creator,parent_ticket"
    ASSIGNEES_COLLECTIONS_PARENT_TICKET = "assignees,collections,parent_ticket"
    ASSIGNEES_CONTACT = "assignees,contact"
    ASSIGNEES_CONTACT_CREATOR = "assignees,contact,creator"
    ASSIGNEES_CONTACT_CREATOR_PARENT_TICKET = "assignees,contact,creator,parent_ticket"
    ASSIGNEES_CONTACT_PARENT_TICKET = "assignees,contact,parent_ticket"
    ASSIGNEES_CREATOR = "assignees,creator"
    ASSIGNEES_CREATOR_PARENT_TICKET = "assignees,creator,parent_ticket"
    ASSIGNEES_PARENT_TICKET = "assignees,parent_ticket"
    ATTACHMENTS = "attachments"
    ATTACHMENTS_ACCOUNT = "attachments,account"
    ATTACHMENTS_ACCOUNT_CONTACT = "attachments,account,contact"
    ATTACHMENTS_ACCOUNT_CONTACT_CREATOR = "attachments,account,contact,creator"
    ATTACHMENTS_ACCOUNT_CONTACT_CREATOR_PARENT_TICKET = "attachments,account,contact,creator,parent_ticket"
    ATTACHMENTS_ACCOUNT_CONTACT_PARENT_TICKET = "attachments,account,contact,parent_ticket"
    ATTACHMENTS_ACCOUNT_CREATOR = "attachments,account,creator"
    ATTACHMENTS_ACCOUNT_CREATOR_PARENT_TICKET = "attachments,account,creator,parent_ticket"
    ATTACHMENTS_ACCOUNT_PARENT_TICKET = "attachments,account,parent_ticket"
    ATTACHMENTS_ASSIGNEES = "attachments,assignees"
    ATTACHMENTS_ASSIGNEES_ACCOUNT = "attachments,assignees,account"
    ATTACHMENTS_ASSIGNEES_ACCOUNT_CONTACT = "attachments,assignees,account,contact"
    ATTACHMENTS_ASSIGNEES_ACCOUNT_CONTACT_CREATOR = "attachments,assignees,account,contact,creator"
    ATTACHMENTS_ASSIGNEES_ACCOUNT_CONTACT_CREATOR_PARENT_TICKET = (
        "attachments,assignees,account,contact,creator,parent_ticket"
    )
    ATTACHMENTS_ASSIGNEES_ACCOUNT_CONTACT_PARENT_TICKET = "attachments,assignees,account,contact,parent_ticket"
    ATTACHMENTS_ASSIGNEES_ACCOUNT_CREATOR = "attachments,assignees,account,creator"
    ATTACHMENTS_ASSIGNEES_ACCOUNT_CREATOR_PARENT_TICKET = "attachments,assignees,account,creator,parent_ticket"
    ATTACHMENTS_ASSIGNEES_ACCOUNT_PARENT_TICKET = "attachments,assignees,account,parent_ticket"
    ATTACHMENTS_ASSIGNEES_COLLECTIONS = "attachments,assignees,collections"
    ATTACHMENTS_ASSIGNEES_COLLECTIONS_ACCOUNT = "attachments,assignees,collections,account"
    ATTACHMENTS_ASSIGNEES_COLLECTIONS_ACCOUNT_CONTACT = "attachments,assignees,collections,account,contact"
    ATTACHMENTS_ASSIGNEES_COLLECTIONS_ACCOUNT_CONTACT_CREATOR = (
        "attachments,assignees,collections,account,contact,creator"
    )
    ATTACHMENTS_ASSIGNEES_COLLECTIONS_ACCOUNT_CONTACT_CREATOR_PARENT_TICKET = (
        "attachments,assignees,collections,account,contact,creator,parent_ticket"
    )
    ATTACHMENTS_ASSIGNEES_COLLECTIONS_ACCOUNT_CONTACT_PARENT_TICKET = (
        "attachments,assignees,collections,account,contact,parent_ticket"
    )
    ATTACHMENTS_ASSIGNEES_COLLECTIONS_ACCOUNT_CREATOR = "attachments,assignees,collections,account,creator"
    ATTACHMENTS_ASSIGNEES_COLLECTIONS_ACCOUNT_CREATOR_PARENT_TICKET = (
        "attachments,assignees,collections,account,creator,parent_ticket"
    )
    ATTACHMENTS_ASSIGNEES_COLLECTIONS_ACCOUNT_PARENT_TICKET = "attachments,assignees,collections,account,parent_ticket"
    ATTACHMENTS_ASSIGNEES_COLLECTIONS_CONTACT = "attachments,assignees,collections,contact"
    ATTACHMENTS_ASSIGNEES_COLLECTIONS_CONTACT_CREATOR = "attachments,assignees,collections,contact,creator"
    ATTACHMENTS_ASSIGNEES_COLLECTIONS_CONTACT_CREATOR_PARENT_TICKET = (
        "attachments,assignees,collections,contact,creator,parent_ticket"
    )
    ATTACHMENTS_ASSIGNEES_COLLECTIONS_CONTACT_PARENT_TICKET = "attachments,assignees,collections,contact,parent_ticket"
    ATTACHMENTS_ASSIGNEES_COLLECTIONS_CREATOR = "attachments,assignees,collections,creator"
    ATTACHMENTS_ASSIGNEES_COLLECTIONS_CREATOR_PARENT_TICKET = "attachments,assignees,collections,creator,parent_ticket"
    ATTACHMENTS_ASSIGNEES_COLLECTIONS_PARENT_TICKET = "attachments,assignees,collections,parent_ticket"
    ATTACHMENTS_ASSIGNEES_CONTACT = "attachments,assignees,contact"
    ATTACHMENTS_ASSIGNEES_CONTACT_CREATOR = "attachments,assignees,contact,creator"
    ATTACHMENTS_ASSIGNEES_CONTACT_CREATOR_PARENT_TICKET = "attachments,assignees,contact,creator,parent_ticket"
    ATTACHMENTS_ASSIGNEES_CONTACT_PARENT_TICKET = "attachments,assignees,contact,parent_ticket"
    ATTACHMENTS_ASSIGNEES_CREATOR = "attachments,assignees,creator"
    ATTACHMENTS_ASSIGNEES_CREATOR_PARENT_TICKET = "attachments,assignees,creator,parent_ticket"
    ATTACHMENTS_ASSIGNEES_PARENT_TICKET = "attachments,assignees,parent_ticket"
    ATTACHMENTS_COLLECTIONS = "attachments,collections"
    ATTACHMENTS_COLLECTIONS_ACCOUNT = "attachments,collections,account"
    ATTACHMENTS_COLLECTIONS_ACCOUNT_CONTACT = "attachments,collections,account,contact"
    ATTACHMENTS_COLLECTIONS_ACCOUNT_CONTACT_CREATOR = "attachments,collections,account,contact,creator"
    ATTACHMENTS_COLLECTIONS_ACCOUNT_CONTACT_CREATOR_PARENT_TICKET = (
        "attachments,collections,account,contact,creator,parent_ticket"
    )
    ATTACHMENTS_COLLECTIONS_ACCOUNT_CONTACT_PARENT_TICKET = "attachments,collections,account,contact,parent_ticket"
    ATTACHMENTS_COLLECTIONS_ACCOUNT_CREATOR = "attachments,collections,account,creator"
    ATTACHMENTS_COLLECTIONS_ACCOUNT_CREATOR_PARENT_TICKET = "attachments,collections,account,creator,parent_ticket"
    ATTACHMENTS_COLLECTIONS_ACCOUNT_PARENT_TICKET = "attachments,collections,account,parent_ticket"
    ATTACHMENTS_COLLECTIONS_CONTACT = "attachments,collections,contact"
    ATTACHMENTS_COLLECTIONS_CONTACT_CREATOR = "attachments,collections,contact,creator"
    ATTACHMENTS_COLLECTIONS_CONTACT_CREATOR_PARENT_TICKET = "attachments,collections,contact,creator,parent_ticket"
    ATTACHMENTS_COLLECTIONS_CONTACT_PARENT_TICKET = "attachments,collections,contact,parent_ticket"
    ATTACHMENTS_COLLECTIONS_CREATOR = "attachments,collections,creator"
    ATTACHMENTS_COLLECTIONS_CREATOR_PARENT_TICKET = "attachments,collections,creator,parent_ticket"
    ATTACHMENTS_COLLECTIONS_PARENT_TICKET = "attachments,collections,parent_ticket"
    ATTACHMENTS_CONTACT = "attachments,contact"
    ATTACHMENTS_CONTACT_CREATOR = "attachments,contact,creator"
    ATTACHMENTS_CONTACT_CREATOR_PARENT_TICKET = "attachments,contact,creator,parent_ticket"
    ATTACHMENTS_CONTACT_PARENT_TICKET = "attachments,contact,parent_ticket"
    ATTACHMENTS_CREATOR = "attachments,creator"
    ATTACHMENTS_CREATOR_PARENT_TICKET = "attachments,creator,parent_ticket"
    ATTACHMENTS_PARENT_TICKET = "attachments,parent_ticket"
    COLLECTIONS = "collections"
    COLLECTIONS_ACCOUNT = "collections,account"
    COLLECTIONS_ACCOUNT_CONTACT = "collections,account,contact"
    COLLECTIONS_ACCOUNT_CONTACT_CREATOR = "collections,account,contact,creator"
    COLLECTIONS_ACCOUNT_CONTACT_CREATOR_PARENT_TICKET = "collections,account,contact,creator,parent_ticket"
    COLLECTIONS_ACCOUNT_CONTACT_PARENT_TICKET = "collections,account,contact,parent_ticket"
    COLLECTIONS_ACCOUNT_CREATOR = "collections,account,creator"
    COLLECTIONS_ACCOUNT_CREATOR_PARENT_TICKET = "collections,account,creator,parent_ticket"
    COLLECTIONS_ACCOUNT_PARENT_TICKET = "collections,account,parent_ticket"
    COLLECTIONS_CONTACT = "collections,contact"
    COLLECTIONS_CONTACT_CREATOR = "collections,contact,creator"
    COLLECTIONS_CONTACT_CREATOR_PARENT_TICKET = "collections,contact,creator,parent_ticket"
    COLLECTIONS_CONTACT_PARENT_TICKET = "collections,contact,parent_ticket"
    COLLECTIONS_CREATOR = "collections,creator"
    COLLECTIONS_CREATOR_PARENT_TICKET = "collections,creator,parent_ticket"
    COLLECTIONS_PARENT_TICKET = "collections,parent_ticket"
    CONTACT = "contact"
    CONTACT_CREATOR = "contact,creator"
    CONTACT_CREATOR_PARENT_TICKET = "contact,creator,parent_ticket"
    CONTACT_PARENT_TICKET = "contact,parent_ticket"
    CREATOR = "creator"
    CREATOR_PARENT_TICKET = "creator,parent_ticket"
    PARENT_TICKET = "parent_ticket"

    def visit(
        self,
        account: typing.Callable[[], T_Result],
        account_contact: typing.Callable[[], T_Result],
        account_contact_creator: typing.Callable[[], T_Result],
        account_contact_creator_parent_ticket: typing.Callable[[], T_Result],
        account_contact_parent_ticket: typing.Callable[[], T_Result],
        account_creator: typing.Callable[[], T_Result],
        account_creator_parent_ticket: typing.Callable[[], T_Result],
        account_parent_ticket: typing.Callable[[], T_Result],
        assignees: typing.Callable[[], T_Result],
        assignees_account: typing.Callable[[], T_Result],
        assignees_account_contact: typing.Callable[[], T_Result],
        assignees_account_contact_creator: typing.Callable[[], T_Result],
        assignees_account_contact_creator_parent_ticket: typing.Callable[[], T_Result],
        assignees_account_contact_parent_ticket: typing.Callable[[], T_Result],
        assignees_account_creator: typing.Callable[[], T_Result],
        assignees_account_creator_parent_ticket: typing.Callable[[], T_Result],
        assignees_account_parent_ticket: typing.Callable[[], T_Result],
        assignees_collections: typing.Callable[[], T_Result],
        assignees_collections_account: typing.Callable[[], T_Result],
        assignees_collections_account_contact: typing.Callable[[], T_Result],
        assignees_collections_account_contact_creator: typing.Callable[[], T_Result],
        assignees_collections_account_contact_creator_parent_ticket: typing.Callable[[], T_Result],
        assignees_collections_account_contact_parent_ticket: typing.Callable[[], T_Result],
        assignees_collections_account_creator: typing.Callable[[], T_Result],
        assignees_collections_account_creator_parent_ticket: typing.Callable[[], T_Result],
        assignees_collections_account_parent_ticket: typing.Callable[[], T_Result],
        assignees_collections_contact: typing.Callable[[], T_Result],
        assignees_collections_contact_creator: typing.Callable[[], T_Result],
        assignees_collections_contact_creator_parent_ticket: typing.Callable[[], T_Result],
        assignees_collections_contact_parent_ticket: typing.Callable[[], T_Result],
        assignees_collections_creator: typing.Callable[[], T_Result],
        assignees_collections_creator_parent_ticket: typing.Callable[[], T_Result],
        assignees_collections_parent_ticket: typing.Callable[[], T_Result],
        assignees_contact: typing.Callable[[], T_Result],
        assignees_contact_creator: typing.Callable[[], T_Result],
        assignees_contact_creator_parent_ticket: typing.Callable[[], T_Result],
        assignees_contact_parent_ticket: typing.Callable[[], T_Result],
        assignees_creator: typing.Callable[[], T_Result],
        assignees_creator_parent_ticket: typing.Callable[[], T_Result],
        assignees_parent_ticket: typing.Callable[[], T_Result],
        attachments: typing.Callable[[], T_Result],
        attachments_account: typing.Callable[[], T_Result],
        attachments_account_contact: typing.Callable[[], T_Result],
        attachments_account_contact_creator: typing.Callable[[], T_Result],
        attachments_account_contact_creator_parent_ticket: typing.Callable[[], T_Result],
        attachments_account_contact_parent_ticket: typing.Callable[[], T_Result],
        attachments_account_creator: typing.Callable[[], T_Result],
        attachments_account_creator_parent_ticket: typing.Callable[[], T_Result],
        attachments_account_parent_ticket: typing.Callable[[], T_Result],
        attachments_assignees: typing.Callable[[], T_Result],
        attachments_assignees_account: typing.Callable[[], T_Result],
        attachments_assignees_account_contact: typing.Callable[[], T_Result],
        attachments_assignees_account_contact_creator: typing.Callable[[], T_Result],
        attachments_assignees_account_contact_creator_parent_ticket: typing.Callable[[], T_Result],
        attachments_assignees_account_contact_parent_ticket: typing.Callable[[], T_Result],
        attachments_assignees_account_creator: typing.Callable[[], T_Result],
        attachments_assignees_account_creator_parent_ticket: typing.Callable[[], T_Result],
        attachments_assignees_account_parent_ticket: typing.Callable[[], T_Result],
        attachments_assignees_collections: typing.Callable[[], T_Result],
        attachments_assignees_collections_account: typing.Callable[[], T_Result],
        attachments_assignees_collections_account_contact: typing.Callable[[], T_Result],
        attachments_assignees_collections_account_contact_creator: typing.Callable[[], T_Result],
        attachments_assignees_collections_account_contact_creator_parent_ticket: typing.Callable[[], T_Result],
        attachments_assignees_collections_account_contact_parent_ticket: typing.Callable[[], T_Result],
        attachments_assignees_collections_account_creator: typing.Callable[[], T_Result],
        attachments_assignees_collections_account_creator_parent_ticket: typing.Callable[[], T_Result],
        attachments_assignees_collections_account_parent_ticket: typing.Callable[[], T_Result],
        attachments_assignees_collections_contact: typing.Callable[[], T_Result],
        attachments_assignees_collections_contact_creator: typing.Callable[[], T_Result],
        attachments_assignees_collections_contact_creator_parent_ticket: typing.Callable[[], T_Result],
        attachments_assignees_collections_contact_parent_ticket: typing.Callable[[], T_Result],
        attachments_assignees_collections_creator: typing.Callable[[], T_Result],
        attachments_assignees_collections_creator_parent_ticket: typing.Callable[[], T_Result],
        attachments_assignees_collections_parent_ticket: typing.Callable[[], T_Result],
        attachments_assignees_contact: typing.Callable[[], T_Result],
        attachments_assignees_contact_creator: typing.Callable[[], T_Result],
        attachments_assignees_contact_creator_parent_ticket: typing.Callable[[], T_Result],
        attachments_assignees_contact_parent_ticket: typing.Callable[[], T_Result],
        attachments_assignees_creator: typing.Callable[[], T_Result],
        attachments_assignees_creator_parent_ticket: typing.Callable[[], T_Result],
        attachments_assignees_parent_ticket: typing.Callable[[], T_Result],
        attachments_collections: typing.Callable[[], T_Result],
        attachments_collections_account: typing.Callable[[], T_Result],
        attachments_collections_account_contact: typing.Callable[[], T_Result],
        attachments_collections_account_contact_creator: typing.Callable[[], T_Result],
        attachments_collections_account_contact_creator_parent_ticket: typing.Callable[[], T_Result],
        attachments_collections_account_contact_parent_ticket: typing.Callable[[], T_Result],
        attachments_collections_account_creator: typing.Callable[[], T_Result],
        attachments_collections_account_creator_parent_ticket: typing.Callable[[], T_Result],
        attachments_collections_account_parent_ticket: typing.Callable[[], T_Result],
        attachments_collections_contact: typing.Callable[[], T_Result],
        attachments_collections_contact_creator: typing.Callable[[], T_Result],
        attachments_collections_contact_creator_parent_ticket: typing.Callable[[], T_Result],
        attachments_collections_contact_parent_ticket: typing.Callable[[], T_Result],
        attachments_collections_creator: typing.Callable[[], T_Result],
        attachments_collections_creator_parent_ticket: typing.Callable[[], T_Result],
        attachments_collections_parent_ticket: typing.Callable[[], T_Result],
        attachments_contact: typing.Callable[[], T_Result],
        attachments_contact_creator: typing.Callable[[], T_Result],
        attachments_contact_creator_parent_ticket: typing.Callable[[], T_Result],
        attachments_contact_parent_ticket: typing.Callable[[], T_Result],
        attachments_creator: typing.Callable[[], T_Result],
        attachments_creator_parent_ticket: typing.Callable[[], T_Result],
        attachments_parent_ticket: typing.Callable[[], T_Result],
        collections: typing.Callable[[], T_Result],
        collections_account: typing.Callable[[], T_Result],
        collections_account_contact: typing.Callable[[], T_Result],
        collections_account_contact_creator: typing.Callable[[], T_Result],
        collections_account_contact_creator_parent_ticket: typing.Callable[[], T_Result],
        collections_account_contact_parent_ticket: typing.Callable[[], T_Result],
        collections_account_creator: typing.Callable[[], T_Result],
        collections_account_creator_parent_ticket: typing.Callable[[], T_Result],
        collections_account_parent_ticket: typing.Callable[[], T_Result],
        collections_contact: typing.Callable[[], T_Result],
        collections_contact_creator: typing.Callable[[], T_Result],
        collections_contact_creator_parent_ticket: typing.Callable[[], T_Result],
        collections_contact_parent_ticket: typing.Callable[[], T_Result],
        collections_creator: typing.Callable[[], T_Result],
        collections_creator_parent_ticket: typing.Callable[[], T_Result],
        collections_parent_ticket: typing.Callable[[], T_Result],
        contact: typing.Callable[[], T_Result],
        contact_creator: typing.Callable[[], T_Result],
        contact_creator_parent_ticket: typing.Callable[[], T_Result],
        contact_parent_ticket: typing.Callable[[], T_Result],
        creator: typing.Callable[[], T_Result],
        creator_parent_ticket: typing.Callable[[], T_Result],
        parent_ticket: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is TicketsListRequestExpand.ACCOUNT:
            return account()
        if self is TicketsListRequestExpand.ACCOUNT_CONTACT:
            return account_contact()
        if self is TicketsListRequestExpand.ACCOUNT_CONTACT_CREATOR:
            return account_contact_creator()
        if self is TicketsListRequestExpand.ACCOUNT_CONTACT_CREATOR_PARENT_TICKET:
            return account_contact_creator_parent_ticket()
        if self is TicketsListRequestExpand.ACCOUNT_CONTACT_PARENT_TICKET:
            return account_contact_parent_ticket()
        if self is TicketsListRequestExpand.ACCOUNT_CREATOR:
            return account_creator()
        if self is TicketsListRequestExpand.ACCOUNT_CREATOR_PARENT_TICKET:
            return account_creator_parent_ticket()
        if self is TicketsListRequestExpand.ACCOUNT_PARENT_TICKET:
            return account_parent_ticket()
        if self is TicketsListRequestExpand.ASSIGNEES:
            return assignees()
        if self is TicketsListRequestExpand.ASSIGNEES_ACCOUNT:
            return assignees_account()
        if self is TicketsListRequestExpand.ASSIGNEES_ACCOUNT_CONTACT:
            return assignees_account_contact()
        if self is TicketsListRequestExpand.ASSIGNEES_ACCOUNT_CONTACT_CREATOR:
            return assignees_account_contact_creator()
        if self is TicketsListRequestExpand.ASSIGNEES_ACCOUNT_CONTACT_CREATOR_PARENT_TICKET:
            return assignees_account_contact_creator_parent_ticket()
        if self is TicketsListRequestExpand.ASSIGNEES_ACCOUNT_CONTACT_PARENT_TICKET:
            return assignees_account_contact_parent_ticket()
        if self is TicketsListRequestExpand.ASSIGNEES_ACCOUNT_CREATOR:
            return assignees_account_creator()
        if self is TicketsListRequestExpand.ASSIGNEES_ACCOUNT_CREATOR_PARENT_TICKET:
            return assignees_account_creator_parent_ticket()
        if self is TicketsListRequestExpand.ASSIGNEES_ACCOUNT_PARENT_TICKET:
            return assignees_account_parent_ticket()
        if self is TicketsListRequestExpand.ASSIGNEES_COLLECTIONS:
            return assignees_collections()
        if self is TicketsListRequestExpand.ASSIGNEES_COLLECTIONS_ACCOUNT:
            return assignees_collections_account()
        if self is TicketsListRequestExpand.ASSIGNEES_COLLECTIONS_ACCOUNT_CONTACT:
            return assignees_collections_account_contact()
        if self is TicketsListRequestExpand.ASSIGNEES_COLLECTIONS_ACCOUNT_CONTACT_CREATOR:
            return assignees_collections_account_contact_creator()
        if self is TicketsListRequestExpand.ASSIGNEES_COLLECTIONS_ACCOUNT_CONTACT_CREATOR_PARENT_TICKET:
            return assignees_collections_account_contact_creator_parent_ticket()
        if self is TicketsListRequestExpand.ASSIGNEES_COLLECTIONS_ACCOUNT_CONTACT_PARENT_TICKET:
            return assignees_collections_account_contact_parent_ticket()
        if self is TicketsListRequestExpand.ASSIGNEES_COLLECTIONS_ACCOUNT_CREATOR:
            return assignees_collections_account_creator()
        if self is TicketsListRequestExpand.ASSIGNEES_COLLECTIONS_ACCOUNT_CREATOR_PARENT_TICKET:
            return assignees_collections_account_creator_parent_ticket()
        if self is TicketsListRequestExpand.ASSIGNEES_COLLECTIONS_ACCOUNT_PARENT_TICKET:
            return assignees_collections_account_parent_ticket()
        if self is TicketsListRequestExpand.ASSIGNEES_COLLECTIONS_CONTACT:
            return assignees_collections_contact()
        if self is TicketsListRequestExpand.ASSIGNEES_COLLECTIONS_CONTACT_CREATOR:
            return assignees_collections_contact_creator()
        if self is TicketsListRequestExpand.ASSIGNEES_COLLECTIONS_CONTACT_CREATOR_PARENT_TICKET:
            return assignees_collections_contact_creator_parent_ticket()
        if self is TicketsListRequestExpand.ASSIGNEES_COLLECTIONS_CONTACT_PARENT_TICKET:
            return assignees_collections_contact_parent_ticket()
        if self is TicketsListRequestExpand.ASSIGNEES_COLLECTIONS_CREATOR:
            return assignees_collections_creator()
        if self is TicketsListRequestExpand.ASSIGNEES_COLLECTIONS_CREATOR_PARENT_TICKET:
            return assignees_collections_creator_parent_ticket()
        if self is TicketsListRequestExpand.ASSIGNEES_COLLECTIONS_PARENT_TICKET:
            return assignees_collections_parent_ticket()
        if self is TicketsListRequestExpand.ASSIGNEES_CONTACT:
            return assignees_contact()
        if self is TicketsListRequestExpand.ASSIGNEES_CONTACT_CREATOR:
            return assignees_contact_creator()
        if self is TicketsListRequestExpand.ASSIGNEES_CONTACT_CREATOR_PARENT_TICKET:
            return assignees_contact_creator_parent_ticket()
        if self is TicketsListRequestExpand.ASSIGNEES_CONTACT_PARENT_TICKET:
            return assignees_contact_parent_ticket()
        if self is TicketsListRequestExpand.ASSIGNEES_CREATOR:
            return assignees_creator()
        if self is TicketsListRequestExpand.ASSIGNEES_CREATOR_PARENT_TICKET:
            return assignees_creator_parent_ticket()
        if self is TicketsListRequestExpand.ASSIGNEES_PARENT_TICKET:
            return assignees_parent_ticket()
        if self is TicketsListRequestExpand.ATTACHMENTS:
            return attachments()
        if self is TicketsListRequestExpand.ATTACHMENTS_ACCOUNT:
            return attachments_account()
        if self is TicketsListRequestExpand.ATTACHMENTS_ACCOUNT_CONTACT:
            return attachments_account_contact()
        if self is TicketsListRequestExpand.ATTACHMENTS_ACCOUNT_CONTACT_CREATOR:
            return attachments_account_contact_creator()
        if self is TicketsListRequestExpand.ATTACHMENTS_ACCOUNT_CONTACT_CREATOR_PARENT_TICKET:
            return attachments_account_contact_creator_parent_ticket()
        if self is TicketsListRequestExpand.ATTACHMENTS_ACCOUNT_CONTACT_PARENT_TICKET:
            return attachments_account_contact_parent_ticket()
        if self is TicketsListRequestExpand.ATTACHMENTS_ACCOUNT_CREATOR:
            return attachments_account_creator()
        if self is TicketsListRequestExpand.ATTACHMENTS_ACCOUNT_CREATOR_PARENT_TICKET:
            return attachments_account_creator_parent_ticket()
        if self is TicketsListRequestExpand.ATTACHMENTS_ACCOUNT_PARENT_TICKET:
            return attachments_account_parent_ticket()
        if self is TicketsListRequestExpand.ATTACHMENTS_ASSIGNEES:
            return attachments_assignees()
        if self is TicketsListRequestExpand.ATTACHMENTS_ASSIGNEES_ACCOUNT:
            return attachments_assignees_account()
        if self is TicketsListRequestExpand.ATTACHMENTS_ASSIGNEES_ACCOUNT_CONTACT:
            return attachments_assignees_account_contact()
        if self is TicketsListRequestExpand.ATTACHMENTS_ASSIGNEES_ACCOUNT_CONTACT_CREATOR:
            return attachments_assignees_account_contact_creator()
        if self is TicketsListRequestExpand.ATTACHMENTS_ASSIGNEES_ACCOUNT_CONTACT_CREATOR_PARENT_TICKET:
            return attachments_assignees_account_contact_creator_parent_ticket()
        if self is TicketsListRequestExpand.ATTACHMENTS_ASSIGNEES_ACCOUNT_CONTACT_PARENT_TICKET:
            return attachments_assignees_account_contact_parent_ticket()
        if self is TicketsListRequestExpand.ATTACHMENTS_ASSIGNEES_ACCOUNT_CREATOR:
            return attachments_assignees_account_creator()
        if self is TicketsListRequestExpand.ATTACHMENTS_ASSIGNEES_ACCOUNT_CREATOR_PARENT_TICKET:
            return attachments_assignees_account_creator_parent_ticket()
        if self is TicketsListRequestExpand.ATTACHMENTS_ASSIGNEES_ACCOUNT_PARENT_TICKET:
            return attachments_assignees_account_parent_ticket()
        if self is TicketsListRequestExpand.ATTACHMENTS_ASSIGNEES_COLLECTIONS:
            return attachments_assignees_collections()
        if self is TicketsListRequestExpand.ATTACHMENTS_ASSIGNEES_COLLECTIONS_ACCOUNT:
            return attachments_assignees_collections_account()
        if self is TicketsListRequestExpand.ATTACHMENTS_ASSIGNEES_COLLECTIONS_ACCOUNT_CONTACT:
            return attachments_assignees_collections_account_contact()
        if self is TicketsListRequestExpand.ATTACHMENTS_ASSIGNEES_COLLECTIONS_ACCOUNT_CONTACT_CREATOR:
            return attachments_assignees_collections_account_contact_creator()
        if self is TicketsListRequestExpand.ATTACHMENTS_ASSIGNEES_COLLECTIONS_ACCOUNT_CONTACT_CREATOR_PARENT_TICKET:
            return attachments_assignees_collections_account_contact_creator_parent_ticket()
        if self is TicketsListRequestExpand.ATTACHMENTS_ASSIGNEES_COLLECTIONS_ACCOUNT_CONTACT_PARENT_TICKET:
            return attachments_assignees_collections_account_contact_parent_ticket()
        if self is TicketsListRequestExpand.ATTACHMENTS_ASSIGNEES_COLLECTIONS_ACCOUNT_CREATOR:
            return attachments_assignees_collections_account_creator()
        if self is TicketsListRequestExpand.ATTACHMENTS_ASSIGNEES_COLLECTIONS_ACCOUNT_CREATOR_PARENT_TICKET:
            return attachments_assignees_collections_account_creator_parent_ticket()
        if self is TicketsListRequestExpand.ATTACHMENTS_ASSIGNEES_COLLECTIONS_ACCOUNT_PARENT_TICKET:
            return attachments_assignees_collections_account_parent_ticket()
        if self is TicketsListRequestExpand.ATTACHMENTS_ASSIGNEES_COLLECTIONS_CONTACT:
            return attachments_assignees_collections_contact()
        if self is TicketsListRequestExpand.ATTACHMENTS_ASSIGNEES_COLLECTIONS_CONTACT_CREATOR:
            return attachments_assignees_collections_contact_creator()
        if self is TicketsListRequestExpand.ATTACHMENTS_ASSIGNEES_COLLECTIONS_CONTACT_CREATOR_PARENT_TICKET:
            return attachments_assignees_collections_contact_creator_parent_ticket()
        if self is TicketsListRequestExpand.ATTACHMENTS_ASSIGNEES_COLLECTIONS_CONTACT_PARENT_TICKET:
            return attachments_assignees_collections_contact_parent_ticket()
        if self is TicketsListRequestExpand.ATTACHMENTS_ASSIGNEES_COLLECTIONS_CREATOR:
            return attachments_assignees_collections_creator()
        if self is TicketsListRequestExpand.ATTACHMENTS_ASSIGNEES_COLLECTIONS_CREATOR_PARENT_TICKET:
            return attachments_assignees_collections_creator_parent_ticket()
        if self is TicketsListRequestExpand.ATTACHMENTS_ASSIGNEES_COLLECTIONS_PARENT_TICKET:
            return attachments_assignees_collections_parent_ticket()
        if self is TicketsListRequestExpand.ATTACHMENTS_ASSIGNEES_CONTACT:
            return attachments_assignees_contact()
        if self is TicketsListRequestExpand.ATTACHMENTS_ASSIGNEES_CONTACT_CREATOR:
            return attachments_assignees_contact_creator()
        if self is TicketsListRequestExpand.ATTACHMENTS_ASSIGNEES_CONTACT_CREATOR_PARENT_TICKET:
            return attachments_assignees_contact_creator_parent_ticket()
        if self is TicketsListRequestExpand.ATTACHMENTS_ASSIGNEES_CONTACT_PARENT_TICKET:
            return attachments_assignees_contact_parent_ticket()
        if self is TicketsListRequestExpand.ATTACHMENTS_ASSIGNEES_CREATOR:
            return attachments_assignees_creator()
        if self is TicketsListRequestExpand.ATTACHMENTS_ASSIGNEES_CREATOR_PARENT_TICKET:
            return attachments_assignees_creator_parent_ticket()
        if self is TicketsListRequestExpand.ATTACHMENTS_ASSIGNEES_PARENT_TICKET:
            return attachments_assignees_parent_ticket()
        if self is TicketsListRequestExpand.ATTACHMENTS_COLLECTIONS:
            return attachments_collections()
        if self is TicketsListRequestExpand.ATTACHMENTS_COLLECTIONS_ACCOUNT:
            return attachments_collections_account()
        if self is TicketsListRequestExpand.ATTACHMENTS_COLLECTIONS_ACCOUNT_CONTACT:
            return attachments_collections_account_contact()
        if self is TicketsListRequestExpand.ATTACHMENTS_COLLECTIONS_ACCOUNT_CONTACT_CREATOR:
            return attachments_collections_account_contact_creator()
        if self is TicketsListRequestExpand.ATTACHMENTS_COLLECTIONS_ACCOUNT_CONTACT_CREATOR_PARENT_TICKET:
            return attachments_collections_account_contact_creator_parent_ticket()
        if self is TicketsListRequestExpand.ATTACHMENTS_COLLECTIONS_ACCOUNT_CONTACT_PARENT_TICKET:
            return attachments_collections_account_contact_parent_ticket()
        if self is TicketsListRequestExpand.ATTACHMENTS_COLLECTIONS_ACCOUNT_CREATOR:
            return attachments_collections_account_creator()
        if self is TicketsListRequestExpand.ATTACHMENTS_COLLECTIONS_ACCOUNT_CREATOR_PARENT_TICKET:
            return attachments_collections_account_creator_parent_ticket()
        if self is TicketsListRequestExpand.ATTACHMENTS_COLLECTIONS_ACCOUNT_PARENT_TICKET:
            return attachments_collections_account_parent_ticket()
        if self is TicketsListRequestExpand.ATTACHMENTS_COLLECTIONS_CONTACT:
            return attachments_collections_contact()
        if self is TicketsListRequestExpand.ATTACHMENTS_COLLECTIONS_CONTACT_CREATOR:
            return attachments_collections_contact_creator()
        if self is TicketsListRequestExpand.ATTACHMENTS_COLLECTIONS_CONTACT_CREATOR_PARENT_TICKET:
            return attachments_collections_contact_creator_parent_ticket()
        if self is TicketsListRequestExpand.ATTACHMENTS_COLLECTIONS_CONTACT_PARENT_TICKET:
            return attachments_collections_contact_parent_ticket()
        if self is TicketsListRequestExpand.ATTACHMENTS_COLLECTIONS_CREATOR:
            return attachments_collections_creator()
        if self is TicketsListRequestExpand.ATTACHMENTS_COLLECTIONS_CREATOR_PARENT_TICKET:
            return attachments_collections_creator_parent_ticket()
        if self is TicketsListRequestExpand.ATTACHMENTS_COLLECTIONS_PARENT_TICKET:
            return attachments_collections_parent_ticket()
        if self is TicketsListRequestExpand.ATTACHMENTS_CONTACT:
            return attachments_contact()
        if self is TicketsListRequestExpand.ATTACHMENTS_CONTACT_CREATOR:
            return attachments_contact_creator()
        if self is TicketsListRequestExpand.ATTACHMENTS_CONTACT_CREATOR_PARENT_TICKET:
            return attachments_contact_creator_parent_ticket()
        if self is TicketsListRequestExpand.ATTACHMENTS_CONTACT_PARENT_TICKET:
            return attachments_contact_parent_ticket()
        if self is TicketsListRequestExpand.ATTACHMENTS_CREATOR:
            return attachments_creator()
        if self is TicketsListRequestExpand.ATTACHMENTS_CREATOR_PARENT_TICKET:
            return attachments_creator_parent_ticket()
        if self is TicketsListRequestExpand.ATTACHMENTS_PARENT_TICKET:
            return attachments_parent_ticket()
        if self is TicketsListRequestExpand.COLLECTIONS:
            return collections()
        if self is TicketsListRequestExpand.COLLECTIONS_ACCOUNT:
            return collections_account()
        if self is TicketsListRequestExpand.COLLECTIONS_ACCOUNT_CONTACT:
            return collections_account_contact()
        if self is TicketsListRequestExpand.COLLECTIONS_ACCOUNT_CONTACT_CREATOR:
            return collections_account_contact_creator()
        if self is TicketsListRequestExpand.COLLECTIONS_ACCOUNT_CONTACT_CREATOR_PARENT_TICKET:
            return collections_account_contact_creator_parent_ticket()
        if self is TicketsListRequestExpand.COLLECTIONS_ACCOUNT_CONTACT_PARENT_TICKET:
            return collections_account_contact_parent_ticket()
        if self is TicketsListRequestExpand.COLLECTIONS_ACCOUNT_CREATOR:
            return collections_account_creator()
        if self is TicketsListRequestExpand.COLLECTIONS_ACCOUNT_CREATOR_PARENT_TICKET:
            return collections_account_creator_parent_ticket()
        if self is TicketsListRequestExpand.COLLECTIONS_ACCOUNT_PARENT_TICKET:
            return collections_account_parent_ticket()
        if self is TicketsListRequestExpand.COLLECTIONS_CONTACT:
            return collections_contact()
        if self is TicketsListRequestExpand.COLLECTIONS_CONTACT_CREATOR:
            return collections_contact_creator()
        if self is TicketsListRequestExpand.COLLECTIONS_CONTACT_CREATOR_PARENT_TICKET:
            return collections_contact_creator_parent_ticket()
        if self is TicketsListRequestExpand.COLLECTIONS_CONTACT_PARENT_TICKET:
            return collections_contact_parent_ticket()
        if self is TicketsListRequestExpand.COLLECTIONS_CREATOR:
            return collections_creator()
        if self is TicketsListRequestExpand.COLLECTIONS_CREATOR_PARENT_TICKET:
            return collections_creator_parent_ticket()
        if self is TicketsListRequestExpand.COLLECTIONS_PARENT_TICKET:
            return collections_parent_ticket()
        if self is TicketsListRequestExpand.CONTACT:
            return contact()
        if self is TicketsListRequestExpand.CONTACT_CREATOR:
            return contact_creator()
        if self is TicketsListRequestExpand.CONTACT_CREATOR_PARENT_TICKET:
            return contact_creator_parent_ticket()
        if self is TicketsListRequestExpand.CONTACT_PARENT_TICKET:
            return contact_parent_ticket()
        if self is TicketsListRequestExpand.CREATOR:
            return creator()
        if self is TicketsListRequestExpand.CREATOR_PARENT_TICKET:
            return creator_parent_ticket()
        if self is TicketsListRequestExpand.PARENT_TICKET:
            return parent_ticket()