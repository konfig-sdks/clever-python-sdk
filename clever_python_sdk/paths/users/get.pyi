# coding: utf-8

"""
    Data API

    Serves the Clever Data API

    The version of the OpenAPI document: 3.1.0
    Generated by: https://konfigthis.com
"""

from dataclasses import dataclass
import typing_extensions
import urllib3
from pydantic import RootModel
from clever_python_sdk.request_before_hook import request_before_hook
import json
from urllib3._collections import HTTPHeaderDict

from clever_python_sdk.api_response import AsyncGeneratorResponse
from clever_python_sdk import api_client, exceptions
from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from clever_python_sdk import schemas  # noqa: F401

from clever_python_sdk.model.users_response import UsersResponse as UsersResponseSchema

from clever_python_sdk.type.users_response import UsersResponse

from ...api_client import Dictionary
from clever_python_sdk.pydantic.users_response import UsersResponse as UsersResponsePydantic

# Query params
LimitSchema = schemas.IntSchema


class RoleSchema(
    schemas.EnumBase,
    schemas.StrSchema
):
    
    @schemas.classproperty
    def CONTACT(cls):
        return cls("contact")
    
    @schemas.classproperty
    def DISTRICT_ADMIN(cls):
        return cls("district_admin")
    
    @schemas.classproperty
    def STAFF(cls):
        return cls("staff")
    
    @schemas.classproperty
    def STUDENT(cls):
        return cls("student")
    
    @schemas.classproperty
    def TEACHER(cls):
        return cls("teacher")
StartingAfterSchema = schemas.StrSchema
EndingBeforeSchema = schemas.StrSchema


class CountSchema(
    schemas.EnumBase,
    schemas.StrSchema
):
    
    @schemas.classproperty
    def EMPTY(cls):
        return cls("")
    
    @schemas.classproperty
    def TRUE(cls):
        return cls("true")
    
    @schemas.classproperty
    def FALSE(cls):
        return cls("false")
    
    @schemas.classproperty
    def UNDEFINED(cls):
        return cls("undefined")
RequestRequiredQueryParams = typing_extensions.TypedDict(
    'RequestRequiredQueryParams',
    {
    }
)
RequestOptionalQueryParams = typing_extensions.TypedDict(
    'RequestOptionalQueryParams',
    {
        'limit': typing.Union[LimitSchema, decimal.Decimal, int, ],
        'role': typing.Union[RoleSchema, str, ],
        'starting_after': typing.Union[StartingAfterSchema, str, ],
        'ending_before': typing.Union[EndingBeforeSchema, str, ],
        'count': typing.Union[CountSchema, str, ],
    },
    total=False
)


class RequestQueryParams(RequestRequiredQueryParams, RequestOptionalQueryParams):
    pass


request_query_limit = api_client.QueryParameter(
    name="limit",
    style=api_client.ParameterStyle.FORM,
    schema=LimitSchema,
    explode=True,
)
request_query_role = api_client.QueryParameter(
    name="role",
    style=api_client.ParameterStyle.FORM,
    schema=RoleSchema,
    explode=True,
)
request_query_starting_after = api_client.QueryParameter(
    name="starting_after",
    style=api_client.ParameterStyle.FORM,
    schema=StartingAfterSchema,
    explode=True,
)
request_query_ending_before = api_client.QueryParameter(
    name="ending_before",
    style=api_client.ParameterStyle.FORM,
    schema=EndingBeforeSchema,
    explode=True,
)
request_query_count = api_client.QueryParameter(
    name="count",
    style=api_client.ParameterStyle.FORM,
    schema=CountSchema,
    explode=True,
)
SchemaFor200ResponseBodyApplicationJson = UsersResponseSchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: UsersResponse


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: UsersResponse


_response_for_200 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor200,
    response_cls_async=ApiResponseFor200Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor200ResponseBodyApplicationJson),
    },
)
_all_accept_content_types = (
    'application/json',
)


