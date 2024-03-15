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


class RequiredTerm(TypedDict):
    pass

class OptionalTerm(TypedDict, total=False):
    district: str

    end_date: typing.Optional[str]

    id: str

    name: typing.Optional[str]

    start_date: typing.Optional[str]

class Term(RequiredTerm, OptionalTerm):
    pass