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


class RequiredDistrictAdmin(TypedDict):
    pass

class OptionalDistrictAdmin(TypedDict, total=False):
    title: typing.Optional[str]

    legacy_id: str

class DistrictAdmin(RequiredDistrictAdmin, OptionalDistrictAdmin):
    pass
