from petstore import PetStoreClient
from petstore.models import PetCreate, PetUpdate

petStoreClient = PetStoreClient("http://localhost:5118")

# create a pet
pet = petStoreClient.pets.create(PetCreate(name="Kiwi", age=5, owner_id=0))
print(f"created pet: {pet}")

# get a pet from id
pet = petStoreClient.pets.get(pet.id)
print(f"get pet: {pet}")

# update a pet by id
pet = petStoreClient.pets.update(pet.id, PetUpdate(name="CoCo", tag="changed", owner_id=314))
print(f"pet updated: {pet}")

# list all available pets
pets = petStoreClient.pets.list().value
for pet in pets:
    print(f"list pet: {pet}")

# delete a pet by id
petStoreClient.pets.delete(pet.id)
print("pet deleted")
