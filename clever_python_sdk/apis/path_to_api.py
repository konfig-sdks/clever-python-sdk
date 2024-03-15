import typing_extensions

from clever_python_sdk.paths import PathValues
from clever_python_sdk.apis.paths.courses import Courses
from clever_python_sdk.apis.paths.courses_id import CoursesId
from clever_python_sdk.apis.paths.courses_id_district import CoursesIdDistrict
from clever_python_sdk.apis.paths.courses_id_resources import CoursesIdResources
from clever_python_sdk.apis.paths.courses_id_schools import CoursesIdSchools
from clever_python_sdk.apis.paths.courses_id_sections import CoursesIdSections
from clever_python_sdk.apis.paths.districts import Districts
from clever_python_sdk.apis.paths.districts_id import DistrictsId
from clever_python_sdk.apis.paths.resources import Resources
from clever_python_sdk.apis.paths.resources_id import ResourcesId
from clever_python_sdk.apis.paths.resources_id_courses import ResourcesIdCourses
from clever_python_sdk.apis.paths.resources_id_sections import ResourcesIdSections
from clever_python_sdk.apis.paths.resources_id_users import ResourcesIdUsers
from clever_python_sdk.apis.paths.schools import Schools
from clever_python_sdk.apis.paths.schools_id import SchoolsId
from clever_python_sdk.apis.paths.schools_id_courses import SchoolsIdCourses
from clever_python_sdk.apis.paths.schools_id_district import SchoolsIdDistrict
from clever_python_sdk.apis.paths.schools_id_sections import SchoolsIdSections
from clever_python_sdk.apis.paths.schools_id_terms import SchoolsIdTerms
from clever_python_sdk.apis.paths.schools_id_users import SchoolsIdUsers
from clever_python_sdk.apis.paths.sections import Sections
from clever_python_sdk.apis.paths.sections_id import SectionsId
from clever_python_sdk.apis.paths.sections_id_course import SectionsIdCourse
from clever_python_sdk.apis.paths.sections_id_district import SectionsIdDistrict
from clever_python_sdk.apis.paths.sections_id_resources import SectionsIdResources
from clever_python_sdk.apis.paths.sections_id_school import SectionsIdSchool
from clever_python_sdk.apis.paths.sections_id_term import SectionsIdTerm
from clever_python_sdk.apis.paths.sections_id_users import SectionsIdUsers
from clever_python_sdk.apis.paths.terms import Terms
from clever_python_sdk.apis.paths.terms_id import TermsId
from clever_python_sdk.apis.paths.terms_id_district import TermsIdDistrict
from clever_python_sdk.apis.paths.terms_id_schools import TermsIdSchools
from clever_python_sdk.apis.paths.terms_id_sections import TermsIdSections
from clever_python_sdk.apis.paths.users import Users
from clever_python_sdk.apis.paths.users_id import UsersId
from clever_python_sdk.apis.paths.users_id_district import UsersIdDistrict
from clever_python_sdk.apis.paths.users_id_mycontacts import UsersIdMycontacts
from clever_python_sdk.apis.paths.users_id_mystudents import UsersIdMystudents
from clever_python_sdk.apis.paths.users_id_myteachers import UsersIdMyteachers
from clever_python_sdk.apis.paths.users_id_resources import UsersIdResources
from clever_python_sdk.apis.paths.users_id_schools import UsersIdSchools
from clever_python_sdk.apis.paths.users_id_sections import UsersIdSections

