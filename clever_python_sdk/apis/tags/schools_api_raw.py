# coding: utf-8

"""
    Data API

    Serves the Clever Data API

    The version of the OpenAPI document: 3.1.0
    Generated by: https://konfigthis.com
"""

from clever_python_sdk.paths.schools_id_courses.get import GetCoursesRaw
from clever_python_sdk.paths.schools_id_district.get import GetDistrictRaw
from clever_python_sdk.paths.schools_id_sections.get import GetSectionsRaw
from clever_python_sdk.paths.schools_id.get import GetSpecificSchoolRaw
from clever_python_sdk.paths.schools_id_terms.get import GetTermsRaw
from clever_python_sdk.paths.schools_id_users.get import GetUsersRaw
from clever_python_sdk.paths.schools.get import ListRaw


class SchoolsApiRaw(
    GetCoursesRaw,
    GetDistrictRaw,
    GetSectionsRaw,
    GetSpecificSchoolRaw,
    GetTermsRaw,
    GetUsersRaw,
    ListRaw,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    pass
