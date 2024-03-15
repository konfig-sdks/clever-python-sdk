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


class RequiredPrincipal(TypedDict):
    pass

class OptionalPrincipal(TypedDict, total=False):
    email: typing.Optional[str]

    name: typing.Optional[str]

class Principal(RequiredPrincipal, OptionalPrincipal):
    pass