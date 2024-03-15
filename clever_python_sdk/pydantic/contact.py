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

from clever_python_sdk.pydantic.student_relationship import StudentRelationship

class Contact(BaseModel):
    legacy_id: typing.Optional[str] = Field(None, alias='legacy_id')

    phone: typing.Optional[typing.Optional[str]] = Field(None, alias='phone')

    phone_type: typing.Optional[Literal["Cell", "Home", "Work", "Other", ""]] = Field(None, alias='phone_type')

    sis_id: typing.Optional[typing.Optional[str]] = Field(None, alias='sis_id')

    student_relationships: typing.Optional[typing.List[StudentRelationship]] = Field(None, alias='student_relationships')
    class Config:
        arbitrary_types_allowed = True