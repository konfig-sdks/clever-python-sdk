# coding: utf-8

"""
    Data API

    Serves the Clever Data API

    The version of the OpenAPI document: 3.1.0
    Generated by: https://konfigthis.com
"""

from clever_python_sdk.paths.districts.get import GetList
from clever_python_sdk.paths.districts_id.get import GetSpecificDistrict
from clever_python_sdk.apis.tags.districts_api_raw import DistrictsApiRaw


class DistrictsApi(
    GetList,
    GetSpecificDistrict,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    raw: DistrictsApiRaw

    def __init__(self, api_client=None):
        super().__init__(api_client)
        self.raw = DistrictsApiRaw(api_client)
