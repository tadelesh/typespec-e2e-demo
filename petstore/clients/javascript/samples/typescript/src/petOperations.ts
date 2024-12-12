import { PetStoreClient } from '@unbranded/petstore';

// Load the .env file if it exists  
import * as dotenv from "dotenv";
dotenv.config();

const endpoint = process.env["ENDPOINT"] || "<endpoint>";

const client = new PetStoreClient(endpoint, {
  allowInsecureConnection: true
});

async function main() {
  // list all pets
  const result = await client.pets.list();
  console.log(result);

  // create a pet, return a pet
  const createPet = await client.pets.create({ name: 'Test', age: 5, ownerId: 5 });
  console.log(createPet);

  // get a pet, return a pet
  const getPet = await client.pets.get(2);
  console.log(getPet);

  // update a pet, return a pet
  const updatePet = await client.pets.update(2, { name: 'Test', age: 5, ownerId: 5 });
  console.log(updatePet);

  // delete a pet, return undefined
  await client.pets.delete(1);
}

main().catch(console.error);