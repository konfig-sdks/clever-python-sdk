<div align="center">

[![Visit Clever](./header.png)](https://clever.com)

# Clever<a id="clever"></a>

Serves the Clever Data API


</div>

## Table of Contents<a id="table-of-contents"></a>

<!-- toc -->

- [Requirements](#requirements)
- [Installation](#installation)
- [Getting Started](#getting-started)
- [Async](#async)
- [Raw HTTP Response](#raw-http-response)
- [Reference](#reference)
  * [`clever.courses.get_district`](#clevercoursesget_district)
  * [`clever.courses.get_list`](#clevercoursesget_list)
  * [`clever.courses.get_resources`](#clevercoursesget_resources)
  * [`clever.courses.get_schools`](#clevercoursesget_schools)
  * [`clever.courses.get_sections`](#clevercoursesget_sections)
  * [`clever.courses.get_specific_course`](#clevercoursesget_specific_course)
  * [`clever.districts.get_list`](#cleverdistrictsget_list)
  * [`clever.districts.get_specific_district`](#cleverdistrictsget_specific_district)
  * [`clever.resources.get_by_id`](#cleverresourcesget_by_id)
  * [`clever.resources.get_courses`](#cleverresourcesget_courses)
  * [`clever.resources.get_list`](#cleverresourcesget_list)
  * [`clever.resources.get_users`](#cleverresourcesget_users)
  * [`clever.resources.list_sections`](#cleverresourceslist_sections)
  * [`clever.schools.get_courses`](#cleverschoolsget_courses)
  * [`clever.schools.get_district`](#cleverschoolsget_district)
  * [`clever.schools.get_sections`](#cleverschoolsget_sections)
  * [`clever.schools.get_specific_school`](#cleverschoolsget_specific_school)
  * [`clever.schools.get_terms`](#cleverschoolsget_terms)
  * [`clever.schools.get_users`](#cleverschoolsget_users)
  * [`clever.schools.list`](#cleverschoolslist)
  * [`clever.sections.get_course`](#cleversectionsget_course)
  * [`clever.sections.get_district`](#cleversectionsget_district)
  * [`clever.sections.get_list`](#cleversectionsget_list)
  * [`clever.sections.get_resources`](#cleversectionsget_resources)
  * [`clever.sections.get_school`](#cleversectionsget_school)
  * [`clever.sections.get_specific_section`](#cleversectionsget_specific_section)
  * [`clever.sections.get_term`](#cleversectionsget_term)
  * [`clever.sections.get_users`](#cleversectionsget_users)
  * [`clever.terms.get_district_by_id`](#clevertermsget_district_by_id)
  * [`clever.terms.get_list`](#clevertermsget_list)
  * [`clever.terms.get_schools_for_term`](#clevertermsget_schools_for_term)
  * [`clever.terms.get_sections`](#clevertermsget_sections)
  * [`clever.terms.get_specific_term`](#clevertermsget_specific_term)
  * [`clever.users.get_district`](#cleverusersget_district)
  * [`clever.users.get_list`](#cleverusersget_list)
  * [`clever.users.get_my_contacts`](#cleverusersget_my_contacts)
  * [`clever.users.get_resources`](#cleverusersget_resources)
  * [`clever.users.get_schools`](#cleverusersget_schools)
  * [`clever.users.get_sections`](#cleverusersget_sections)
  * [`clever.users.get_student_users`](#cleverusersget_student_users)
  * [`clever.users.get_teachers_for_user`](#cleverusersget_teachers_for_user)
  * [`clever.users.get_user_by_id`](#cleverusersget_user_by_id)

<!-- tocstop -->

## Requirements<a id="requirements"></a>

Python >=3.7

## Installation<a id="installation"></a>
<div align="center">
  <a href="https://konfigthis.com/sdk-sign-up?company=Clever&language=Python">
    <img src="https://raw.githubusercontent.com/konfig-dev/brand-assets/HEAD/cta-images/python-cta.png" width="70%">
  </a>
</div>

## Getting Started<a id="getting-started"></a>

```python
from pprint import pprint
from clever_python_sdk import Clever, ApiException

clever = Clever(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)

try:
    get_district_response = clever.courses.get_district(
        id="id_example",
    )
    print(get_district_response)
except ApiException as e:
    print("Exception when calling CoursesApi.get_district: %s\n" % e)
    pprint(e.body)
    if e.status == 404:
        pprint(e.body["message"])
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```

## Async<a id="async"></a>

`async` support is available by prepending `a` to any method.

```python
import asyncio
from pprint import pprint
from clever_python_sdk import Clever, ApiException

clever = Clever(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)


async def main():
    try:
        get_district_response = await clever.courses.aget_district(
            id="id_example",
        )
        print(get_district_response)
    except ApiException as e:
        print("Exception when calling CoursesApi.get_district: %s\n" % e)
        pprint(e.body)
        if e.status == 404:
            pprint(e.body["message"])
        pprint(e.headers)
        pprint(e.status)
        pprint(e.reason)
        pprint(e.round_trip_time)


asyncio.run(main())
```

## Raw HTTP Response<a id="raw-http-response"></a>

To access raw HTTP response values, use the `.raw` namespace.

```python
from pprint import pprint
from clever_python_sdk import Clever, ApiException

clever = Clever(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)

try:
    get_district_response = clever.courses.raw.get_district(
        id="id_example",
    )
    pprint(get_district_response.body)
    pprint(get_district_response.body["data"])
    pprint(get_district_response.headers)
    pprint(get_district_response.status)
    pprint(get_district_response.round_trip_time)
except ApiException as e:
    print("Exception when calling CoursesApi.get_district: %s\n" % e)
    pprint(e.body)
    if e.status == 404:
        pprint(e.body["message"])
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```


## Reference<a id="reference"></a>
### `clever.courses.get_district`<a id="clevercoursesget_district"></a>

Returns the district for a course

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_district_response = clever.courses.get_district(
    id="id_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`DistrictResponse`](./clever_python_sdk/pydantic/district_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/courses/{id}/district` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `clever.courses.get_list`<a id="clevercoursesget_list"></a>

Returns a list of courses

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_list_response = clever.courses.get_list(
    limit=1,
    starting_after="string_example",
    ending_before="string_example",
    count="",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### limit: `int`<a id="limit-int"></a>

##### starting_after: `str`<a id="starting_after-str"></a>

##### ending_before: `str`<a id="ending_before-str"></a>

##### count: `str`<a id="count-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`CoursesResponse`](./clever_python_sdk/pydantic/courses_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/courses` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `clever.courses.get_resources`<a id="clevercoursesget_resources"></a>

Returns the resources for a course

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_resources_response = clever.courses.get_resources(
    id="id_example",
    limit=1,
    starting_after="string_example",
    ending_before="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

##### limit: `int`<a id="limit-int"></a>

##### starting_after: `str`<a id="starting_after-str"></a>

##### ending_before: `str`<a id="ending_before-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`ResourcesResponse`](./clever_python_sdk/pydantic/resources_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/courses/{id}/resources` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `clever.courses.get_schools`<a id="clevercoursesget_schools"></a>

Returns the schools for a course

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_schools_response = clever.courses.get_schools(
    id="id_example",
    limit=1,
    starting_after="string_example",
    ending_before="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

##### limit: `int`<a id="limit-int"></a>

##### starting_after: `str`<a id="starting_after-str"></a>

##### ending_before: `str`<a id="ending_before-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`SchoolsResponse`](./clever_python_sdk/pydantic/schools_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/courses/{id}/schools` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `clever.courses.get_sections`<a id="clevercoursesget_sections"></a>

Returns the sections for a course

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_sections_response = clever.courses.get_sections(
    id="id_example",
    limit=1,
    starting_after="string_example",
    ending_before="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

##### limit: `int`<a id="limit-int"></a>

##### starting_after: `str`<a id="starting_after-str"></a>

##### ending_before: `str`<a id="ending_before-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`SectionsResponse`](./clever_python_sdk/pydantic/sections_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/courses/{id}/sections` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `clever.courses.get_specific_course`<a id="clevercoursesget_specific_course"></a>

Returns a specific course

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_specific_course_response = clever.courses.get_specific_course(
    id="id_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`CourseResponse`](./clever_python_sdk/pydantic/course_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/courses/{id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `clever.districts.get_list`<a id="cleverdistrictsget_list"></a>

Returns a list of districts. In practice this will only return the one district associated with the bearer token

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_list_response = clever.districts.get_list(
    count="",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### count: `str`<a id="count-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`DistrictsResponse`](./clever_python_sdk/pydantic/districts_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/districts` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `clever.districts.get_specific_district`<a id="cleverdistrictsget_specific_district"></a>

Returns a specific district

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_specific_district_response = clever.districts.get_specific_district(
    id="id_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`DistrictResponse`](./clever_python_sdk/pydantic/district_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/districts/{id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `clever.resources.get_by_id`<a id="cleverresourcesget_by_id"></a>

Returns a specific resource

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_by_id_response = clever.resources.get_by_id(
    id="id_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`ResourceResponse`](./clever_python_sdk/pydantic/resource_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/resources/{id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `clever.resources.get_courses`<a id="cleverresourcesget_courses"></a>

Returns the courses for a resource

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_courses_response = clever.resources.get_courses(
    id="id_example",
    limit=1,
    starting_after="string_example",
    ending_before="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

##### limit: `int`<a id="limit-int"></a>

##### starting_after: `str`<a id="starting_after-str"></a>

##### ending_before: `str`<a id="ending_before-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`CoursesResponse`](./clever_python_sdk/pydantic/courses_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/resources/{id}/courses` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `clever.resources.get_list`<a id="cleverresourcesget_list"></a>

Returns a list of resources

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_list_response = clever.resources.get_list(
    limit=1,
    starting_after="string_example",
    ending_before="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### limit: `int`<a id="limit-int"></a>

##### starting_after: `str`<a id="starting_after-str"></a>

##### ending_before: `str`<a id="ending_before-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`ResourcesResponse`](./clever_python_sdk/pydantic/resources_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/resources` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `clever.resources.get_users`<a id="cleverresourcesget_users"></a>

Returns the student and/or teacher users for a resource

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_users_response = clever.resources.get_users(
    id="id_example",
    role="student",
    limit=1,
    starting_after="string_example",
    ending_before="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

##### role: `str`<a id="role-str"></a>

##### limit: `int`<a id="limit-int"></a>

##### starting_after: `str`<a id="starting_after-str"></a>

##### ending_before: `str`<a id="ending_before-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`UsersResponse`](./clever_python_sdk/pydantic/users_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/resources/{id}/users` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `clever.resources.list_sections`<a id="cleverresourceslist_sections"></a>

Returns the sections for a resource

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_sections_response = clever.resources.list_sections(
    id="id_example",
    limit=1,
    starting_after="string_example",
    ending_before="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

##### limit: `int`<a id="limit-int"></a>

##### starting_after: `str`<a id="starting_after-str"></a>

##### ending_before: `str`<a id="ending_before-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`SectionsResponse`](./clever_python_sdk/pydantic/sections_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/resources/{id}/sections` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `clever.schools.get_courses`<a id="cleverschoolsget_courses"></a>

Returns the courses for a school

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_courses_response = clever.schools.get_courses(
    id="id_example",
    limit=1,
    starting_after="string_example",
    ending_before="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

##### limit: `int`<a id="limit-int"></a>

##### starting_after: `str`<a id="starting_after-str"></a>

##### ending_before: `str`<a id="ending_before-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`CoursesResponse`](./clever_python_sdk/pydantic/courses_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/schools/{id}/courses` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `clever.schools.get_district`<a id="cleverschoolsget_district"></a>

Returns the district for a school

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_district_response = clever.schools.get_district(
    id="id_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`DistrictResponse`](./clever_python_sdk/pydantic/district_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/schools/{id}/district` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `clever.schools.get_sections`<a id="cleverschoolsget_sections"></a>

Returns the sections for a school

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_sections_response = clever.schools.get_sections(
    id="id_example",
    limit=1,
    starting_after="string_example",
    ending_before="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

##### limit: `int`<a id="limit-int"></a>

##### starting_after: `str`<a id="starting_after-str"></a>

##### ending_before: `str`<a id="ending_before-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`SectionsResponse`](./clever_python_sdk/pydantic/sections_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/schools/{id}/sections` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `clever.schools.get_specific_school`<a id="cleverschoolsget_specific_school"></a>

Returns a specific school

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_specific_school_response = clever.schools.get_specific_school(
    id="id_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`SchoolResponse`](./clever_python_sdk/pydantic/school_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/schools/{id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `clever.schools.get_terms`<a id="cleverschoolsget_terms"></a>

Returns the terms for a school

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_terms_response = clever.schools.get_terms(
    id="id_example",
    limit=1,
    starting_after="string_example",
    ending_before="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

##### limit: `int`<a id="limit-int"></a>

##### starting_after: `str`<a id="starting_after-str"></a>

##### ending_before: `str`<a id="ending_before-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`TermsResponse`](./clever_python_sdk/pydantic/terms_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/schools/{id}/terms` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `clever.schools.get_users`<a id="cleverschoolsget_users"></a>

Returns the staff, student, and/or teacher users for a school

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_users_response = clever.schools.get_users(
    id="id_example",
    role="staff",
    primary="",
    limit=1,
    starting_after="string_example",
    ending_before="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

##### role: `str`<a id="role-str"></a>

##### primary: `str`<a id="primary-str"></a>

##### limit: `int`<a id="limit-int"></a>

##### starting_after: `str`<a id="starting_after-str"></a>

##### ending_before: `str`<a id="ending_before-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`UsersResponse`](./clever_python_sdk/pydantic/users_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/schools/{id}/users` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `clever.schools.list`<a id="cleverschoolslist"></a>

Returns a list of schools

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_response = clever.schools.list(
    limit=1,
    starting_after="string_example",
    ending_before="string_example",
    count="",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### limit: `int`<a id="limit-int"></a>

##### starting_after: `str`<a id="starting_after-str"></a>

##### ending_before: `str`<a id="ending_before-str"></a>

##### count: `str`<a id="count-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`SchoolsResponse`](./clever_python_sdk/pydantic/schools_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/schools` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `clever.sections.get_course`<a id="cleversectionsget_course"></a>

Returns the course for a section

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_course_response = clever.sections.get_course(
    id="id_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`CourseResponse`](./clever_python_sdk/pydantic/course_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/sections/{id}/course` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `clever.sections.get_district`<a id="cleversectionsget_district"></a>

Returns the district for a section

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_district_response = clever.sections.get_district(
    id="id_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`DistrictResponse`](./clever_python_sdk/pydantic/district_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/sections/{id}/district` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `clever.sections.get_list`<a id="cleversectionsget_list"></a>

Returns a list of sections

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_list_response = clever.sections.get_list(
    limit=1,
    starting_after="string_example",
    ending_before="string_example",
    count="",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### limit: `int`<a id="limit-int"></a>

##### starting_after: `str`<a id="starting_after-str"></a>

##### ending_before: `str`<a id="ending_before-str"></a>

##### count: `str`<a id="count-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`SectionsResponse`](./clever_python_sdk/pydantic/sections_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/sections` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `clever.sections.get_resources`<a id="cleversectionsget_resources"></a>

Returns the resources for a section

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_resources_response = clever.sections.get_resources(
    id="id_example",
    limit=1,
    starting_after="string_example",
    ending_before="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

##### limit: `int`<a id="limit-int"></a>

##### starting_after: `str`<a id="starting_after-str"></a>

##### ending_before: `str`<a id="ending_before-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`ResourcesResponse`](./clever_python_sdk/pydantic/resources_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/sections/{id}/resources` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `clever.sections.get_school`<a id="cleversectionsget_school"></a>

Returns the school for a section

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_school_response = clever.sections.get_school(
    id="id_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`SchoolResponse`](./clever_python_sdk/pydantic/school_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/sections/{id}/school` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `clever.sections.get_specific_section`<a id="cleversectionsget_specific_section"></a>

Returns a specific section

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_specific_section_response = clever.sections.get_specific_section(
    id="id_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`SectionResponse`](./clever_python_sdk/pydantic/section_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/sections/{id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `clever.sections.get_term`<a id="cleversectionsget_term"></a>

Returns the term for a section

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_term_response = clever.sections.get_term(
    id="id_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`TermResponse`](./clever_python_sdk/pydantic/term_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/sections/{id}/term` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `clever.sections.get_users`<a id="cleversectionsget_users"></a>

Returns the student and/or teacher users for a section

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_users_response = clever.sections.get_users(
    id="id_example",
    role="student",
    limit=1,
    starting_after="string_example",
    ending_before="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

##### role: `str`<a id="role-str"></a>

##### limit: `int`<a id="limit-int"></a>

##### starting_after: `str`<a id="starting_after-str"></a>

##### ending_before: `str`<a id="ending_before-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`UsersResponse`](./clever_python_sdk/pydantic/users_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/sections/{id}/users` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `clever.terms.get_district_by_id`<a id="clevertermsget_district_by_id"></a>

Returns the district for a term

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_district_by_id_response = clever.terms.get_district_by_id(
    id="id_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`DistrictResponse`](./clever_python_sdk/pydantic/district_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/terms/{id}/district` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `clever.terms.get_list`<a id="clevertermsget_list"></a>

Returns a list of terms

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_list_response = clever.terms.get_list(
    limit=1,
    starting_after="string_example",
    ending_before="string_example",
    count="",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### limit: `int`<a id="limit-int"></a>

##### starting_after: `str`<a id="starting_after-str"></a>

##### ending_before: `str`<a id="ending_before-str"></a>

##### count: `str`<a id="count-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`TermsResponse`](./clever_python_sdk/pydantic/terms_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/terms` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `clever.terms.get_schools_for_term`<a id="clevertermsget_schools_for_term"></a>

Returns the schools for a term

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_schools_for_term_response = clever.terms.get_schools_for_term(
    id="id_example",
    limit=1,
    starting_after="string_example",
    ending_before="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

##### limit: `int`<a id="limit-int"></a>

##### starting_after: `str`<a id="starting_after-str"></a>

##### ending_before: `str`<a id="ending_before-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`SchoolsResponse`](./clever_python_sdk/pydantic/schools_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/terms/{id}/schools` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `clever.terms.get_sections`<a id="clevertermsget_sections"></a>

Returns the sections for a term

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_sections_response = clever.terms.get_sections(
    id="id_example",
    limit=1,
    starting_after="string_example",
    ending_before="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

##### limit: `int`<a id="limit-int"></a>

##### starting_after: `str`<a id="starting_after-str"></a>

##### ending_before: `str`<a id="ending_before-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`SectionsResponse`](./clever_python_sdk/pydantic/sections_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/terms/{id}/sections` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `clever.terms.get_specific_term`<a id="clevertermsget_specific_term"></a>

Returns a specific term

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_specific_term_response = clever.terms.get_specific_term(
    id="id_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`TermResponse`](./clever_python_sdk/pydantic/term_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/terms/{id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `clever.users.get_district`<a id="cleverusersget_district"></a>

Returns the district for a user

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_district_response = clever.users.get_district(
    id="id_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`DistrictResponse`](./clever_python_sdk/pydantic/district_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/users/{id}/district` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `clever.users.get_list`<a id="cleverusersget_list"></a>

Returns a list of contact, district admin, staff, student, and/or teacher users

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_list_response = clever.users.get_list(
    limit=1,
    role="contact",
    starting_after="string_example",
    ending_before="string_example",
    count="",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### limit: `int`<a id="limit-int"></a>

##### role: `str`<a id="role-str"></a>

##### starting_after: `str`<a id="starting_after-str"></a>

##### ending_before: `str`<a id="ending_before-str"></a>

##### count: `str`<a id="count-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`UsersResponse`](./clever_python_sdk/pydantic/users_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/users` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `clever.users.get_my_contacts`<a id="cleverusersget_my_contacts"></a>

Returns the contact users for a student user

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_my_contacts_response = clever.users.get_my_contacts(
    id="id_example",
    limit=1,
    starting_after="string_example",
    ending_before="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

##### limit: `int`<a id="limit-int"></a>

##### starting_after: `str`<a id="starting_after-str"></a>

##### ending_before: `str`<a id="ending_before-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`UsersResponse`](./clever_python_sdk/pydantic/users_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/users/{id}/mycontacts` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `clever.users.get_resources`<a id="cleverusersget_resources"></a>

Returns the resources for a user

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_resources_response = clever.users.get_resources(
    id="id_example",
    limit=1,
    starting_after="string_example",
    ending_before="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

##### limit: `int`<a id="limit-int"></a>

##### starting_after: `str`<a id="starting_after-str"></a>

##### ending_before: `str`<a id="ending_before-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`ResourcesResponse`](./clever_python_sdk/pydantic/resources_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/users/{id}/resources` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `clever.users.get_schools`<a id="cleverusersget_schools"></a>

Returns the schools for a user

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_schools_response = clever.users.get_schools(
    id="id_example",
    primary="",
    limit=1,
    starting_after="string_example",
    ending_before="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

##### primary: `str`<a id="primary-str"></a>

##### limit: `int`<a id="limit-int"></a>

##### starting_after: `str`<a id="starting_after-str"></a>

##### ending_before: `str`<a id="ending_before-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`SchoolsResponse`](./clever_python_sdk/pydantic/schools_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/users/{id}/schools` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `clever.users.get_sections`<a id="cleverusersget_sections"></a>

Returns the sections for a user

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_sections_response = clever.users.get_sections(
    id="id_example",
    limit=1,
    starting_after="string_example",
    ending_before="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

##### limit: `int`<a id="limit-int"></a>

##### starting_after: `str`<a id="starting_after-str"></a>

##### ending_before: `str`<a id="ending_before-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`SectionsResponse`](./clever_python_sdk/pydantic/sections_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/users/{id}/sections` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `clever.users.get_student_users`<a id="cleverusersget_student_users"></a>

Returns the student users for a teacher or contact user

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_student_users_response = clever.users.get_student_users(
    id="id_example",
    limit=1,
    starting_after="string_example",
    ending_before="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

##### limit: `int`<a id="limit-int"></a>

##### starting_after: `str`<a id="starting_after-str"></a>

##### ending_before: `str`<a id="ending_before-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`UsersResponse`](./clever_python_sdk/pydantic/users_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/users/{id}/mystudents` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `clever.users.get_teachers_for_user`<a id="cleverusersget_teachers_for_user"></a>

Returns the teacher users for a student user

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_teachers_for_user_response = clever.users.get_teachers_for_user(
    id="id_example",
    limit=1,
    starting_after="string_example",
    ending_before="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

##### limit: `int`<a id="limit-int"></a>

##### starting_after: `str`<a id="starting_after-str"></a>

##### ending_before: `str`<a id="ending_before-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`UsersResponse`](./clever_python_sdk/pydantic/users_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/users/{id}/myteachers` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `clever.users.get_user_by_id`<a id="cleverusersget_user_by_id"></a>

Returns a specific user

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_user_by_id_response = clever.users.get_user_by_id(
    id="id_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`UserResponse`](./clever_python_sdk/pydantic/user_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/users/{id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---


## Author<a id="author"></a>
This Python package is automatically generated by [Konfig](https://konfigthis.com)
