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

from clever_python_sdk.type.student_relationship import StudentRelationship

class RequiredContact(TypedDict):
    pass

class OptionalContact(TypedDict, total=False):
    legacy_id: str

    phone: typing.Optional[str]

    phone_type: typing.Optional[str]

    sis_id: typing.Optional[str]

    student_relationships: typing.List[StudentRelationship]

class Contact(RequiredContact, OptionalContact):
    pass
