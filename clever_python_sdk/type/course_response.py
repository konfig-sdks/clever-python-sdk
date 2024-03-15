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

from clever_python_sdk.type.course import Course

class RequiredCourseResponse(TypedDict):
    pass

class OptionalCourseResponse(TypedDict, total=False):
    data: Course

class CourseResponse(RequiredCourseResponse, OptionalCourseResponse):
    pass
