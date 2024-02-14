# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import typing

from .access_role_enum import AccessRoleEnum
from .application_credited_to import ApplicationCreditedTo
from .application_current_stage import ApplicationCurrentStage
from .application_job import ApplicationJob
from .application_reject_reason import ApplicationRejectReason
from .attachment import Attachment
from .attachment_attachment_type import AttachmentAttachmentType
from .attachment_type_enum import AttachmentTypeEnum
from .candidate_attachments_item import CandidateAttachmentsItem
from .department import Department
from .email_address import EmailAddress
from .email_address_email_address_type import EmailAddressEmailAddressType
from .email_address_type_enum import EmailAddressTypeEnum
from .job import Job
from .job_departments_item import JobDepartmentsItem
from .job_hiring_managers_item import JobHiringManagersItem
from .job_interview_stage import JobInterviewStage
from .job_interview_stage_job import JobInterviewStageJob
from .job_offices_item import JobOfficesItem
from .job_recruiters_item import JobRecruitersItem
from .job_status import JobStatus
from .job_status_enum import JobStatusEnum
from .office import Office
from .phone_number import PhoneNumber
from .phone_number_phone_number_type import PhoneNumberPhoneNumberType
from .phone_number_type_enum import PhoneNumberTypeEnum
from .reject_reason import RejectReason
from .remote_data import RemoteData
from .remote_user import RemoteUser
from .remote_user_access_role import RemoteUserAccessRole
from .scheduled_interview import ScheduledInterview
from .scheduled_interview_application import ScheduledInterviewApplication
from .scheduled_interview_interviewers_item import ScheduledInterviewInterviewersItem
from .scheduled_interview_job_interview_stage import ScheduledInterviewJobInterviewStage
from .scheduled_interview_organizer import ScheduledInterviewOrganizer
from .scheduled_interview_status import ScheduledInterviewStatus
from .scheduled_interview_status_enum import ScheduledInterviewStatusEnum
from .url import Url
from .url_type_enum import UrlTypeEnum
from .url_url_type import UrlUrlType

ScorecardInterview = typing.Union[str, ScheduledInterview]
from .application import Application  # noqa: E402
from .application_candidate import ApplicationCandidate  # noqa: E402
from .candidate import Candidate  # noqa: E402
from .candidate_applications_item import CandidateApplicationsItem  # noqa: E402
