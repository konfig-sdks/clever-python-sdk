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


class RequiredStudentRelationship(TypedDict):
    pass

class OptionalStudentRelationship(TypedDict, total=False):
    relationship: typing.Optional[str]

    student: str

    type: typing.Optional[str]

class StudentRelationship(RequiredStudentRelationship, OptionalStudentRelationship):
    pass