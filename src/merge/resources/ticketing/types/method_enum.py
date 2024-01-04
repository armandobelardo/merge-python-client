# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class MethodEnum(str, enum.Enum):
    """
    * `GET` - GET
    * `OPTIONS` - OPTIONS
    * `HEAD` - HEAD
    * `POST` - POST
    * `PUT` - PUT
    * `PATCH` - PATCH
    * `DELETE` - DELETE
    """

    GET = "GET"
    OPTIONS = "OPTIONS"
    HEAD = "HEAD"
    POST = "POST"
    PUT = "PUT"
    PATCH = "PATCH"
    DELETE = "DELETE"

    def visit(
        self,
        get: typing.Callable[[], T_Result],
        options: typing.Callable[[], T_Result],
        head: typing.Callable[[], T_Result],
        post: typing.Callable[[], T_Result],
        put: typing.Callable[[], T_Result],
        patch: typing.Callable[[], T_Result],
        delete: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is MethodEnum.GET:
            return get()
        if self is MethodEnum.OPTIONS:
            return options()
        if self is MethodEnum.HEAD:
            return head()
        if self is MethodEnum.POST:
            return post()
        if self is MethodEnum.PUT:
            return put()
        if self is MethodEnum.PATCH:
            return patch()
        if self is MethodEnum.DELETE:
            return delete()