PathToApi = typing_extensions.TypedDict(
    'PathToApi',
    {
        PathValues.COURSES: Courses,
        PathValues.COURSES_ID: CoursesId,
        PathValues.COURSES_ID_DISTRICT: CoursesIdDistrict,
        PathValues.COURSES_ID_RESOURCES: CoursesIdResources,
        PathValues.COURSES_ID_SCHOOLS: CoursesIdSchools,
        PathValues.COURSES_ID_SECTIONS: CoursesIdSections,
        PathValues.DISTRICTS: Districts,
        PathValues.DISTRICTS_ID: DistrictsId,
        PathValues.RESOURCES: Resources,
        PathValues.RESOURCES_ID: ResourcesId,
        PathValues.RESOURCES_ID_COURSES: ResourcesIdCourses,
        PathValues.RESOURCES_ID_SECTIONS: ResourcesIdSections,
        PathValues.RESOURCES_ID_USERS: ResourcesIdUsers,
        PathValues.SCHOOLS: Schools,
        PathValues.SCHOOLS_ID: SchoolsId,
        PathValues.SCHOOLS_ID_COURSES: SchoolsIdCourses,
        PathValues.SCHOOLS_ID_DISTRICT: SchoolsIdDistrict,
        PathValues.SCHOOLS_ID_SECTIONS: SchoolsIdSections,
        PathValues.SCHOOLS_ID_TERMS: SchoolsIdTerms,
        PathValues.SCHOOLS_ID_USERS: SchoolsIdUsers,
        PathValues.SECTIONS: Sections,
        PathValues.SECTIONS_ID: SectionsId,
        PathValues.SECTIONS_ID_COURSE: SectionsIdCourse,
        PathValues.SECTIONS_ID_DISTRICT: SectionsIdDistrict,
        PathValues.SECTIONS_ID_RESOURCES: SectionsIdResources,
        PathValues.SECTIONS_ID_SCHOOL: SectionsIdSchool,
        PathValues.SECTIONS_ID_TERM: SectionsIdTerm,
        PathValues.SECTIONS_ID_USERS: SectionsIdUsers,
        PathValues.TERMS: Terms,
        PathValues.TERMS_ID: TermsId,
        PathValues.TERMS_ID_DISTRICT: TermsIdDistrict,
        PathValues.TERMS_ID_SCHOOLS: TermsIdSchools,
        PathValues.TERMS_ID_SECTIONS: TermsIdSections,
        PathValues.USERS: Users,
        PathValues.USERS_ID: UsersId,
        PathValues.USERS_ID_DISTRICT: UsersIdDistrict,
        PathValues.USERS_ID_MYCONTACTS: UsersIdMycontacts,
        PathValues.USERS_ID_MYSTUDENTS: UsersIdMystudents,
        PathValues.USERS_ID_MYTEACHERS: UsersIdMyteachers,
        PathValues.USERS_ID_RESOURCES: UsersIdResources,
        PathValues.USERS_ID_SCHOOLS: UsersIdSchools,
        PathValues.USERS_ID_SECTIONS: UsersIdSections,
    }
)

path_to_api = PathToApi(
    {
        PathValues.COURSES: Courses,
        PathValues.COURSES_ID: CoursesId,
        PathValues.COURSES_ID_DISTRICT: CoursesIdDistrict,
        PathValues.COURSES_ID_RESOURCES: CoursesIdResources,
        PathValues.COURSES_ID_SCHOOLS: CoursesIdSchools,
        PathValues.COURSES_ID_SECTIONS: CoursesIdSections,
        PathValues.DISTRICTS: Districts,
        PathValues.DISTRICTS_ID: DistrictsId,
        PathValues.RESOURCES: Resources,
        PathValues.RESOURCES_ID: ResourcesId,
        PathValues.RESOURCES_ID_COURSES: ResourcesIdCourses,
        PathValues.RESOURCES_ID_SECTIONS: ResourcesIdSections,
        PathValues.RESOURCES_ID_USERS: ResourcesIdUsers,
        PathValues.SCHOOLS: Schools,
        PathValues.SCHOOLS_ID: SchoolsId,
        PathValues.SCHOOLS_ID_COURSES: SchoolsIdCourses,
        PathValues.SCHOOLS_ID_DISTRICT: SchoolsIdDistrict,
        PathValues.SCHOOLS_ID_SECTIONS: SchoolsIdSections,
        PathValues.SCHOOLS_ID_TERMS: SchoolsIdTerms,
        PathValues.SCHOOLS_ID_USERS: SchoolsIdUsers,
        PathValues.SECTIONS: Sections,
        PathValues.SECTIONS_ID: SectionsId,
        PathValues.SECTIONS_ID_COURSE: SectionsIdCourse,
        PathValues.SECTIONS_ID_DISTRICT: SectionsIdDistrict,
        PathValues.SECTIONS_ID_RESOURCES: SectionsIdResources,
        PathValues.SECTIONS_ID_SCHOOL: SectionsIdSchool,
        PathValues.SECTIONS_ID_TERM: SectionsIdTerm,
        PathValues.SECTIONS_ID_USERS: SectionsIdUsers,
        PathValues.TERMS: Terms,
        PathValues.TERMS_ID: TermsId,
        PathValues.TERMS_ID_DISTRICT: TermsIdDistrict,
        PathValues.TERMS_ID_SCHOOLS: TermsIdSchools,
        PathValues.TERMS_ID_SECTIONS: TermsIdSections,
        PathValues.USERS: Users,
        PathValues.USERS_ID: UsersId,
        PathValues.USERS_ID_DISTRICT: UsersIdDistrict,
        PathValues.USERS_ID_MYCONTACTS: UsersIdMycontacts,
        PathValues.USERS_ID_MYSTUDENTS: UsersIdMystudents,
        PathValues.USERS_ID_MYTEACHERS: UsersIdMyteachers,
        PathValues.USERS_ID_RESOURCES: UsersIdResources,
        PathValues.USERS_ID_SCHOOLS: UsersIdSchools,
        PathValues.USERS_ID_SECTIONS: UsersIdSections,
    }
)
