# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import typing

from .company import Company
from .country_enum import CountryEnum
from .employee_company import EmployeeCompany
from .employee_employment_status import EmployeeEmploymentStatus
from .employee_ethnicity import EmployeeEthnicity
from .employee_gender import EmployeeGender
from .employee_groups_item import EmployeeGroupsItem
from .employee_home_location import EmployeeHomeLocation
from .employee_marital_status import EmployeeMaritalStatus
from .employee_pay_group import EmployeePayGroup
from .employee_team import EmployeeTeam
from .employee_work_location import EmployeeWorkLocation
from .employment_employment_type import EmploymentEmploymentType
from .employment_flsa_status import EmploymentFlsaStatus
from .employment_pay_currency import EmploymentPayCurrency
from .employment_pay_frequency import EmploymentPayFrequency
from .employment_pay_group import EmploymentPayGroup
from .employment_pay_period import EmploymentPayPeriod
from .employment_status_enum import EmploymentStatusEnum
from .employment_type_enum import EmploymentTypeEnum
from .ethnicity_enum import EthnicityEnum
from .flsa_status_enum import FlsaStatusEnum
from .gender_enum import GenderEnum
from .group import Group
from .group_type import GroupType
from .group_type_enum import GroupTypeEnum
from .location import Location
from .location_country import LocationCountry
from .location_location_type import LocationLocationType
from .location_type_enum import LocationTypeEnum
from .marital_status_enum import MaritalStatusEnum
from .pay_currency_enum import PayCurrencyEnum
from .pay_frequency_enum import PayFrequencyEnum
from .pay_group import PayGroup
from .pay_period_enum import PayPeriodEnum
from .remote_data import RemoteData

EmployeeRequestManager = typing.Union[str, "Employee"]
from .employee import Employee  # noqa: E402
from .employee_employments_item import EmployeeEmploymentsItem  # noqa: E402
from .employee_manager import EmployeeManager  # noqa: E402
from .employment import Employment  # noqa: E402
from .employment_employee import EmploymentEmployee  # noqa: E402
from .team import Team  # noqa: E402
from .team_parent_team import TeamParentTeam  # noqa: E402
