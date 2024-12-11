# coding=utf-8

# pylint: disable=useless-super-delegation

from typing import Any, List, Mapping, Optional, TYPE_CHECKING, overload

from .. import _model_base
from .._model_base import rest_field

if TYPE_CHECKING:
    from .. import models as _models


class Checkup(_model_base.Model):
    """Checkup.


    :ivar id: Required.
    :vartype id: int
    :ivar vet_name: Required.
    :vartype vet_name: str
    :ivar notes: Required.
    :vartype notes: str
    """

    id: int = rest_field()
    """Required."""
    vet_name: str = rest_field(name="vetName")
    """Required."""
    notes: str = rest_field()
    """Required."""

    @overload
    def __init__(
        self,
        *,
        id: int,  # pylint: disable=redefined-builtin
        vet_name: str,
        notes: str,
    ) -> None: ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]) -> None:
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)


class CheckupCollectionWithNextLink(_model_base.Model):
    """Paged response of Checkup items.


    :ivar value: The items on this page. Required.
    :vartype value: list[~petstore.models.Checkup]
    :ivar next_link: The link to the next page of items.
    :vartype next_link: str
    """

    value: List["_models.Checkup"] = rest_field()
    """The items on this page. Required."""
    next_link: Optional[str] = rest_field(name="nextLink")
    """The link to the next page of items."""

    @overload
    def __init__(
        self,
        *,
        value: List["_models.Checkup"],
        next_link: Optional[str] = None,
    ) -> None: ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]) -> None:
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)


class CheckupUpdate(_model_base.Model):
    """Resource create or update operation model.

    :ivar vet_name:
    :vartype vet_name: str
    :ivar notes:
    :vartype notes: str
    """

    vet_name: Optional[str] = rest_field(name="vetName")
    notes: Optional[str] = rest_field()

    @overload
    def __init__(
        self,
        *,
        vet_name: Optional[str] = None,
        notes: Optional[str] = None,
    ) -> None: ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]) -> None:
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)


class Insurance(_model_base.Model):
    """Insurance.


    :ivar provider: Required.
    :vartype provider: str
    :ivar premium: Required.
    :vartype premium: int
    :ivar deductible: Required.
    :vartype deductible: int
    """

    provider: str = rest_field()
    """Required."""
    premium: int = rest_field()
    """Required."""
    deductible: int = rest_field()
    """Required."""

    @overload
    def __init__(
        self,
        *,
        provider: str,
        premium: int,
        deductible: int,
    ) -> None: ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]) -> None:
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)


class InsuranceUpdate(_model_base.Model):
    """Resource create or update operation model.

    :ivar provider:
    :vartype provider: str
    :ivar premium:
    :vartype premium: int
    :ivar deductible:
    :vartype deductible: int
    """

    provider: Optional[str] = rest_field()
    premium: Optional[int] = rest_field()
    deductible: Optional[int] = rest_field()

    @overload
    def __init__(
        self,
        *,
        provider: Optional[str] = None,
        premium: Optional[int] = None,
        deductible: Optional[int] = None,
    ) -> None: ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]) -> None:
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)


class Owner(_model_base.Model):
    """Owner.


    :ivar id: Required.
    :vartype id: int
    :ivar name: Required.
    :vartype name: str
    :ivar age: Required.
    :vartype age: int
    """

    id: int = rest_field()
    """Required."""
    name: str = rest_field()
    """Required."""
    age: int = rest_field()
    """Required."""

    @overload
    def __init__(
        self,
        *,
        id: int,  # pylint: disable=redefined-builtin
        name: str,
        age: int,
    ) -> None: ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]) -> None:
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)


class OwnerCollectionWithNextLink(_model_base.Model):
    """Paged response of Owner items.


    :ivar value: The items on this page. Required.
    :vartype value: list[~petstore.models.Owner]
    :ivar next_link: The link to the next page of items.
    :vartype next_link: str
    """

    value: List["_models.Owner"] = rest_field()
    """The items on this page. Required."""
    next_link: Optional[str] = rest_field(name="nextLink")
    """The link to the next page of items."""

    @overload
    def __init__(
        self,
        *,
        value: List["_models.Owner"],
        next_link: Optional[str] = None,
    ) -> None: ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]) -> None:
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)


class OwnerCreate(_model_base.Model):
    """Resource create operation model.

    All required parameters must be populated in order to send to server.

    :ivar name: Required.
    :vartype name: str
    :ivar age: Required.
    :vartype age: int
    """

    name: str = rest_field()
    """Required."""
    age: int = rest_field()
    """Required."""

    @overload
    def __init__(
        self,
        *,
        name: str,
        age: int,
    ) -> None: ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]) -> None:
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)


