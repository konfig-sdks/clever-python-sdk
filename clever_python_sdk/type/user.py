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

from clever_python_sdk.type.name import Name
from clever_python_sdk.type.roles import Roles

class RequiredUser(TypedDict):
    pass

class OptionalUser(TypedDict, total=False):
    created: str

    district: str

    email: typing.Optional[str]

    id: str

    last_modified: str

    name: Name

    roles: Roles

class User(RequiredUser, OptionalUser):
    pass