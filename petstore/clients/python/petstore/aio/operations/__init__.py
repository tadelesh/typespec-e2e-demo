# coding=utf-8

# pylint: disable=wrong-import-position

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ._patch import *  # pylint: disable=unused-wildcard-import

from ._operations import PetsOperations  # type: ignore
from ._operations import PetCheckupsOperations  # type: ignore
from ._operations import PetInsuranceOperations  # type: ignore
from ._operations import ToysOperations  # type: ignore
from ._operations import ToyInsuranceOperations  # type: ignore
from ._operations import CheckupsOperations  # type: ignore
from ._operations import OwnersOperations  # type: ignore
from ._operations import OwnerCheckupsOperations  # type: ignore
from ._operations import OwnerInsuranceOperations  # type: ignore

from ._patch import __all__ as _patch_all
from ._patch import *
from ._patch import patch_sdk as _patch_sdk

__all__ = [
    "PetsOperations",
    "PetCheckupsOperations",
    "PetInsuranceOperations",
    "ToysOperations",
    "ToyInsuranceOperations",
    "CheckupsOperations",
    "OwnersOperations",
    "OwnerCheckupsOperations",
    "OwnerInsuranceOperations",
]
__all__.extend([p for p in _patch_all if p not in __all__])  # pyright: ignore
_patch_sdk()
