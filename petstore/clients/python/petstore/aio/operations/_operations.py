# pylint: disable=too-many-lines
# coding=utf-8

from io import IOBase
import json
import sys
from typing import Any, Callable, Dict, IO, Optional, TypeVar, Union, overload

from corehttp.exceptions import (
    ClientAuthenticationError,
    HttpResponseError,
    ResourceExistsError,
    ResourceNotFoundError,
    ResourceNotModifiedError,
    StreamClosedError,
    StreamConsumedError,
    map_error,
)
from corehttp.rest import AsyncHttpResponse, HttpRequest
from corehttp.runtime.pipeline import PipelineResponse
from corehttp.utils import case_insensitive_dict

from ... import models as _models
from ..._model_base import SdkJSONEncoder, _deserialize
from ...operations._operations import (
    build_checkups_create_or_update_request,
    build_checkups_list_request,
    build_owner_checkups_create_or_update_request,
    build_owner_checkups_list_request,
    build_owner_insurance_get_request,
    build_owner_insurance_update_request,
    build_owners_create_request,
    build_owners_delete_request,
    build_owners_get_request,
    build_owners_list_request,
    build_owners_update_request,
    build_pet_checkups_create_or_update_request,
    build_pet_checkups_list_request,
    build_pet_insurance_get_request,
    build_pet_insurance_update_request,
    build_pets_create_request,
    build_pets_delete_request,
    build_pets_get_request,
    build_pets_list_request,
    build_pets_update_request,
    build_toy_insurance_get_request,
    build_toy_insurance_update_request,
    build_toys_get_request,
    build_toys_list_request,
)

if sys.version_info >= (3, 9):
    from collections.abc import MutableMapping
else:
    from typing import MutableMapping  # type: ignore
JSON = MutableMapping[str, Any]  # pylint: disable=unsubscriptable-object
T = TypeVar("T")
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]