class BaseApi(api_client.Api):

    def _get_list_mapped_args(
        self,
        limit: typing.Optional[int] = None,
        role: typing.Optional[str] = None,
        starting_after: typing.Optional[str] = None,
        ending_before: typing.Optional[str] = None,
        count: typing.Optional[str] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _query_params = {}
        if limit is not None:
            _query_params["limit"] = limit
        if role is not None:
            _query_params["role"] = role
        if starting_after is not None:
            _query_params["starting_after"] = starting_after
        if ending_before is not None:
            _query_params["ending_before"] = ending_before
        if count is not None:
            _query_params["count"] = count
        args.query = _query_params
        return args

    async def _aget_list_oapg(
        self,
            query_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        """
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        used_path = path.value
    
        prefix_separator_iterator = None
        for parameter in (
            request_query_limit,
            request_query_role,
            request_query_starting_after,
            request_query_ending_before,
            request_query_count,
        ):
            parameter_data = query_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            if prefix_separator_iterator is None:
                prefix_separator_iterator = parameter.get_prefix_separator_iterator()
            serialized_data = parameter.serialize(parameter_data, prefix_separator_iterator)
            for serialized_value in serialized_data.values():
                used_path += serialized_value
    
        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'get'.upper()
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/users',
            auth_settings=_auth,
            headers=_headers,
        )
    
        response = await self.api_client.async_call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            auth_settings=_auth,
            prefix_separator_iterator=prefix_separator_iterator,
            timeout=timeout,
            **kwargs
        )
    
        if stream:
            if not 200 <= response.http_response.status <= 299:
                body = (await response.http_response.content.read()).decode("utf-8")
                raise exceptions.ApiStreamingException(
                    status=response.http_response.status,
                    reason=response.http_response.reason,
                    body=body,
                )
    
            async def stream_iterator():
                """
                iterates over response.http_response.content and closes connection once iteration has finished
                """
                async for line in response.http_response.content:
                    if line == b'\r\n':
                        continue
                    yield line
                response.http_response.close()
                await response.session.close()
            return AsyncGeneratorResponse(
                content=stream_iterator(),
                headers=response.http_response.headers,
                status=response.http_response.status,
                response=response.http_response
            )
    
        response_for_status = _status_code_to_response.get(str(response.http_response.status))
        if response_for_status:
            api_response = await response_for_status.deserialize_async(
                                                    response,
                                                    self.api_client.configuration,
                                                    skip_deserialization=skip_deserialization
                                                )
        else:
            # If response data is JSON then deserialize for SDK consumer convenience
            is_json = api_client.JSONDetector._content_type_is_json(response.http_response.headers.get('Content-Type', ''))
            api_response = api_client.ApiResponseWithoutDeserializationAsync(
                body=await response.http_response.json() if is_json else await response.http_response.text(),
                response=response.http_response,
                round_trip_time=response.round_trip_time,
                status=response.http_response.status,
                headers=response.http_response.headers,
            )
    
        if not 200 <= api_response.status <= 299:
            raise exceptions.ApiException(api_response=api_response)
    
        # cleanup session / response
        response.http_response.close()
        await response.session.close()
    
        return api_response


    def _get_list_oapg(
        self,
            query_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        """
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        used_path = path.value
    
        prefix_separator_iterator = None
        for parameter in (
            request_query_limit,
            request_query_role,
            request_query_starting_after,
            request_query_ending_before,
            request_query_count,
        ):
            parameter_data = query_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            if prefix_separator_iterator is None:
                prefix_separator_iterator = parameter.get_prefix_separator_iterator()
            serialized_data = parameter.serialize(parameter_data, prefix_separator_iterator)
            for serialized_value in serialized_data.values():
                used_path += serialized_value
    
        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'get'.upper()
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/users',
            auth_settings=_auth,
            headers=_headers,
        )
    
        response = self.api_client.call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            auth_settings=_auth,
            prefix_separator_iterator=prefix_separator_iterator,
            timeout=timeout,
        )
    
        response_for_status = _status_code_to_response.get(str(response.http_response.status))
        if response_for_status:
            api_response = response_for_status.deserialize(
                                                    response,
                                                    self.api_client.configuration,
                                                    skip_deserialization=skip_deserialization
                                                )
        else:
            # If response data is JSON then deserialize for SDK consumer convenience
            is_json = api_client.JSONDetector._content_type_is_json(response.http_response.headers.get('Content-Type', ''))
            api_response = api_client.ApiResponseWithoutDeserialization(
                body=json.loads(response.http_response.data) if is_json else response.http_response.data,
                response=response.http_response,
                round_trip_time=response.round_trip_time,
                status=response.http_response.status,
                headers=response.http_response.headers,
            )
    
        if not 200 <= api_response.status <= 299:
            raise exceptions.ApiException(api_response=api_response)
    
        return api_response


class GetListRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def aget_list(
        self,
        limit: typing.Optional[int] = None,
        role: typing.Optional[str] = None,
        starting_after: typing.Optional[str] = None,
        ending_before: typing.Optional[str] = None,
        count: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._get_list_mapped_args(
            limit=limit,
            role=role,
            starting_after=starting_after,
            ending_before=ending_before,
            count=count,
        )
        return await self._aget_list_oapg(
            query_params=args.query,
            **kwargs,
        )
    
    def get_list(
        self,
        limit: typing.Optional[int] = None,
        role: typing.Optional[str] = None,
        starting_after: typing.Optional[str] = None,
        ending_before: typing.Optional[str] = None,
        count: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._get_list_mapped_args(
            limit=limit,
            role=role,
            starting_after=starting_after,
            ending_before=ending_before,
            count=count,
        )
        return self._get_list_oapg(
            query_params=args.query,
        )

class GetList(BaseApi):

    async def aget_list(
        self,
        limit: typing.Optional[int] = None,
        role: typing.Optional[str] = None,
        starting_after: typing.Optional[str] = None,
        ending_before: typing.Optional[str] = None,
        count: typing.Optional[str] = None,
        validate: bool = False,
        **kwargs,
    ) -> UsersResponsePydantic:
        raw_response = await self.raw.aget_list(
            limit=limit,
            role=role,
            starting_after=starting_after,
            ending_before=ending_before,
            count=count,
            **kwargs,
        )
        if validate:
            return UsersResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(UsersResponsePydantic, raw_response.body)
    
    
    def get_list(
        self,
        limit: typing.Optional[int] = None,
        role: typing.Optional[str] = None,
        starting_after: typing.Optional[str] = None,
        ending_before: typing.Optional[str] = None,
        count: typing.Optional[str] = None,
        validate: bool = False,
    ) -> UsersResponsePydantic:
        raw_response = self.raw.get_list(
            limit=limit,
            role=role,
            starting_after=starting_after,
            ending_before=ending_before,
            count=count,
        )
        if validate:
            return UsersResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(UsersResponsePydantic, raw_response.body)


class ApiForget(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def aget(
        self,
        limit: typing.Optional[int] = None,
        role: typing.Optional[str] = None,
        starting_after: typing.Optional[str] = None,
        ending_before: typing.Optional[str] = None,
        count: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._get_list_mapped_args(
            limit=limit,
            role=role,
            starting_after=starting_after,
            ending_before=ending_before,
            count=count,
        )
        return await self._aget_list_oapg(
            query_params=args.query,
            **kwargs,
        )
    
    def get(
        self,
        limit: typing.Optional[int] = None,
        role: typing.Optional[str] = None,
        starting_after: typing.Optional[str] = None,
        ending_before: typing.Optional[str] = None,
        count: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._get_list_mapped_args(
            limit=limit,
            role=role,
            starting_after=starting_after,
            ending_before=ending_before,
            count=count,
        )
        return self._get_list_oapg(
            query_params=args.query,
        )

