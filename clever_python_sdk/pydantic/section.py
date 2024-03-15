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
from pydantic import BaseModel, Field, RootModel

from clever_python_sdk.pydantic.section_students import SectionStudents
from clever_python_sdk.pydantic.section_teachers import SectionTeachers

class Section(BaseModel):
    course: typing.Optional[typing.Optional[str]] = Field(None, alias='course')

    created: typing.Optional[str] = Field(None, alias='created')

    district: typing.Optional[str] = Field(None, alias='district')

    ext: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = Field(None, alias='ext')

    grade: typing.Optional[Literal["InfantToddler", "Preschool", "PreKindergarten", "TransitionalKindergarten", "Kindergarten", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "PostGraduate", "Ungraded", "Other", ""]] = Field(None, alias='grade')

    id: typing.Optional[str] = Field(None, alias='id')

    last_modified: typing.Optional[str] = Field(None, alias='last_modified')

    name: typing.Optional[str] = Field(None, alias='name')

    period: typing.Optional[typing.Optional[str]] = Field(None, alias='period')

    school: typing.Optional[str] = Field(None, alias='school')

    section_number: typing.Optional[typing.Optional[str]] = Field(None, alias='section_number')

    sis_id: typing.Optional[str] = Field(None, alias='sis_id')

    students: typing.Optional[SectionStudents] = Field(None, alias='students')

    subject: typing.Optional[Literal["english/language arts", "math", "science", "social studies", "language", "homeroom/advisory", "interventions/online learning", "technology and engineering", "PE and health", "arts and music", "other", ""]] = Field(None, alias='subject')

    teacher: typing.Optional[typing.Optional[str]] = Field(None, alias='teacher')

    teachers: typing.Optional[SectionTeachers] = Field(None, alias='teachers')

    term_id: typing.Optional[typing.Optional[str]] = Field(None, alias='term_id')
    class Config:
        arbitrary_types_allowed = True