class PetsOperations:
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through
        :class:`~petstore.aio.PetStoreClient`'s
        :attr:`pets` attribute.
    """

    def __init__(self, *args, **kwargs) -> None:
        input_args = list(args)
        self._client = input_args.pop(0) if input_args else kwargs.pop("client")
        self._config = input_args.pop(0) if input_args else kwargs.pop("config")
        self._serialize = input_args.pop(0) if input_args else kwargs.pop("serializer")
        self._deserialize = input_args.pop(0) if input_args else kwargs.pop("deserializer")

    async def get(self, pet_id: int, **kwargs: Any) -> _models.Pet:
        """Gets an instance of the resource.

        :param pet_id: Required.
        :type pet_id: int
        :return: Pet. The Pet is compatible with MutableMapping
        :rtype: ~petstore.models.Pet
        :raises ~corehttp.exceptions.HttpResponseError:
        """
        error_map: MutableMapping = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = kwargs.pop("params", {}) or {}

        cls: ClsType[_models.Pet] = kwargs.pop("cls", None)

        _request = build_pets_get_request(
            pet_id=pet_id,
            headers=_headers,
            params=_params,
        )
        path_format_arguments = {
            "endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, "str", skip_quote=True),
        }
        _request.url = self._client.format_url(_request.url, **path_format_arguments)

        _stream = kwargs.pop("stream", False)
        pipeline_response: PipelineResponse = await self._client.pipeline.run(_request, stream=_stream, **kwargs)

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            if _stream:
                try:
                    await response.read()  # Load the body in memory and close the socket
                except (StreamConsumedError, StreamClosedError):
                    pass
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = _deserialize(_models.PetStoreError, response.json())
            raise HttpResponseError(response=response, model=error)

        if _stream:
            deserialized = response.iter_bytes()
        else:
            deserialized = _deserialize(_models.Pet, response.json())

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore

    @overload
    async def update(
        self, pet_id: int, properties: _models.PetUpdate, *, content_type: str = "application/json", **kwargs: Any
    ) -> _models.Pet:
        """Updates an existing instance of the resource.

        :param pet_id: Required.
        :type pet_id: int
        :param properties: Required.
        :type properties: ~petstore.models.PetUpdate
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: Pet. The Pet is compatible with MutableMapping
        :rtype: ~petstore.models.Pet
        :raises ~corehttp.exceptions.HttpResponseError:
        """

    @overload
    async def update(
        self, pet_id: int, properties: JSON, *, content_type: str = "application/json", **kwargs: Any
    ) -> _models.Pet:
        """Updates an existing instance of the resource.

        :param pet_id: Required.
        :type pet_id: int
        :param properties: Required.
        :type properties: JSON
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: Pet. The Pet is compatible with MutableMapping
        :rtype: ~petstore.models.Pet
        :raises ~corehttp.exceptions.HttpResponseError:
        """

    @overload
    async def update(
        self, pet_id: int, properties: IO[bytes], *, content_type: str = "application/json", **kwargs: Any
    ) -> _models.Pet:
        """Updates an existing instance of the resource.

        :param pet_id: Required.
        :type pet_id: int
        :param properties: Required.
        :type properties: IO[bytes]
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: Pet. The Pet is compatible with MutableMapping
        :rtype: ~petstore.models.Pet
        :raises ~corehttp.exceptions.HttpResponseError:
        """

    async def update(
        self, pet_id: int, properties: Union[_models.PetUpdate, JSON, IO[bytes]], **kwargs: Any
    ) -> _models.Pet:
        """Updates an existing instance of the resource.

        :param pet_id: Required.
        :type pet_id: int
        :param properties: Is one of the following types: PetUpdate, JSON, IO[bytes] Required.
        :type properties: ~petstore.models.PetUpdate or JSON or IO[bytes]
        :return: Pet. The Pet is compatible with MutableMapping
        :rtype: ~petstore.models.Pet
        :raises ~corehttp.exceptions.HttpResponseError:
        """
        error_map: MutableMapping = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = kwargs.pop("params", {}) or {}

        content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
        cls: ClsType[_models.Pet] = kwargs.pop("cls", None)

        content_type = content_type or "application/json"
        _content = None
        if isinstance(properties, (IOBase, bytes)):
            _content = properties
        else:
            _content = json.dumps(properties, cls=SdkJSONEncoder, exclude_readonly=True)  # type: ignore

        _request = build_pets_update_request(
            pet_id=pet_id,
            content_type=content_type,
            content=_content,
            headers=_headers,
            params=_params,
        )
        path_format_arguments = {
            "endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, "str", skip_quote=True),
        }
        _request.url = self._client.format_url(_request.url, **path_format_arguments)

        _stream = kwargs.pop("stream", False)
        pipeline_response: PipelineResponse = await self._client.pipeline.run(_request, stream=_stream, **kwargs)

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            if _stream:
                try:
                    await response.read()  # Load the body in memory and close the socket
                except (StreamConsumedError, StreamClosedError):
                    pass
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = _deserialize(_models.PetStoreError, response.json())
            raise HttpResponseError(response=response, model=error)

        if _stream:
            deserialized = response.iter_bytes()
        else:
            deserialized = _deserialize(_models.Pet, response.json())

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore

    async def delete(self, pet_id: int, **kwargs: Any) -> None:
        """Deletes an existing instance of the resource.

        :param pet_id: Required.
        :type pet_id: int
        :return: None
        :rtype: None
        :raises ~corehttp.exceptions.HttpResponseError:
        """
        error_map: MutableMapping = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = kwargs.pop("params", {}) or {}

        cls: ClsType[None] = kwargs.pop("cls", None)

        _request = build_pets_delete_request(
            pet_id=pet_id,
            headers=_headers,
            params=_params,
        )
        path_format_arguments = {
            "endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, "str", skip_quote=True),
        }
        _request.url = self._client.format_url(_request.url, **path_format_arguments)

        _stream = False
        pipeline_response: PipelineResponse = await self._client.pipeline.run(_request, stream=_stream, **kwargs)

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = _deserialize(_models.PetStoreError, response.json())
            raise HttpResponseError(response=response, model=error)

        if cls:
            return cls(pipeline_response, None, {})  # type: ignore

    @overload
    async def create(
        self, resource: _models.PetCreate, *, content_type: str = "application/json", **kwargs: Any
    ) -> _models.Pet:
        """Creates a new instance of the resource.

        :param resource: Required.
        :type resource: ~petstore.models.PetCreate
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: Pet. The Pet is compatible with MutableMapping
        :rtype: ~petstore.models.Pet
        :raises ~corehttp.exceptions.HttpResponseError:
        """

    @overload
    async def create(self, resource: JSON, *, content_type: str = "application/json", **kwargs: Any) -> _models.Pet:
        """Creates a new instance of the resource.

        :param resource: Required.
        :type resource: JSON
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: Pet. The Pet is compatible with MutableMapping
        :rtype: ~petstore.models.Pet
        :raises ~corehttp.exceptions.HttpResponseError:
        """

    @overload
    async def create(
        self, resource: IO[bytes], *, content_type: str = "application/json", **kwargs: Any
    ) -> _models.Pet:
        """Creates a new instance of the resource.

        :param resource: Required.
        :type resource: IO[bytes]
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: Pet. The Pet is compatible with MutableMapping
        :rtype: ~petstore.models.Pet
        :raises ~corehttp.exceptions.HttpResponseError:
        """

    async def create(self, resource: Union[_models.PetCreate, JSON, IO[bytes]], **kwargs: Any) -> _models.Pet:
        """Creates a new instance of the resource.

        :param resource: Is one of the following types: PetCreate, JSON, IO[bytes] Required.
        :type resource: ~petstore.models.PetCreate or JSON or IO[bytes]
        :return: Pet. The Pet is compatible with MutableMapping
        :rtype: ~petstore.models.Pet
        :raises ~corehttp.exceptions.HttpResponseError:
        """
        error_map: MutableMapping = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = kwargs.pop("params", {}) or {}

        content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
        cls: ClsType[_models.Pet] = kwargs.pop("cls", None)

        content_type = content_type or "application/json"
        _content = None
        if isinstance(resource, (IOBase, bytes)):
            _content = resource
        else:
            _content = json.dumps(resource, cls=SdkJSONEncoder, exclude_readonly=True)  # type: ignore

        _request = build_pets_create_request(
            content_type=content_type,
            content=_content,
            headers=_headers,
            params=_params,
        )
        path_format_arguments = {
            "endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, "str", skip_quote=True),
        }
        _request.url = self._client.format_url(_request.url, **path_format_arguments)

        _stream = kwargs.pop("stream", False)
        pipeline_response: PipelineResponse = await self._client.pipeline.run(_request, stream=_stream, **kwargs)

        response = pipeline_response.http_response

        if response.status_code not in [200, 201]:
            if _stream:
                try:
                    await response.read()  # Load the body in memory and close the socket
                except (StreamConsumedError, StreamClosedError):
                    pass
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = _deserialize(_models.PetStoreError, response.json())
            raise HttpResponseError(response=response, model=error)

        if _stream:
            deserialized = response.iter_bytes()
        else:
            deserialized = _deserialize(_models.Pet, response.json())

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore

    async def list(self, **kwargs: Any) -> _models.PetCollectionWithNextLink:
        """Lists all instances of the resource.

        :return: PetCollectionWithNextLink. The PetCollectionWithNextLink is compatible with
         MutableMapping
        :rtype: ~petstore.models.PetCollectionWithNextLink
        :raises ~corehttp.exceptions.HttpResponseError:
        """
        error_map: MutableMapping = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = kwargs.pop("params", {}) or {}

        cls: ClsType[_models.PetCollectionWithNextLink] = kwargs.pop("cls", None)

        _request = build_pets_list_request(
            headers=_headers,
            params=_params,
        )
        path_format_arguments = {
            "endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, "str", skip_quote=True),
        }
        _request.url = self._client.format_url(_request.url, **path_format_arguments)

        _stream = kwargs.pop("stream", False)
        pipeline_response: PipelineResponse = await self._client.pipeline.run(_request, stream=_stream, **kwargs)

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            if _stream:
                try:
                    await response.read()  # Load the body in memory and close the socket
                except (StreamConsumedError, StreamClosedError):
                    pass
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = _deserialize(_models.PetStoreError, response.json())
            raise HttpResponseError(response=response, model=error)

        if _stream:
            deserialized = response.iter_bytes()
        else:
            deserialized = _deserialize(_models.PetCollectionWithNextLink, response.json())

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore


class PetCheckupsOperations:
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through
        :class:`~petstore.aio.PetStoreClient`'s
        :attr:`pet_checkups` attribute.
    """

    def __init__(self, *args, **kwargs) -> None:
        input_args = list(args)
        self._client = input_args.pop(0) if input_args else kwargs.pop("client")
        self._config = input_args.pop(0) if input_args else kwargs.pop("config")
        self._serialize = input_args.pop(0) if input_args else kwargs.pop("serializer")
        self._deserialize = input_args.pop(0) if input_args else kwargs.pop("deserializer")

    @overload
    async def create_or_update(
        self,
        pet_id: int,
        checkup_id: int,
        resource: _models.CheckupUpdate,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.Checkup:
        """Creates or update an instance of the extension resource.

        :param pet_id: Required.
        :type pet_id: int
        :param checkup_id: Required.
        :type checkup_id: int
        :param resource: Required.
        :type resource: ~petstore.models.CheckupUpdate
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: Checkup. The Checkup is compatible with MutableMapping
        :rtype: ~petstore.models.Checkup
        :raises ~corehttp.exceptions.HttpResponseError:
        """

    @overload
    async def create_or_update(
        self, pet_id: int, checkup_id: int, resource: JSON, *, content_type: str = "application/json", **kwargs: Any
    ) -> _models.Checkup:
        """Creates or update an instance of the extension resource.

        :param pet_id: Required.
        :type pet_id: int
        :param checkup_id: Required.
        :type checkup_id: int
        :param resource: Required.
        :type resource: JSON
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: Checkup. The Checkup is compatible with MutableMapping
        :rtype: ~petstore.models.Checkup
        :raises ~corehttp.exceptions.HttpResponseError:
        """

    @overload
    async def create_or_update(
        self,
        pet_id: int,
        checkup_id: int,
        resource: IO[bytes],
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.Checkup:
        """Creates or update an instance of the extension resource.

        :param pet_id: Required.
        :type pet_id: int
        :param checkup_id: Required.
        :type checkup_id: int
        :param resource: Required.
        :type resource: IO[bytes]
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: Checkup. The Checkup is compatible with MutableMapping
        :rtype: ~petstore.models.Checkup
        :raises ~corehttp.exceptions.HttpResponseError:
        """

    async def create_or_update(
        self, pet_id: int, checkup_id: int, resource: Union[_models.CheckupUpdate, JSON, IO[bytes]], **kwargs: Any
    ) -> _models.Checkup:
        """Creates or update an instance of the extension resource.

        :param pet_id: Required.
        :type pet_id: int
        :param checkup_id: Required.
        :type checkup_id: int
        :param resource: Is one of the following types: CheckupUpdate, JSON, IO[bytes] Required.
        :type resource: ~petstore.models.CheckupUpdate or JSON or IO[bytes]
        :return: Checkup. The Checkup is compatible with MutableMapping
        :rtype: ~petstore.models.Checkup
        :raises ~corehttp.exceptions.HttpResponseError:
        """
        error_map: MutableMapping = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = kwargs.pop("params", {}) or {}

        content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
        cls: ClsType[_models.Checkup] = kwargs.pop("cls", None)

        content_type = content_type or "application/json"
        _content = None
        if isinstance(resource, (IOBase, bytes)):
            _content = resource
        else:
            _content = json.dumps(resource, cls=SdkJSONEncoder, exclude_readonly=True)  # type: ignore

        _request = build_pet_checkups_create_or_update_request(
            pet_id=pet_id,
            checkup_id=checkup_id,
            content_type=content_type,
            content=_content,
            headers=_headers,
            params=_params,
        )
        path_format_arguments = {
            "endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, "str", skip_quote=True),
        }
        _request.url = self._client.format_url(_request.url, **path_format_arguments)

        _stream = kwargs.pop("stream", False)
        pipeline_response: PipelineResponse = await self._client.pipeline.run(_request, stream=_stream, **kwargs)

        response = pipeline_response.http_response

        if response.status_code not in [200, 201]:
            if _stream:
                try:
                    await response.read()  # Load the body in memory and close the socket
                except (StreamConsumedError, StreamClosedError):
                    pass
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = _deserialize(_models.PetStoreError, response.json())
            raise HttpResponseError(response=response, model=error)

        if _stream:
            deserialized = response.iter_bytes()
        else:
            deserialized = _deserialize(_models.Checkup, response.json())

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore

    async def list(self, pet_id: int, **kwargs: Any) -> _models.CheckupCollectionWithNextLink:
        """Lists all instances of the extension resource.

        :param pet_id: Required.
        :type pet_id: int
        :return: CheckupCollectionWithNextLink. The CheckupCollectionWithNextLink is compatible with
         MutableMapping
        :rtype: ~petstore.models.CheckupCollectionWithNextLink
        :raises ~corehttp.exceptions.HttpResponseError:
        """
        error_map: MutableMapping = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = kwargs.pop("params", {}) or {}

        cls: ClsType[_models.CheckupCollectionWithNextLink] = kwargs.pop("cls", None)

        _request = build_pet_checkups_list_request(
            pet_id=pet_id,
            headers=_headers,
            params=_params,
        )
        path_format_arguments = {
            "endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, "str", skip_quote=True),
        }
        _request.url = self._client.format_url(_request.url, **path_format_arguments)

        _stream = kwargs.pop("stream", False)
        pipeline_response: PipelineResponse = await self._client.pipeline.run(_request, stream=_stream, **kwargs)

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            if _stream:
                try:
                    await response.read()  # Load the body in memory and close the socket
                except (StreamConsumedError, StreamClosedError):
                    pass
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = _deserialize(_models.PetStoreError, response.json())
            raise HttpResponseError(response=response, model=error)

        if _stream:
            deserialized = response.iter_bytes()
        else:
            deserialized = _deserialize(_models.CheckupCollectionWithNextLink, response.json())

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore


class PetInsuranceOperations:
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through
        :class:`~petstore.aio.PetStoreClient`'s
        :attr:`pet_insurance` attribute.
    """

    def __init__(self, *args, **kwargs) -> None:
        input_args = list(args)
        self._client = input_args.pop(0) if input_args else kwargs.pop("client")
        self._config = input_args.pop(0) if input_args else kwargs.pop("config")
        self._serialize = input_args.pop(0) if input_args else kwargs.pop("serializer")
        self._deserialize = input_args.pop(0) if input_args else kwargs.pop("deserializer")

    async def get(self, pet_id: int, **kwargs: Any) -> _models.Insurance:
        """Gets the singleton resource.

        :param pet_id: Required.
        :type pet_id: int
        :return: Insurance. The Insurance is compatible with MutableMapping
        :rtype: ~petstore.models.Insurance
        :raises ~corehttp.exceptions.HttpResponseError:
        """
        error_map: MutableMapping = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = kwargs.pop("params", {}) or {}

        cls: ClsType[_models.Insurance] = kwargs.pop("cls", None)

        _request = build_pet_insurance_get_request(
            pet_id=pet_id,
            headers=_headers,
            params=_params,
        )
        path_format_arguments = {
            "endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, "str", skip_quote=True),
        }
        _request.url = self._client.format_url(_request.url, **path_format_arguments)

        _stream = kwargs.pop("stream", False)
        pipeline_response: PipelineResponse = await self._client.pipeline.run(_request, stream=_stream, **kwargs)

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            if _stream:
                try:
                    await response.read()  # Load the body in memory and close the socket
                except (StreamConsumedError, StreamClosedError):
                    pass
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = _deserialize(_models.PetStoreError, response.json())
            raise HttpResponseError(response=response, model=error)

        if _stream:
            deserialized = response.iter_bytes()
        else:
            deserialized = _deserialize(_models.Insurance, response.json())

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore

    @overload
    async def update(
        self, pet_id: int, properties: _models.InsuranceUpdate, *, content_type: str = "application/json", **kwargs: Any
    ) -> _models.Insurance:
        """Updates the singleton resource.

        :param pet_id: Required.
        :type pet_id: int
        :param properties: Required.
        :type properties: ~petstore.models.InsuranceUpdate
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: Insurance. The Insurance is compatible with MutableMapping
        :rtype: ~petstore.models.Insurance
        :raises ~corehttp.exceptions.HttpResponseError:
        """

    @overload
    async def update(
        self, pet_id: int, properties: JSON, *, content_type: str = "application/json", **kwargs: Any
    ) -> _models.Insurance:
        """Updates the singleton resource.

        :param pet_id: Required.
        :type pet_id: int
        :param properties: Required.
        :type properties: JSON
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: Insurance. The Insurance is compatible with MutableMapping
        :rtype: ~petstore.models.Insurance
        :raises ~corehttp.exceptions.HttpResponseError:
        """

    @overload
    async def update(
        self, pet_id: int, properties: IO[bytes], *, content_type: str = "application/json", **kwargs: Any
    ) -> _models.Insurance:
        """Updates the singleton resource.

        :param pet_id: Required.
        :type pet_id: int
        :param properties: Required.
        :type properties: IO[bytes]
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: Insurance. The Insurance is compatible with MutableMapping
        :rtype: ~petstore.models.Insurance
        :raises ~corehttp.exceptions.HttpResponseError:
        """

    async def update(
        self, pet_id: int, properties: Union[_models.InsuranceUpdate, JSON, IO[bytes]], **kwargs: Any
    ) -> _models.Insurance:
        """Updates the singleton resource.

        :param pet_id: Required.
        :type pet_id: int
        :param properties: Is one of the following types: InsuranceUpdate, JSON, IO[bytes] Required.
        :type properties: ~petstore.models.InsuranceUpdate or JSON or IO[bytes]
        :return: Insurance. The Insurance is compatible with MutableMapping
        :rtype: ~petstore.models.Insurance
        :raises ~corehttp.exceptions.HttpResponseError:
        """
        error_map: MutableMapping = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = kwargs.pop("params", {}) or {}

        content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
        cls: ClsType[_models.Insurance] = kwargs.pop("cls", None)

        content_type = content_type or "application/json"
        _content = None
        if isinstance(properties, (IOBase, bytes)):
            _content = properties
        else:
            _content = json.dumps(properties, cls=SdkJSONEncoder, exclude_readonly=True)  # type: ignore

        _request = build_pet_insurance_update_request(
            pet_id=pet_id,
            content_type=content_type,
            content=_content,
            headers=_headers,
            params=_params,
        )
        path_format_arguments = {
            "endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, "str", skip_quote=True),
        }
        _request.url = self._client.format_url(_request.url, **path_format_arguments)

        _stream = kwargs.pop("stream", False)
        pipeline_response: PipelineResponse = await self._client.pipeline.run(_request, stream=_stream, **kwargs)

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            if _stream:
                try:
                    await response.read()  # Load the body in memory and close the socket
                except (StreamConsumedError, StreamClosedError):
                    pass
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = _deserialize(_models.PetStoreError, response.json())
            raise HttpResponseError(response=response, model=error)

        if _stream:
            deserialized = response.iter_bytes()
        else:
            deserialized = _deserialize(_models.Insurance, response.json())

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore


class ToysOperations:
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through
        :class:`~petstore.aio.PetStoreClient`'s
        :attr:`toys` attribute.
    """

    def __init__(self, *args, **kwargs) -> None:
        input_args = list(args)
        self._client = input_args.pop(0) if input_args else kwargs.pop("client")
        self._config = input_args.pop(0) if input_args else kwargs.pop("config")
        self._serialize = input_args.pop(0) if input_args else kwargs.pop("serializer")
        self._deserialize = input_args.pop(0) if input_args else kwargs.pop("deserializer")

    async def get(self, pet_id: int, toy_id: int, **kwargs: Any) -> _models.Toy:
        """Gets an instance of the resource.

        :param pet_id: Required.
        :type pet_id: int
        :param toy_id: Required.
        :type toy_id: int
        :return: Toy. The Toy is compatible with MutableMapping
        :rtype: ~petstore.models.Toy
        :raises ~corehttp.exceptions.HttpResponseError:
        """
        error_map: MutableMapping = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = kwargs.pop("params", {}) or {}

        cls: ClsType[_models.Toy] = kwargs.pop("cls", None)

        _request = build_toys_get_request(
            pet_id=pet_id,
            toy_id=toy_id,
            headers=_headers,
            params=_params,
        )
        path_format_arguments = {
            "endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, "str", skip_quote=True),
        }
        _request.url = self._client.format_url(_request.url, **path_format_arguments)

        _stream = kwargs.pop("stream", False)
        pipeline_response: PipelineResponse = await self._client.pipeline.run(_request, stream=_stream, **kwargs)

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            if _stream:
                try:
                    await response.read()  # Load the body in memory and close the socket
                except (StreamConsumedError, StreamClosedError):
                    pass
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = _deserialize(_models.PetStoreError, response.json())
            raise HttpResponseError(response=response, model=error)

        if _stream:
            deserialized = response.iter_bytes()
        else:
            deserialized = _deserialize(_models.Toy, response.json())

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore

    async def list(self, pet_id: int, *, name_filter: str, **kwargs: Any) -> _models.ToyCollectionWithNextLink:
        """list.

        :param pet_id: Required.
        :type pet_id: int
        :keyword name_filter: Required.
        :paramtype name_filter: str
        :return: ToyCollectionWithNextLink. The ToyCollectionWithNextLink is compatible with
         MutableMapping
        :rtype: ~petstore.models.ToyCollectionWithNextLink
        :raises ~corehttp.exceptions.HttpResponseError:
        """
        error_map: MutableMapping = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = kwargs.pop("params", {}) or {}

        cls: ClsType[_models.ToyCollectionWithNextLink] = kwargs.pop("cls", None)

        _request = build_toys_list_request(
            pet_id=pet_id,
            name_filter=name_filter,
            headers=_headers,
            params=_params,
        )
        path_format_arguments = {
            "endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, "str", skip_quote=True),
        }
        _request.url = self._client.format_url(_request.url, **path_format_arguments)

        _stream = kwargs.pop("stream", False)
        pipeline_response: PipelineResponse = await self._client.pipeline.run(_request, stream=_stream, **kwargs)

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            if _stream:
                try:
                    await response.read()  # Load the body in memory and close the socket
                except (StreamConsumedError, StreamClosedError):
                    pass
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = _deserialize(_models.PetStoreError, response.json())
            raise HttpResponseError(response=response, model=error)

        if _stream:
            deserialized = response.iter_bytes()
        else:
            deserialized = _deserialize(_models.ToyCollectionWithNextLink, response.json())

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore


class ToyInsuranceOperations:
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through
        :class:`~petstore.aio.PetStoreClient`'s
        :attr:`toy_insurance` attribute.
    """

    def __init__(self, *args, **kwargs) -> None:
        input_args = list(args)
        self._client = input_args.pop(0) if input_args else kwargs.pop("client")
        self._config = input_args.pop(0) if input_args else kwargs.pop("config")
        self._serialize = input_args.pop(0) if input_args else kwargs.pop("serializer")
        self._deserialize = input_args.pop(0) if input_args else kwargs.pop("deserializer")

    async def get(self, pet_id: int, toy_id: int, **kwargs: Any) -> _models.Insurance:
        """Gets the singleton resource.

        :param pet_id: Required.
        :type pet_id: int
        :param toy_id: Required.
        :type toy_id: int
        :return: Insurance. The Insurance is compatible with MutableMapping
        :rtype: ~petstore.models.Insurance
        :raises ~corehttp.exceptions.HttpResponseError:
        """
        error_map: MutableMapping = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = kwargs.pop("params", {}) or {}

        cls: ClsType[_models.Insurance] = kwargs.pop("cls", None)

        _request = build_toy_insurance_get_request(
            pet_id=pet_id,
            toy_id=toy_id,
            headers=_headers,
            params=_params,
        )
        path_format_arguments = {
            "endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, "str", skip_quote=True),
        }
        _request.url = self._client.format_url(_request.url, **path_format_arguments)

        _stream = kwargs.pop("stream", False)
        pipeline_response: PipelineResponse = await self._client.pipeline.run(_request, stream=_stream, **kwargs)

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            if _stream:
                try:
                    await response.read()  # Load the body in memory and close the socket
                except (StreamConsumedError, StreamClosedError):
                    pass
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = _deserialize(_models.PetStoreError, response.json())
            raise HttpResponseError(response=response, model=error)

        if _stream:
            deserialized = response.iter_bytes()
        else:
            deserialized = _deserialize(_models.Insurance, response.json())

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore

    @overload
    async def update(
        self,
        pet_id: int,
        toy_id: int,
        properties: _models.InsuranceUpdate,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.Insurance:
        """Updates the singleton resource.

        :param pet_id: Required.
        :type pet_id: int
        :param toy_id: Required.
        :type toy_id: int
        :param properties: Required.
        :type properties: ~petstore.models.InsuranceUpdate
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: Insurance. The Insurance is compatible with MutableMapping
        :rtype: ~petstore.models.Insurance
        :raises ~corehttp.exceptions.HttpResponseError:
        """

    @overload
    async def update(
        self, pet_id: int, toy_id: int, properties: JSON, *, content_type: str = "application/json", **kwargs: Any
    ) -> _models.Insurance:
        """Updates the singleton resource.

        :param pet_id: Required.
        :type pet_id: int
        :param toy_id: Required.
        :type toy_id: int
        :param properties: Required.
        :type properties: JSON
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: Insurance. The Insurance is compatible with MutableMapping
        :rtype: ~petstore.models.Insurance
        :raises ~corehttp.exceptions.HttpResponseError:
        """

    @overload
    async def update(
        self, pet_id: int, toy_id: int, properties: IO[bytes], *, content_type: str = "application/json", **kwargs: Any
    ) -> _models.Insurance:
        """Updates the singleton resource.

        :param pet_id: Required.
        :type pet_id: int
        :param toy_id: Required.
        :type toy_id: int
        :param properties: Required.
        :type properties: IO[bytes]
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: Insurance. The Insurance is compatible with MutableMapping
        :rtype: ~petstore.models.Insurance
        :raises ~corehttp.exceptions.HttpResponseError:
        """

    async def update(
        self, pet_id: int, toy_id: int, properties: Union[_models.InsuranceUpdate, JSON, IO[bytes]], **kwargs: Any
    ) -> _models.Insurance:
        """Updates the singleton resource.

        :param pet_id: Required.
        :type pet_id: int
        :param toy_id: Required.
        :type toy_id: int
        :param properties: Is one of the following types: InsuranceUpdate, JSON, IO[bytes] Required.
        :type properties: ~petstore.models.InsuranceUpdate or JSON or IO[bytes]
        :return: Insurance. The Insurance is compatible with MutableMapping
        :rtype: ~petstore.models.Insurance
        :raises ~corehttp.exceptions.HttpResponseError:
        """
        error_map: MutableMapping = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = kwargs.pop("params", {}) or {}

        content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
        cls: ClsType[_models.Insurance] = kwargs.pop("cls", None)

        content_type = content_type or "application/json"
        _content = None
        if isinstance(properties, (IOBase, bytes)):
            _content = properties
        else:
            _content = json.dumps(properties, cls=SdkJSONEncoder, exclude_readonly=True)  # type: ignore

        _request = build_toy_insurance_update_request(
            pet_id=pet_id,
            toy_id=toy_id,
            content_type=content_type,
            content=_content,
            headers=_headers,
            params=_params,
        )
        path_format_arguments = {
            "endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, "str", skip_quote=True),
        }
        _request.url = self._client.format_url(_request.url, **path_format_arguments)

        _stream = kwargs.pop("stream", False)
        pipeline_response: PipelineResponse = await self._client.pipeline.run(_request, stream=_stream, **kwargs)

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            if _stream:
                try:
                    await response.read()  # Load the body in memory and close the socket
                except (StreamConsumedError, StreamClosedError):
                    pass
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = _deserialize(_models.PetStoreError, response.json())
            raise HttpResponseError(response=response, model=error)

        if _stream:
            deserialized = response.iter_bytes()
        else:
            deserialized = _deserialize(_models.Insurance, response.json())

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore


class CheckupsOperations:
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through
        :class:`~petstore.aio.PetStoreClient`'s
        :attr:`checkups` attribute.
    """

    def __init__(self, *args, **kwargs) -> None:
        input_args = list(args)
        self._client = input_args.pop(0) if input_args else kwargs.pop("client")
        self._config = input_args.pop(0) if input_args else kwargs.pop("config")
        self._serialize = input_args.pop(0) if input_args else kwargs.pop("serializer")
        self._deserialize = input_args.pop(0) if input_args else kwargs.pop("deserializer")

    @overload
    async def create_or_update(
        self, checkup_id: int, resource: _models.CheckupUpdate, *, content_type: str = "application/json", **kwargs: Any
    ) -> _models.Checkup:
        """Creates or update an instance of the resource.

        :param checkup_id: Required.
        :type checkup_id: int
        :param resource: Required.
        :type resource: ~petstore.models.CheckupUpdate
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: Checkup. The Checkup is compatible with MutableMapping
        :rtype: ~petstore.models.Checkup
        :raises ~corehttp.exceptions.HttpResponseError:
        """

    @overload
    async def create_or_update(
        self, checkup_id: int, resource: JSON, *, content_type: str = "application/json", **kwargs: Any
    ) -> _models.Checkup:
        """Creates or update an instance of the resource.

        :param checkup_id: Required.
        :type checkup_id: int
        :param resource: Required.
        :type resource: JSON
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: Checkup. The Checkup is compatible with MutableMapping
        :rtype: ~petstore.models.Checkup
        :raises ~corehttp.exceptions.HttpResponseError:
        """

    @overload
    async def create_or_update(
        self, checkup_id: int, resource: IO[bytes], *, content_type: str = "application/json", **kwargs: Any
    ) -> _models.Checkup:
        """Creates or update an instance of the resource.

        :param checkup_id: Required.
        :type checkup_id: int
        :param resource: Required.
        :type resource: IO[bytes]
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: Checkup. The Checkup is compatible with MutableMapping
        :rtype: ~petstore.models.Checkup
        :raises ~corehttp.exceptions.HttpResponseError:
        """

    async def create_or_update(
        self, checkup_id: int, resource: Union[_models.CheckupUpdate, JSON, IO[bytes]], **kwargs: Any
    ) -> _models.Checkup:
        """Creates or update an instance of the resource.

        :param checkup_id: Required.
        :type checkup_id: int
        :param resource: Is one of the following types: CheckupUpdate, JSON, IO[bytes] Required.
        :type resource: ~petstore.models.CheckupUpdate or JSON or IO[bytes]
        :return: Checkup. The Checkup is compatible with MutableMapping
        :rtype: ~petstore.models.Checkup
        :raises ~corehttp.exceptions.HttpResponseError:
        """
        error_map: MutableMapping = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = kwargs.pop("params", {}) or {}

        content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
        cls: ClsType[_models.Checkup] = kwargs.pop("cls", None)

        content_type = content_type or "application/json"
        _content = None
        if isinstance(resource, (IOBase, bytes)):
            _content = resource
        else:
            _content = json.dumps(resource, cls=SdkJSONEncoder, exclude_readonly=True)  # type: ignore

        _request = build_checkups_create_or_update_request(
            checkup_id=checkup_id,
            content_type=content_type,
            content=_content,
            headers=_headers,
            params=_params,
        )
        path_format_arguments = {
            "endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, "str", skip_quote=True),
        }
        _request.url = self._client.format_url(_request.url, **path_format_arguments)

        _stream = kwargs.pop("stream", False)
        pipeline_response: PipelineResponse = await self._client.pipeline.run(_request, stream=_stream, **kwargs)

        response = pipeline_response.http_response

        if response.status_code not in [200, 201]:
            if _stream:
                try:
                    await response.read()  # Load the body in memory and close the socket
                except (StreamConsumedError, StreamClosedError):
                    pass
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = _deserialize(_models.PetStoreError, response.json())
            raise HttpResponseError(response=response, model=error)

        if _stream:
            deserialized = response.iter_bytes()
        else:
            deserialized = _deserialize(_models.Checkup, response.json())

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore

    async def list(self, **kwargs: Any) -> _models.CheckupCollectionWithNextLink:
        """Lists all instances of the resource.

        :return: CheckupCollectionWithNextLink. The CheckupCollectionWithNextLink is compatible with
         MutableMapping
        :rtype: ~petstore.models.CheckupCollectionWithNextLink
        :raises ~corehttp.exceptions.HttpResponseError:
        """
        error_map: MutableMapping = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = kwargs.pop("params", {}) or {}

        cls: ClsType[_models.CheckupCollectionWithNextLink] = kwargs.pop("cls", None)

        _request = build_checkups_list_request(
            headers=_headers,
            params=_params,
        )
        path_format_arguments = {
            "endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, "str", skip_quote=True),
        }
        _request.url = self._client.format_url(_request.url, **path_format_arguments)

        _stream = kwargs.pop("stream", False)
        pipeline_response: PipelineResponse = await self._client.pipeline.run(_request, stream=_stream, **kwargs)

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            if _stream:
                try:
                    await response.read()  # Load the body in memory and close the socket
                except (StreamConsumedError, StreamClosedError):
                    pass
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = _deserialize(_models.PetStoreError, response.json())
            raise HttpResponseError(response=response, model=error)

        if _stream:
            deserialized = response.iter_bytes()
        else:
            deserialized = _deserialize(_models.CheckupCollectionWithNextLink, response.json())

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore


class OwnersOperations:
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through
        :class:`~petstore.aio.PetStoreClient`'s
        :attr:`owners` attribute.
    """

    def __init__(self, *args, **kwargs) -> None:
        input_args = list(args)
        self._client = input_args.pop(0) if input_args else kwargs.pop("client")
        self._config = input_args.pop(0) if input_args else kwargs.pop("config")
        self._serialize = input_args.pop(0) if input_args else kwargs.pop("serializer")
        self._deserialize = input_args.pop(0) if input_args else kwargs.pop("deserializer")

    async def get(self, owner_id: int, **kwargs: Any) -> _models.Owner:
        """Gets an instance of the resource.

        :param owner_id: Required.
        :type owner_id: int
        :return: Owner. The Owner is compatible with MutableMapping
        :rtype: ~petstore.models.Owner
        :raises ~corehttp.exceptions.HttpResponseError:
        """
        error_map: MutableMapping = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = kwargs.pop("params", {}) or {}

        cls: ClsType[_models.Owner] = kwargs.pop("cls", None)

        _request = build_owners_get_request(
            owner_id=owner_id,
            headers=_headers,
            params=_params,
        )
        path_format_arguments = {
            "endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, "str", skip_quote=True),
        }
        _request.url = self._client.format_url(_request.url, **path_format_arguments)

        _stream = kwargs.pop("stream", False)
        pipeline_response: PipelineResponse = await self._client.pipeline.run(_request, stream=_stream, **kwargs)

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            if _stream:
                try:
                    await response.read()  # Load the body in memory and close the socket
                except (StreamConsumedError, StreamClosedError):
                    pass
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = _deserialize(_models.PetStoreError, response.json())
            raise HttpResponseError(response=response, model=error)

        if _stream:
            deserialized = response.iter_bytes()
        else:
            deserialized = _deserialize(_models.Owner, response.json())

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore

    @overload
    async def update(
        self, owner_id: int, properties: _models.OwnerUpdate, *, content_type: str = "application/json", **kwargs: Any
    ) -> _models.Owner:
        """Updates an existing instance of the resource.

        :param owner_id: Required.
        :type owner_id: int
        :param properties: Required.
        :type properties: ~petstore.models.OwnerUpdate
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: Owner. The Owner is compatible with MutableMapping
        :rtype: ~petstore.models.Owner
        :raises ~corehttp.exceptions.HttpResponseError:
        """

    @overload
    async def update(
        self, owner_id: int, properties: JSON, *, content_type: str = "application/json", **kwargs: Any
    ) -> _models.Owner:
        """Updates an existing instance of the resource.

        :param owner_id: Required.
        :type owner_id: int
        :param properties: Required.
        :type properties: JSON
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: Owner. The Owner is compatible with MutableMapping
        :rtype: ~petstore.models.Owner
        :raises ~corehttp.exceptions.HttpResponseError:
        """

    @overload
    async def update(
        self, owner_id: int, properties: IO[bytes], *, content_type: str = "application/json", **kwargs: Any
    ) -> _models.Owner:
        """Updates an existing instance of the resource.

        :param owner_id: Required.
        :type owner_id: int
        :param properties: Required.
        :type properties: IO[bytes]
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: Owner. The Owner is compatible with MutableMapping
        :rtype: ~petstore.models.Owner
        :raises ~corehttp.exceptions.HttpResponseError:
        """

    async def update(
        self, owner_id: int, properties: Union[_models.OwnerUpdate, JSON, IO[bytes]], **kwargs: Any
    ) -> _models.Owner:
        """Updates an existing instance of the resource.

        :param owner_id: Required.
        :type owner_id: int
        :param properties: Is one of the following types: OwnerUpdate, JSON, IO[bytes] Required.
        :type properties: ~petstore.models.OwnerUpdate or JSON or IO[bytes]
        :return: Owner. The Owner is compatible with MutableMapping
        :rtype: ~petstore.models.Owner
        :raises ~corehttp.exceptions.HttpResponseError:
        """
        error_map: MutableMapping = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = kwargs.pop("params", {}) or {}

        content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
        cls: ClsType[_models.Owner] = kwargs.pop("cls", None)

        content_type = content_type or "application/json"
        _content = None
        if isinstance(properties, (IOBase, bytes)):
            _content = properties
        else:
            _content = json.dumps(properties, cls=SdkJSONEncoder, exclude_readonly=True)  # type: ignore

        _request = build_owners_update_request(
            owner_id=owner_id,
            content_type=content_type,
            content=_content,
            headers=_headers,
            params=_params,
        )
        path_format_arguments = {
            "endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, "str", skip_quote=True),
        }
        _request.url = self._client.format_url(_request.url, **path_format_arguments)

        _stream = kwargs.pop("stream", False)
        pipeline_response: PipelineResponse = await self._client.pipeline.run(_request, stream=_stream, **kwargs)

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            if _stream:
                try:
                    await response.read()  # Load the body in memory and close the socket
                except (StreamConsumedError, StreamClosedError):
                    pass
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = _deserialize(_models.PetStoreError, response.json())
            raise HttpResponseError(response=response, model=error)

        if _stream:
            deserialized = response.iter_bytes()
        else:
            deserialized = _deserialize(_models.Owner, response.json())

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore

    async def delete(self, owner_id: int, **kwargs: Any) -> None:
        """Deletes an existing instance of the resource.

        :param owner_id: Required.
        :type owner_id: int
        :return: None
        :rtype: None
        :raises ~corehttp.exceptions.HttpResponseError:
        """
        error_map: MutableMapping = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = kwargs.pop("params", {}) or {}

        cls: ClsType[None] = kwargs.pop("cls", None)

        _request = build_owners_delete_request(
            owner_id=owner_id,
            headers=_headers,
            params=_params,
        )
        path_format_arguments = {
            "endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, "str", skip_quote=True),
        }
        _request.url = self._client.format_url(_request.url, **path_format_arguments)

        _stream = False
        pipeline_response: PipelineResponse = await self._client.pipeline.run(_request, stream=_stream, **kwargs)

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = _deserialize(_models.PetStoreError, response.json())
            raise HttpResponseError(response=response, model=error)

        if cls:
            return cls(pipeline_response, None, {})  # type: ignore

    @overload
    async def create(
        self, resource: _models.OwnerCreate, *, content_type: str = "application/json", **kwargs: Any
    ) -> _models.Owner:
        """Creates a new instance of the resource.

        :param resource: Required.
        :type resource: ~petstore.models.OwnerCreate
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: Owner. The Owner is compatible with MutableMapping
        :rtype: ~petstore.models.Owner
        :raises ~corehttp.exceptions.HttpResponseError:
        """

    @overload
    async def create(self, resource: JSON, *, content_type: str = "application/json", **kwargs: Any) -> _models.Owner:
        """Creates a new instance of the resource.

        :param resource: Required.
        :type resource: JSON
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: Owner. The Owner is compatible with MutableMapping
        :rtype: ~petstore.models.Owner
        :raises ~corehttp.exceptions.HttpResponseError:
        """

    @overload
    async def create(
        self, resource: IO[bytes], *, content_type: str = "application/json", **kwargs: Any
    ) -> _models.Owner:
        """Creates a new instance of the resource.

        :param resource: Required.
        :type resource: IO[bytes]
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: Owner. The Owner is compatible with MutableMapping
        :rtype: ~petstore.models.Owner
        :raises ~corehttp.exceptions.HttpResponseError:
        """

    async def create(self, resource: Union[_models.OwnerCreate, JSON, IO[bytes]], **kwargs: Any) -> _models.Owner:
        """Creates a new instance of the resource.

        :param resource: Is one of the following types: OwnerCreate, JSON, IO[bytes] Required.
        :type resource: ~petstore.models.OwnerCreate or JSON or IO[bytes]
        :return: Owner. The Owner is compatible with MutableMapping
        :rtype: ~petstore.models.Owner
        :raises ~corehttp.exceptions.HttpResponseError:
        """
        error_map: MutableMapping = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = kwargs.pop("params", {}) or {}

        content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
        cls: ClsType[_models.Owner] = kwargs.pop("cls", None)

        content_type = content_type or "application/json"
        _content = None
        if isinstance(resource, (IOBase, bytes)):
            _content = resource
        else:
            _content = json.dumps(resource, cls=SdkJSONEncoder, exclude_readonly=True)  # type: ignore

        _request = build_owners_create_request(
            content_type=content_type,
            content=_content,
            headers=_headers,
            params=_params,
        )
        path_format_arguments = {
            "endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, "str", skip_quote=True),
        }
        _request.url = self._client.format_url(_request.url, **path_format_arguments)

        _stream = kwargs.pop("stream", False)
        pipeline_response: PipelineResponse = await self._client.pipeline.run(_request, stream=_stream, **kwargs)

        response = pipeline_response.http_response

        if response.status_code not in [200, 201]:
            if _stream:
                try:
                    await response.read()  # Load the body in memory and close the socket
                except (StreamConsumedError, StreamClosedError):
                    pass
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = _deserialize(_models.PetStoreError, response.json())
            raise HttpResponseError(response=response, model=error)

        if _stream:
            deserialized = response.iter_bytes()
        else:
            deserialized = _deserialize(_models.Owner, response.json())

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore

    async def list(self, **kwargs: Any) -> _models.OwnerCollectionWithNextLink:
        """Lists all instances of the resource.

        :return: OwnerCollectionWithNextLink. The OwnerCollectionWithNextLink is compatible with
         MutableMapping
        :rtype: ~petstore.models.OwnerCollectionWithNextLink
        :raises ~corehttp.exceptions.HttpResponseError:
        """
        error_map: MutableMapping = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = kwargs.pop("params", {}) or {}

        cls: ClsType[_models.OwnerCollectionWithNextLink] = kwargs.pop("cls", None)

        _request = build_owners_list_request(
            headers=_headers,
            params=_params,
        )
        path_format_arguments = {
            "endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, "str", skip_quote=True),
        }
        _request.url = self._client.format_url(_request.url, **path_format_arguments)

        _stream = kwargs.pop("stream", False)
        pipeline_response: PipelineResponse = await self._client.pipeline.run(_request, stream=_stream, **kwargs)

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            if _stream:
                try:
                    await response.read()  # Load the body in memory and close the socket
                except (StreamConsumedError, StreamClosedError):
                    pass
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = _deserialize(_models.PetStoreError, response.json())
            raise HttpResponseError(response=response, model=error)

        if _stream:
            deserialized = response.iter_bytes()
        else:
            deserialized = _deserialize(_models.OwnerCollectionWithNextLink, response.json())

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore


class OwnerCheckupsOperations:
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through
        :class:`~petstore.aio.PetStoreClient`'s
        :attr:`owner_checkups` attribute.
    """

    def __init__(self, *args, **kwargs) -> None:
        input_args = list(args)
        self._client = input_args.pop(0) if input_args else kwargs.pop("client")
        self._config = input_args.pop(0) if input_args else kwargs.pop("config")
        self._serialize = input_args.pop(0) if input_args else kwargs.pop("serializer")
        self._deserialize = input_args.pop(0) if input_args else kwargs.pop("deserializer")

    @overload
    async def create_or_update(
        self,
        owner_id: int,
        checkup_id: int,
        resource: _models.CheckupUpdate,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.Checkup:
        """Creates or update an instance of the extension resource.

        :param owner_id: Required.
        :type owner_id: int
        :param checkup_id: Required.
        :type checkup_id: int
        :param resource: Required.
        :type resource: ~petstore.models.CheckupUpdate
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: Checkup. The Checkup is compatible with MutableMapping
        :rtype: ~petstore.models.Checkup
        :raises ~corehttp.exceptions.HttpResponseError:
        """

    @overload
    async def create_or_update(
        self, owner_id: int, checkup_id: int, resource: JSON, *, content_type: str = "application/json", **kwargs: Any
    ) -> _models.Checkup:
        """Creates or update an instance of the extension resource.

        :param owner_id: Required.
        :type owner_id: int
        :param checkup_id: Required.
        :type checkup_id: int
        :param resource: Required.
        :type resource: JSON
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: Checkup. The Checkup is compatible with MutableMapping
        :rtype: ~petstore.models.Checkup
        :raises ~corehttp.exceptions.HttpResponseError:
        """

    @overload
    async def create_or_update(
        self,
        owner_id: int,
        checkup_id: int,
        resource: IO[bytes],
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.Checkup:
        """Creates or update an instance of the extension resource.

        :param owner_id: Required.
        :type owner_id: int
        :param checkup_id: Required.
        :type checkup_id: int
        :param resource: Required.
        :type resource: IO[bytes]
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: Checkup. The Checkup is compatible with MutableMapping
        :rtype: ~petstore.models.Checkup
        :raises ~corehttp.exceptions.HttpResponseError:
        """

    async def create_or_update(
        self, owner_id: int, checkup_id: int, resource: Union[_models.CheckupUpdate, JSON, IO[bytes]], **kwargs: Any
    ) -> _models.Checkup:
        """Creates or update an instance of the extension resource.

        :param owner_id: Required.
        :type owner_id: int
        :param checkup_id: Required.
        :type checkup_id: int
        :param resource: Is one of the following types: CheckupUpdate, JSON, IO[bytes] Required.
        :type resource: ~petstore.models.CheckupUpdate or JSON or IO[bytes]
        :return: Checkup. The Checkup is compatible with MutableMapping
        :rtype: ~petstore.models.Checkup
        :raises ~corehttp.exceptions.HttpResponseError:
        """
        error_map: MutableMapping = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = kwargs.pop("params", {}) or {}

        content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
        cls: ClsType[_models.Checkup] = kwargs.pop("cls", None)

        content_type = content_type or "application/json"
        _content = None
        if isinstance(resource, (IOBase, bytes)):
            _content = resource
        else:
            _content = json.dumps(resource, cls=SdkJSONEncoder, exclude_readonly=True)  # type: ignore

        _request = build_owner_checkups_create_or_update_request(
            owner_id=owner_id,
            checkup_id=checkup_id,
            content_type=content_type,
            content=_content,
            headers=_headers,
            params=_params,
        )
        path_format_arguments = {
            "endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, "str", skip_quote=True),
        }
        _request.url = self._client.format_url(_request.url, **path_format_arguments)

        _stream = kwargs.pop("stream", False)
        pipeline_response: PipelineResponse = await self._client.pipeline.run(_request, stream=_stream, **kwargs)

        response = pipeline_response.http_response

        if response.status_code not in [200, 201]:
            if _stream:
                try:
                    await response.read()  # Load the body in memory and close the socket
                except (StreamConsumedError, StreamClosedError):
                    pass
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = _deserialize(_models.PetStoreError, response.json())
            raise HttpResponseError(response=response, model=error)

        if _stream:
            deserialized = response.iter_bytes()
        else:
            deserialized = _deserialize(_models.Checkup, response.json())

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore

    async def list(self, owner_id: int, **kwargs: Any) -> _models.CheckupCollectionWithNextLink:
        """Lists all instances of the extension resource.

        :param owner_id: Required.
        :type owner_id: int
        :return: CheckupCollectionWithNextLink. The CheckupCollectionWithNextLink is compatible with
         MutableMapping
        :rtype: ~petstore.models.CheckupCollectionWithNextLink
        :raises ~corehttp.exceptions.HttpResponseError:
        """
        error_map: MutableMapping = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = kwargs.pop("params", {}) or {}

        cls: ClsType[_models.CheckupCollectionWithNextLink] = kwargs.pop("cls", None)

        _request = build_owner_checkups_list_request(
            owner_id=owner_id,
            headers=_headers,
            params=_params,
        )
        path_format_arguments = {
            "endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, "str", skip_quote=True),
        }
        _request.url = self._client.format_url(_request.url, **path_format_arguments)

        _stream = kwargs.pop("stream", False)
        pipeline_response: PipelineResponse = await self._client.pipeline.run(_request, stream=_stream, **kwargs)

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            if _stream:
                try:
                    await response.read()  # Load the body in memory and close the socket
                except (StreamConsumedError, StreamClosedError):
                    pass
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = _deserialize(_models.PetStoreError, response.json())
            raise HttpResponseError(response=response, model=error)

        if _stream:
            deserialized = response.iter_bytes()
        else:
            deserialized = _deserialize(_models.CheckupCollectionWithNextLink, response.json())

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore


class OwnerInsuranceOperations:
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through
        :class:`~petstore.aio.PetStoreClient`'s
        :attr:`owner_insurance` attribute.
    """

    def __init__(self, *args, **kwargs) -> None:
        input_args = list(args)
        self._client = input_args.pop(0) if input_args else kwargs.pop("client")
        self._config = input_args.pop(0) if input_args else kwargs.pop("config")
        self._serialize = input_args.pop(0) if input_args else kwargs.pop("serializer")
        self._deserialize = input_args.pop(0) if input_args else kwargs.pop("deserializer")

    async def get(self, owner_id: int, **kwargs: Any) -> _models.Insurance:
        """Gets the singleton resource.

        :param owner_id: Required.
        :type owner_id: int
        :return: Insurance. The Insurance is compatible with MutableMapping
        :rtype: ~petstore.models.Insurance
        :raises ~corehttp.exceptions.HttpResponseError:
        """
        error_map: MutableMapping = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = kwargs.pop("params", {}) or {}

        cls: ClsType[_models.Insurance] = kwargs.pop("cls", None)

        _request = build_owner_insurance_get_request(
            owner_id=owner_id,
            headers=_headers,
            params=_params,
        )
        path_format_arguments = {
            "endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, "str", skip_quote=True),
        }
        _request.url = self._client.format_url(_request.url, **path_format_arguments)

        _stream = kwargs.pop("stream", False)
        pipeline_response: PipelineResponse = await self._client.pipeline.run(_request, stream=_stream, **kwargs)

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            if _stream:
                try:
                    await response.read()  # Load the body in memory and close the socket
                except (StreamConsumedError, StreamClosedError):
                    pass
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = _deserialize(_models.PetStoreError, response.json())
            raise HttpResponseError(response=response, model=error)

        if _stream:
            deserialized = response.iter_bytes()
        else:
            deserialized = _deserialize(_models.Insurance, response.json())

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore

    @overload
    async def update(
        self,
        owner_id: int,
        properties: _models.InsuranceUpdate,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.Insurance:
        """Updates the singleton resource.

        :param owner_id: Required.
        :type owner_id: int
        :param properties: Required.
        :type properties: ~petstore.models.InsuranceUpdate
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: Insurance. The Insurance is compatible with MutableMapping
        :rtype: ~petstore.models.Insurance
        :raises ~corehttp.exceptions.HttpResponseError:
        """

    @overload
    async def update(
        self, owner_id: int, properties: JSON, *, content_type: str = "application/json", **kwargs: Any
    ) -> _models.Insurance:
        """Updates the singleton resource.

        :param owner_id: Required.
        :type owner_id: int
        :param properties: Required.
        :type properties: JSON
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: Insurance. The Insurance is compatible with MutableMapping
        :rtype: ~petstore.models.Insurance
        :raises ~corehttp.exceptions.HttpResponseError:
        """

    @overload
    async def update(
        self, owner_id: int, properties: IO[bytes], *, content_type: str = "application/json", **kwargs: Any
    ) -> _models.Insurance:
        """Updates the singleton resource.

        :param owner_id: Required.
        :type owner_id: int
        :param properties: Required.
        :type properties: IO[bytes]
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: Insurance. The Insurance is compatible with MutableMapping
        :rtype: ~petstore.models.Insurance
        :raises ~corehttp.exceptions.HttpResponseError:
        """

    async def update(
        self, owner_id: int, properties: Union[_models.InsuranceUpdate, JSON, IO[bytes]], **kwargs: Any
    ) -> _models.Insurance:
        """Updates the singleton resource.

        :param owner_id: Required.
        :type owner_id: int
        :param properties: Is one of the following types: InsuranceUpdate, JSON, IO[bytes] Required.
        :type properties: ~petstore.models.InsuranceUpdate or JSON or IO[bytes]
        :return: Insurance. The Insurance is compatible with MutableMapping
        :rtype: ~petstore.models.Insurance
        :raises ~corehttp.exceptions.HttpResponseError:
        """
        error_map: MutableMapping = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = kwargs.pop("params", {}) or {}

        content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
        cls: ClsType[_models.Insurance] = kwargs.pop("cls", None)

        content_type = content_type or "application/json"
        _content = None
        if isinstance(properties, (IOBase, bytes)):
            _content = properties
        else:
            _content = json.dumps(properties, cls=SdkJSONEncoder, exclude_readonly=True)  # type: ignore

        _request = build_owner_insurance_update_request(
            owner_id=owner_id,
            content_type=content_type,
            content=_content,
            headers=_headers,
            params=_params,
        )
        path_format_arguments = {
            "endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, "str", skip_quote=True),
        }
        _request.url = self._client.format_url(_request.url, **path_format_arguments)

        _stream = kwargs.pop("stream", False)
        pipeline_response: PipelineResponse = await self._client.pipeline.run(_request, stream=_stream, **kwargs)

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            if _stream:
                try:
                    await response.read()  # Load the body in memory and close the socket
                except (StreamConsumedError, StreamClosedError):
                    pass
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = _deserialize(_models.PetStoreError, response.json())
            raise HttpResponseError(response=response, model=error)

        if _stream:
            deserialized = response.iter_bytes()
        else:
            deserialized = _deserialize(_models.Insurance, response.json())

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore
