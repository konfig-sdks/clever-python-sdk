import typing_extensions

from clever_python_sdk.apis.tags import TagValues
from clever_python_sdk.apis.tags.users_api import UsersApi
from clever_python_sdk.apis.tags.sections_api import SectionsApi
from clever_python_sdk.apis.tags.schools_api import SchoolsApi
from clever_python_sdk.apis.tags.courses_api import CoursesApi
from clever_python_sdk.apis.tags.resources_api import ResourcesApi
from clever_python_sdk.apis.tags.terms_api import TermsApi
from clever_python_sdk.apis.tags.districts_api import DistrictsApi

TagToApi = typing_extensions.TypedDict(
    'TagToApi',
    {
        TagValues.USERS: UsersApi,
        TagValues.SECTIONS: SectionsApi,
        TagValues.SCHOOLS: SchoolsApi,
        TagValues.COURSES: CoursesApi,
        TagValues.RESOURCES: ResourcesApi,
        TagValues.TERMS: TermsApi,
        TagValues.DISTRICTS: DistrictsApi,
    }
)

tag_to_api = TagToApi(
    {
        TagValues.USERS: UsersApi,
        TagValues.SECTIONS: SectionsApi,
        TagValues.SCHOOLS: SchoolsApi,
        TagValues.COURSES: CoursesApi,
        TagValues.RESOURCES: ResourcesApi,
        TagValues.TERMS: TermsApi,
        TagValues.DISTRICTS: DistrictsApi,
    }
)