class OwnerUpdate(_model_base.Model):
    """Resource create or update operation model.

    :ivar name:
    :vartype name: str
    :ivar age:
    :vartype age: int
    """

    name: Optional[str] = rest_field()
    age: Optional[int] = rest_field()

    @overload
    def __init__(
        self,
        *,
        name: Optional[str] = None,
        age: Optional[int] = None,
    ) -> None: ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]) -> None:
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)


class Pet(_model_base.Model):
    """Pet.


    :ivar id: Required.
    :vartype id: int
    :ivar name: Required.
    :vartype name: str
    :ivar tag:
    :vartype tag: str
    :ivar age: Required.
    :vartype age: int
    :ivar owner_id: Required.
    :vartype owner_id: int
    """

    id: int = rest_field()
    """Required."""
    name: str = rest_field()
    """Required."""
    tag: Optional[str] = rest_field()
    age: int = rest_field()
    """Required."""
    owner_id: int = rest_field(name="ownerId")
    """Required."""

    @overload
    def __init__(
        self,
        *,
        id: int,  # pylint: disable=redefined-builtin
        name: str,
        age: int,
        owner_id: int,
        tag: Optional[str] = None,
    ) -> None: ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]) -> None:
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)


class PetCollectionWithNextLink(_model_base.Model):
    """Paged response of Pet items.


    :ivar value: The items on this page. Required.
    :vartype value: list[~petstore.models.Pet]
    :ivar next_link: The link to the next page of items.
    :vartype next_link: str
    """

    value: List["_models.Pet"] = rest_field()
    """The items on this page. Required."""
    next_link: Optional[str] = rest_field(name="nextLink")
    """The link to the next page of items."""

    @overload
    def __init__(
        self,
        *,
        value: List["_models.Pet"],
        next_link: Optional[str] = None,
    ) -> None: ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]) -> None:
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)


class PetCreate(_model_base.Model):
    """Resource create operation model.

    All required parameters must be populated in order to send to server.

    :ivar name: Required.
    :vartype name: str
    :ivar tag:
    :vartype tag: str
    :ivar age: Required.
    :vartype age: int
    :ivar owner_id: Required.
    :vartype owner_id: int
    """

    name: str = rest_field()
    """Required."""
    tag: Optional[str] = rest_field()
    age: int = rest_field()
    """Required."""
    owner_id: int = rest_field(name="ownerId")
    """Required."""

    @overload
    def __init__(
        self,
        *,
        name: str,
        age: int,
        owner_id: int,
        tag: Optional[str] = None,
    ) -> None: ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]) -> None:
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)


class PetStoreError(_model_base.Model):
    """PetStoreError.

    All required parameters must be populated in order to send to server.

    :ivar code: Required.
    :vartype code: int
    :ivar message: Required.
    :vartype message: str
    """

    code: int = rest_field()
    """Required."""
    message: str = rest_field()
    """Required."""

    @overload
    def __init__(
        self,
        *,
        code: int,
        message: str,
    ) -> None: ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]) -> None:
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)


class PetUpdate(_model_base.Model):
    """Resource create or update operation model.

    :ivar name:
    :vartype name: str
    :ivar tag:
    :vartype tag: str
    :ivar age:
    :vartype age: int
    :ivar owner_id:
    :vartype owner_id: int
    """

    name: Optional[str] = rest_field()
    tag: Optional[str] = rest_field()
    age: Optional[int] = rest_field()
    owner_id: Optional[int] = rest_field(name="ownerId")

    @overload
    def __init__(
        self,
        *,
        name: Optional[str] = None,
        tag: Optional[str] = None,
        age: Optional[int] = None,
        owner_id: Optional[int] = None,
    ) -> None: ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]) -> None:
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)


class Toy(_model_base.Model):
    """Toy.


    :ivar id: Required.
    :vartype id: int
    :ivar pet_id: Required.
    :vartype pet_id: int
    :ivar name: Required.
    :vartype name: str
    """

    id: int = rest_field()
    """Required."""
    pet_id: int = rest_field(name="petId")
    """Required."""
    name: str = rest_field()
    """Required."""

    @overload
    def __init__(
        self,
        *,
        id: int,  # pylint: disable=redefined-builtin
        pet_id: int,
        name: str,
    ) -> None: ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]) -> None:
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)


class ToyCollectionWithNextLink(_model_base.Model):
    """Paged response of Toy items.


    :ivar value: The items on this page. Required.
    :vartype value: list[~petstore.models.Toy]
    :ivar next_link: The link to the next page of items.
    :vartype next_link: str
    """

    value: List["_models.Toy"] = rest_field()
    """The items on this page. Required."""
    next_link: Optional[str] = rest_field(name="nextLink")
    """The link to the next page of items."""

    @overload
    def __init__(
        self,
        *,
        value: List["_models.Toy"],
        next_link: Optional[str] = None,
    ) -> None: ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]) -> None:
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
