# coding: utf-8

"""
    Data API

    Serves the Clever Data API

    The version of the OpenAPI document: 3.1.0
    Generated by: https://konfigthis.com
"""

from datetime import datetime, date
import typing
from enum import Enum
from typing_extensions import TypedDict, Literal, TYPE_CHECKING

from clever_python_sdk.type.link import Link
from clever_python_sdk.type.user_response import UserResponse

class RequiredUsersResponse(TypedDict):
    pass

class OptionalUsersResponse(TypedDict, total=False):
    data: typing.List[UserResponse]

    links: typing.List[Link]

class UsersResponse(RequiredUsersResponse, OptionalUsersResponse):
    pass
