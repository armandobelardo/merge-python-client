# This file was auto-generated by Fern from our API Definition.

import typing

from .access_role_enum import AccessRoleEnum
from .department import Department
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
from .remote_data import RemoteData
from .remote_user import RemoteUser
from .remote_user_access_role import RemoteUserAccessRole
from .url import Url
from .url_type_enum import UrlTypeEnum
from .url_url_type import UrlUrlType

ScheduledInterviewJobInterviewStage = typing.Union[str, JobInterviewStage]
