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

from clever_python_sdk.pydantic.location import Location
from clever_python_sdk.pydantic.principal import Principal

class School(BaseModel):
    created: typing.Optional[str] = Field(None, alias='created')

    district: typing.Optional[str] = Field(None, alias='district')

    ext: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = Field(None, alias='ext')

    high_grade: typing.Optional[Literal["InfantToddler", "Preschool", "PreKindergarten", "TransitionalKindergarten", "Kindergarten", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "PostGraduate", "Ungraded", "Other", ""]] = Field(None, alias='high_grade')

    id: typing.Optional[str] = Field(None, alias='id')

    last_modified: typing.Optional[str] = Field(None, alias='last_modified')

    location: typing.Optional[Location] = Field(None, alias='location')

    low_grade: typing.Optional[Literal["InfantToddler", "Preschool", "PreKindergarten", "TransitionalKindergarten", "Kindergarten", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "PostGraduate", "Ungraded", "Other", ""]] = Field(None, alias='low_grade')

    mdr_number: typing.Optional[typing.Optional[str]] = Field(None, alias='mdr_number')

    name: typing.Optional[str] = Field(None, alias='name')

    nces_id: typing.Optional[typing.Optional[str]] = Field(None, alias='nces_id')

    phone: typing.Optional[typing.Optional[str]] = Field(None, alias='phone')

    principal: typing.Optional[Principal] = Field(None, alias='principal')

    school_number: typing.Optional[str] = Field(None, alias='school_number')

    sis_id: typing.Optional[str] = Field(None, alias='sis_id')

    state_id: typing.Optional[typing.Optional[str]] = Field(None, alias='state_id')
    class Config:
        arbitrary_types_allowed = True
