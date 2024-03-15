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


class Course(BaseModel):
    district: typing.Optional[str] = Field(None, alias='district')

    id: typing.Optional[str] = Field(None, alias='id')

    name: typing.Optional[typing.Optional[str]] = Field(None, alias='name')

    number: typing.Optional[typing.Optional[str]] = Field(None, alias='number')
    class Config:
        arbitrary_types_allowed = True