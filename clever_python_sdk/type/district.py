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

from clever_python_sdk.type.district_contact import DistrictContact
from clever_python_sdk.type.district_login_methods import DistrictLoginMethods

class RequiredDistrict(TypedDict):
    pass

class OptionalDistrict(TypedDict, total=False):
    district_contact: DistrictContact

    error: str

    id: str

    last_sync: typing.Optional[str]

    launch_date: date

    lms_state: typing.Optional[str]

    login_methods: DistrictLoginMethods

    mdr_number: typing.Optional[str]

    name: str

    nces_id: typing.Optional[str]

    pause_end: typing.Optional[str]

    pause_start: typing.Optional[str]

    portal_url: str

    sis_type: str

    state: typing.Optional[str]

class District(RequiredDistrict, OptionalDistrict):
    pass
