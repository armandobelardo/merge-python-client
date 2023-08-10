# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

import pydantic

from ....core.datetime_utils import serialize_datetime
from .employee_request_company import EmployeeRequestCompany
from .employee_request_employment_status import EmployeeRequestEmploymentStatus
from .employee_request_employments_item import EmployeeRequestEmploymentsItem
from .employee_request_ethnicity import EmployeeRequestEthnicity
from .employee_request_gender import EmployeeRequestGender
from .employee_request_groups_item import EmployeeRequestGroupsItem
from .employee_request_home_location import EmployeeRequestHomeLocation
from .employee_request_manager import EmployeeRequestManager
from .employee_request_marital_status import EmployeeRequestMaritalStatus
from .employee_request_pay_group import EmployeeRequestPayGroup
from .employee_request_team import EmployeeRequestTeam
from .employee_request_work_location import EmployeeRequestWorkLocation


class EmployeeRequest(pydantic.BaseModel):
    """
    # The Employee Object
    ### Description
    The `Employee` object is used to represent any person who has been employed by a company.

    ### Usage Example
    Fetch from the `LIST Employee` endpoint and filter by `ID` to show all employees.
    """

    employee_number: typing.Optional[str] = pydantic.Field(
        description="The employee's number that appears in the third-party integration's UI."
    )
    company: typing.Optional[EmployeeRequestCompany] = pydantic.Field(description="The ID of the employee's company.")
    first_name: typing.Optional[str] = pydantic.Field(description="The employee's first name.")
    last_name: typing.Optional[str] = pydantic.Field(description="The employee's last name.")
    display_full_name: typing.Optional[str] = pydantic.Field(
        description="The employee's full name, to use for display purposes. If a preferred first name is available, the full name will include the preferred first name."
    )
    username: typing.Optional[str] = pydantic.Field(
        description="The employee's username that appears in the remote UI."
    )
    groups: typing.Optional[typing.List[typing.Optional[EmployeeRequestGroupsItem]]]
    work_email: typing.Optional[str] = pydantic.Field(description="The employee's work email.")
    personal_email: typing.Optional[str] = pydantic.Field(description="The employee's personal email.")
    mobile_phone_number: typing.Optional[str] = pydantic.Field(description="The employee's mobile phone number.")
    employments: typing.Optional[typing.List[typing.Optional[EmployeeRequestEmploymentsItem]]] = pydantic.Field(
        description="Array of `Employment` IDs for this Employee."
    )
    home_location: typing.Optional[EmployeeRequestHomeLocation] = pydantic.Field(
        description="The employee's home address."
    )
    work_location: typing.Optional[EmployeeRequestWorkLocation] = pydantic.Field(
        description="The employee's work address."
    )
    manager: typing.Optional[EmployeeRequestManager] = pydantic.Field(
        description="The employee ID of the employee's manager."
    )
    team: typing.Optional[EmployeeRequestTeam] = pydantic.Field(description="The employee's team.")
    pay_group: typing.Optional[EmployeeRequestPayGroup] = pydantic.Field(description="The employee's pay group")
    ssn: typing.Optional[str] = pydantic.Field(description="The employee's social security number.")
    gender: typing.Optional[EmployeeRequestGender] = pydantic.Field(
        description=(
            "The employee's gender.\n"
            "\n"
            "* `MALE` - MALE\n"
            "* `FEMALE` - FEMALE\n"
            "* `NON-BINARY` - NON-BINARY\n"
            "* `OTHER` - OTHER\n"
            "* `PREFER_NOT_TO_DISCLOSE` - PREFER_NOT_TO_DISCLOSE\n"
        )
    )
    ethnicity: typing.Optional[EmployeeRequestEthnicity] = pydantic.Field(
        description=(
            "The employee's ethnicity.\n"
            "\n"
            "* `AMERICAN_INDIAN_OR_ALASKA_NATIVE` - AMERICAN_INDIAN_OR_ALASKA_NATIVE\n"
            "* `ASIAN_OR_INDIAN_SUBCONTINENT` - ASIAN_OR_INDIAN_SUBCONTINENT\n"
            "* `BLACK_OR_AFRICAN_AMERICAN` - BLACK_OR_AFRICAN_AMERICAN\n"
            "* `HISPANIC_OR_LATINO` - HISPANIC_OR_LATINO\n"
            "* `NATIVE_HAWAIIAN_OR_OTHER_PACIFIC_ISLANDER` - NATIVE_HAWAIIAN_OR_OTHER_PACIFIC_ISLANDER\n"
            "* `TWO_OR_MORE_RACES` - TWO_OR_MORE_RACES\n"
            "* `WHITE` - WHITE\n"
            "* `PREFER_NOT_TO_DISCLOSE` - PREFER_NOT_TO_DISCLOSE\n"
        )
    )
    marital_status: typing.Optional[EmployeeRequestMaritalStatus] = pydantic.Field(
        description=(
            "The employee's filing status as related to marital status.\n"
            "\n"
            "* `SINGLE` - SINGLE\n"
            "* `MARRIED_FILING_JOINTLY` - MARRIED_FILING_JOINTLY\n"
            "* `MARRIED_FILING_SEPARATELY` - MARRIED_FILING_SEPARATELY\n"
            "* `HEAD_OF_HOUSEHOLD` - HEAD_OF_HOUSEHOLD\n"
            "* `QUALIFYING_WIDOW_OR_WIDOWER_WITH_DEPENDENT_CHILD` - QUALIFYING_WIDOW_OR_WIDOWER_WITH_DEPENDENT_CHILD\n"
        )
    )
    date_of_birth: typing.Optional[dt.datetime] = pydantic.Field(description="The employee's date of birth.")
    hire_date: typing.Optional[dt.datetime] = pydantic.Field(
        description="The date that the employee was hired, usually the day that an offer letter is signed. If an employee has multiple hire dates from previous employments, this represents the most recent hire date. Note: If you're looking for the employee's start date, refer to the start_date field."
    )
    start_date: typing.Optional[dt.datetime] = pydantic.Field(
        description="The date that the employee started working. If an employee was rehired, the most recent start date will be returned."
    )
    employment_status: typing.Optional[EmployeeRequestEmploymentStatus] = pydantic.Field(
        description=(
            "The employment status of the employee.\n"
            "\n"
            "* `ACTIVE` - ACTIVE\n"
            "* `PENDING` - PENDING\n"
            "* `INACTIVE` - INACTIVE\n"
        )
    )
    termination_date: typing.Optional[dt.datetime] = pydantic.Field(description="The employee's termination date.")
    avatar: typing.Optional[str] = pydantic.Field(description="The URL of the employee's avatar image.")
    integration_params: typing.Optional[typing.Dict[str, typing.Any]]
    linked_account_params: typing.Optional[typing.Dict[str, typing.Any]]

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Config:
        frozen = True
        json_encoders = {dt.datetime: serialize_datetime}
