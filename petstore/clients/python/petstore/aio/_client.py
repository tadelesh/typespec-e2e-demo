# coding=utf-8


from copy import deepcopy
from typing import Any, Awaitable
from typing_extensions import Self

from corehttp.rest import AsyncHttpResponse, HttpRequest
from corehttp.runtime import AsyncPipelineClient, policies

from .._serialization import Deserializer, Serializer
from ._configuration import PetStoreClientConfiguration
from .operations import (
    CheckupsOperations,
    OwnerCheckupsOperations,
    OwnerInsuranceOperations,
    OwnersOperations,
    PetCheckupsOperations,
    PetInsuranceOperations,
    PetsOperations,
    ToyInsuranceOperations,
    ToysOperations,
)


class PetStoreClient:  # pylint: disable=client-accepts-api-version-keyword,too-many-instance-attributes
    """PetStoreClient.

    :ivar pets: PetsOperations operations
    :vartype pets: petstore.aio.operations.PetsOperations
    :ivar pet_checkups: PetCheckupsOperations operations
    :vartype pet_checkups: petstore.aio.operations.PetCheckupsOperations
    :ivar pet_insurance: PetInsuranceOperations operations
    :vartype pet_insurance: petstore.aio.operations.PetInsuranceOperations
    :ivar toys: ToysOperations operations
    :vartype toys: petstore.aio.operations.ToysOperations
    :ivar toy_insurance: ToyInsuranceOperations operations
    :vartype toy_insurance: petstore.aio.operations.ToyInsuranceOperations
    :ivar checkups: CheckupsOperations operations
    :vartype checkups: petstore.aio.operations.CheckupsOperations
    :ivar owners: OwnersOperations operations
    :vartype owners: petstore.aio.operations.OwnersOperations
    :ivar owner_checkups: OwnerCheckupsOperations operations
    :vartype owner_checkups: petstore.aio.operations.OwnerCheckupsOperations
    :ivar owner_insurance: OwnerInsuranceOperations operations
    :vartype owner_insurance: petstore.aio.operations.OwnerInsuranceOperations
    :param endpoint: Service host. Required.
    :type endpoint: str
    """

    def __init__(  # pylint: disable=missing-client-constructor-parameter-credential
        self, endpoint: str, **kwargs: Any
    ) -> None:
        _endpoint = "{endpoint}"
        self._config = PetStoreClientConfiguration(endpoint=endpoint, **kwargs)
        _policies = kwargs.pop("policies", None)
        if _policies is None:
            _policies = [
                self._config.headers_policy,
                self._config.user_agent_policy,
                self._config.proxy_policy,
                policies.ContentDecodePolicy(**kwargs),
                self._config.retry_policy,
                self._config.authentication_policy,
                self._config.logging_policy,
            ]
        self._client: AsyncPipelineClient = AsyncPipelineClient(endpoint=_endpoint, policies=_policies, **kwargs)

        self._serialize = Serializer()
        self._deserialize = Deserializer()
        self._serialize.client_side_validation = False
        self.pets = PetsOperations(self._client, self._config, self._serialize, self._deserialize)
        self.pet_checkups = PetCheckupsOperations(self._client, self._config, self._serialize, self._deserialize)
        self.pet_insurance = PetInsuranceOperations(self._client, self._config, self._serialize, self._deserialize)
        self.toys = ToysOperations(self._client, self._config, self._serialize, self._deserialize)
        self.toy_insurance = ToyInsuranceOperations(self._client, self._config, self._serialize, self._deserialize)
        self.checkups = CheckupsOperations(self._client, self._config, self._serialize, self._deserialize)
        self.owners = OwnersOperations(self._client, self._config, self._serialize, self._deserialize)
        self.owner_checkups = OwnerCheckupsOperations(self._client, self._config, self._serialize, self._deserialize)
        self.owner_insurance = OwnerInsuranceOperations(self._client, self._config, self._serialize, self._deserialize)

    def send_request(
        self, request: HttpRequest, *, stream: bool = False, **kwargs: Any
    ) -> Awaitable[AsyncHttpResponse]:
        """Runs the network request through the client's chained policies.

        >>> from corehttp.rest import HttpRequest
        >>> request = HttpRequest("GET", "https://www.example.org/")
        <HttpRequest [GET], url: 'https://www.example.org/'>
        >>> response = await client.send_request(request)
        <AsyncHttpResponse: 200 OK>

        For more information on this code flow, see https://aka.ms/azsdk/dpcodegen/python/send_request

        :param request: The network request you want to make. Required.
        :type request: ~corehttp.rest.HttpRequest
        :keyword bool stream: Whether the response payload will be streamed. Defaults to False.
        :return: The response of your network call. Does not do error handling on your response.
        :rtype: ~corehttp.rest.AsyncHttpResponse
        """

        request_copy = deepcopy(request)
        path_format_arguments = {
            "endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, "str", skip_quote=True),
        }

        request_copy.url = self._client.format_url(request_copy.url, **path_format_arguments)
        return self._client.send_request(request_copy, stream=stream, **kwargs)  # type: ignore

    async def close(self) -> None:
        await self._client.close()

    async def __aenter__(self) -> Self:
        await self._client.__aenter__()
        return self

    async def __aexit__(self, *exc_details: Any) -> None:
        await self._client.__aexit__(*exc_details)
