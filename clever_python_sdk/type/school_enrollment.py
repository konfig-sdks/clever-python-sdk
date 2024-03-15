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


class RequiredSchoolEnrollment(TypedDict):
    pass

class OptionalSchoolEnrollment(TypedDict, total=False):
    end_date: str

    school: str

    start_date: str

class SchoolEnrollment(RequiredSchoolEnrollment, OptionalSchoolEnrollment):
    pass
