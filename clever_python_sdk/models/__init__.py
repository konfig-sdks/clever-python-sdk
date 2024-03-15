# coding: utf-8

# flake8: noqa

# import all models into this package
# if you have many models here with many references from one model to another this may
# raise a RecursionError
# to avoid this, import only the models that you directly need like:
# from from clever_python_sdk.model.pet import Pet
# or import this package, but before doing it, use:
# import sys
# sys.setrecursionlimit(n)

from clever_python_sdk.model.bad_request import BadRequest
from clever_python_sdk.model.contact import Contact
from clever_python_sdk.model.course import Course
from clever_python_sdk.model.course_response import CourseResponse
from clever_python_sdk.model.courses_response import CoursesResponse
from clever_python_sdk.model.credentials import Credentials
from clever_python_sdk.model.disability import Disability
from clever_python_sdk.model.district import District
from clever_python_sdk.model.district_admin import DistrictAdmin
from clever_python_sdk.model.district_contact import DistrictContact
from clever_python_sdk.model.district_login_methods import DistrictLoginMethods
from clever_python_sdk.model.district_response import DistrictResponse
from clever_python_sdk.model.districts_response import DistrictsResponse
from clever_python_sdk.model.internal_error import InternalError
from clever_python_sdk.model.link import Link
from clever_python_sdk.model.location import Location
from clever_python_sdk.model.name import Name
from clever_python_sdk.model.not_found import NotFound
from clever_python_sdk.model.preferred_name import PreferredName
from clever_python_sdk.model.principal import Principal
from clever_python_sdk.model.resource import Resource
from clever_python_sdk.model.resource_response import ResourceResponse
from clever_python_sdk.model.resource_roles import ResourceRoles
from clever_python_sdk.model.resources_response import ResourcesResponse
from clever_python_sdk.model.roles import Roles
from clever_python_sdk.model.school import School
from clever_python_sdk.model.school_enrollment import SchoolEnrollment
from clever_python_sdk.model.school_response import SchoolResponse
from clever_python_sdk.model.schools_response import SchoolsResponse
from clever_python_sdk.model.section import Section
from clever_python_sdk.model.section_response import SectionResponse
from clever_python_sdk.model.section_students import SectionStudents
from clever_python_sdk.model.section_teachers import SectionTeachers
from clever_python_sdk.model.sections_response import SectionsResponse
from clever_python_sdk.model.staff import Staff
from clever_python_sdk.model.staff_roles import StaffRoles
from clever_python_sdk.model.staff_schools import StaffSchools
from clever_python_sdk.model.student import Student
from clever_python_sdk.model.student_relationship import StudentRelationship
from clever_python_sdk.model.student_schools import StudentSchools
from clever_python_sdk.model.teacher import Teacher
from clever_python_sdk.model.teacher_schools import TeacherSchools
from clever_python_sdk.model.term import Term
from clever_python_sdk.model.term_response import TermResponse
from clever_python_sdk.model.terms_response import TermsResponse
from clever_python_sdk.model.user import User
from clever_python_sdk.model.user_response import UserResponse
from clever_python_sdk.model.users_response import UsersResponse
