using PetStore;
using PetStore.Models;
using System.ClientModel;

Pets petsClient = new PetStoreClient(new Uri("http://localhost:5118")).GetPetsClient();

// create a pet
ClientResult<Pet> petCreateResult = await petsClient.CreateAsync(new PetCreate("Kiwi", 5, 0));
Pet pet = petCreateResult.Value;
Console.WriteLine($"Created pet: {pet.Id}");

// get a pet from id
ClientResult<Pet> getPetResult = await petsClient.GetAsync(pet.Id);
Pet petFromId = getPetResult.Value;
Console.WriteLine($"Got pet: {petFromId.Name}");

// update the update by id
ClientResult updatePetResult = await petsClient.UpdateAsync(petFromId.Id, BinaryContent.Create(BinaryData.FromObjectAsJson(new
{
    name = "Coco",
    ownerId = 314,
    tag = "changed"
})));
Console.WriteLine("Pet updated.");

// list all available pets
ClientResult<PetCollectionWithNextLink> listResult = await petsClient.ListAsync();
IList<Pet> listOfPets = listResult.Value.Value;
foreach (Pet p in listOfPets)
{
    Console.WriteLine($"Pet: {p.Name}");
}

// delete the pet by id
await petsClient.DeleteAsync(pet.Id);
Console.WriteLine("Pet deleted.");
