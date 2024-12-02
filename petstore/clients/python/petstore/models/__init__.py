# coding=utf-8

# pylint: disable=wrong-import-position

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ._patch import *  # pylint: disable=unused-wildcard-import


from ._models import (  # type: ignore
    Checkup,
    CheckupCollectionWithNextLink,
    CheckupUpdate,
    Insurance,
    InsuranceUpdate,
    Owner,
    OwnerCollectionWithNextLink,
    OwnerCreate,
    OwnerUpdate,
    Pet,
    PetCollectionWithNextLink,
    PetCreate,
    PetStoreError,
    PetUpdate,
    Toy,
    ToyCollectionWithNextLink,
)
from ._patch import __all__ as _patch_all
from ._patch import *
from ._patch import patch_sdk as _patch_sdk

__all__ = [
    "Checkup",
    "CheckupCollectionWithNextLink",
    "CheckupUpdate",
    "Insurance",
    "InsuranceUpdate",
    "Owner",
    "OwnerCollectionWithNextLink",
    "OwnerCreate",
    "OwnerUpdate",
    "Pet",
    "PetCollectionWithNextLink",
    "PetCreate",
    "PetStoreError",
    "PetUpdate",
    "Toy",
    "ToyCollectionWithNextLink",
]
__all__.extend([p for p in _patch_all if p not in __all__])  # pyright: ignore
_patch_sdk()
