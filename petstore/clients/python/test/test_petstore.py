import pytest
from petstore import PetStoreClient
from petstore.models import PetCreate, PetUpdate
from corehttp.exceptions import HttpResponseError


@pytest.fixture
def client():
    return PetStoreClient("http://localhost:5118")


def test_pets_list(client):
    # list pets, return a list of pets
    pager = client.pets.list()
    result = list(pager.value)
    assert len(result) == 2
    assert result[0].name == "Kiwi"
    assert result[0].age == 5
    assert result[0].owner_id == 5
    assert result[1].name == "Coco"
    assert result[1].age == 6
    assert result[1].owner_id == 6


def test_pets_get(client):
    # get a pet by id, return a pet
    pet = client.pets.get(1)
    assert pet.name == "Kiwi"
    assert pet.age == 5
    assert pet.owner_id == 5


def test_pets_get_invalid_pet(client):
    with pytest.raises(HttpResponseError) as exc_info:
        client.pets.get(-1)
    error = exc_info.value.response.json()
    assert error["code"] == 0
    assert error["message"] == "Invalid petId"


def test_pets_get_non_exist_pet(client):
    with pytest.raises(HttpResponseError) as exc_info:
        client.pets.get(15)
    error = exc_info.value.response.json()
    assert error["code"] == 1
    assert error["message"] == "Pet not found"


def test_pets_create(client):
    pet = PetCreate(name="Kiwi", age=5, owner_id=5)
    result = client.pets.create(pet)
    assert result.name == "Kiwi"
    assert result.age == 5
    assert result.owner_id == 5


def test_pets_update(client):
    pet = PetUpdate(name="Kiwi", age=5, owner_id=5)
    result = client.pets.update(0, pet)
    assert result.name == "Kiwi"
    assert result.age == 5
    assert result.owner_id == 5


def test_pets_update_invalid_pet(client):
    with pytest.raises(HttpResponseError) as exc_info:
        pet = PetUpdate(name="Kiwi", age=5, owner_id=5)
        result = client.pets.update(-1, pet)
    error = exc_info.value.response.json()
    assert error["code"] == 0
    assert error["message"] == "Invalid petId"


def test_pets_update_non_exist_pet(client):
    with pytest.raises(HttpResponseError) as exc_info:
        pet = PetUpdate(name="Kiwi", age=5, owner_id=5)
        result = client.pets.update(15, pet)
    error = exc_info.value.response.json()
    assert error["code"] == 1
    assert error["message"] == "Pet not found"


def test_pets_delete(client):
    client.pets.delete(0)


def test_pets_delete_invalid_pet(client):
    with pytest.raises(HttpResponseError) as exc_info:
        client.pets.delete(-1)
    error = exc_info.value.response.json()
    assert error["code"] == 0
    assert error["message"] == "Invalid petId"


def test_pets_delete_non_exist_pet(client):
    with pytest.raises(HttpResponseError) as exc_info:
        client.pets.delete(15)
    error = exc_info.value.response.json()
    assert error["code"] == 1
    assert error["message"] == "Pet not found"
