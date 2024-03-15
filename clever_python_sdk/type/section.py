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

from clever_python_sdk.type.section_students import SectionStudents
from clever_python_sdk.type.section_teachers import SectionTeachers

class RequiredSection(TypedDict):
    pass

class OptionalSection(TypedDict, total=False):
    course: typing.Optional[str]

    created: str

    district: str

    ext: typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]

    grade: typing.Optional[str]

    id: str

    last_modified: str

    name: str

    period: typing.Optional[str]

    school: str

    section_number: typing.Optional[str]

    sis_id: str

    students: SectionStudents

    subject: typing.Optional[str]

    teacher: typing.Optional[str]

    teachers: SectionTeachers

    term_id: typing.Optional[str]

class Section(RequiredSection, OptionalSection):
    pass
