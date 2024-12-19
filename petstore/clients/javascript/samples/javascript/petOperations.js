const { PetStoreClient } = require("@unbranded/petstore");

// Load the .env file if it exists
require("dotenv").config();

const endpoint = process.env["ENDPOINT"] || "<endpoint>";

const client = new PetStoreClient(endpoint, {
  allowInsecureConnection: true,
});

async function main() {
  // list all pets
  const result = await client.pets.list();
  console.log(result);

  // create a pet, return a pet
  const createPet = await client.pets.create({
    name: "Test",
    age: 5,
    ownerId: 5,
  });
  console.log(createPet);

  // get a pet, return a pet
  const getPet = await client.pets.get(2);
  console.log(getPet);

  // get a invalid pet, return error message is Invalid petId
  try {
    await client.pets.get(-1);
  } catch (e) {
    console.log(e.message);
  }

  // get a non existent pet, return error message is Pet not found
  try {
    await client.pets.get(15);
  } catch (e) {
    console.log(e.message);
  }

  // update a pet, return a pet
  const updatePet = await client.pets.update(2, {
    name: "Test",
    age: 5,
    ownerId: 5,
  });
  console.log(updatePet);

  // update a invalid pet, return error message is Invalid petId
  try {
    await client.pets.update(-1, {
      name: "Test",
      age: 5,
      ownerId: 5,
    });
  } catch (e) {
    console.log(e.message);
  }

  // update a non existent pet, return error message is Pet not found
  try {
    await client.pets.update(15, {
      name: "Test",
      age: 5,
      ownerId: 5,
    });
  } catch (e) {
    console.log(e.message);
  }

  // delete a pet, return undefined
  const deletePet = await client.pets.delete(1);
  console.log(deletePet);

  // delete a invalid pet, return error message is Invalid petId
  try {
    await client.pets.delete(-1);
  } catch (e) {
    console.log(e.message);
  }

  // delete a non existent pet, return error message is Pet not found
  try {
    await client.pets.delete(15);
  } catch (e) {
    console.log(e.message);
  }
}

main().catch(console.error);
