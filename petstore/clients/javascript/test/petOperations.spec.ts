// Copyright (c) Microsoft Corporation.
// Licensed under the MIT License.
import { PetStoreClient } from "@unbranded/petstore";
import { assert, beforeEach, it, describe } from "vitest";

describe("PetOperations Samples", () => {
  let client: PetStoreClient;
  beforeEach(async function () {
    client = new PetStoreClient("http://localhost:5118", {
      allowInsecureConnection: true,
    });
  });
  const pet = {
    name: "Kiwi",
    age: 5,
    ownerId: 5,
  };

  it("pet list", async function () {
    // list pets, return a list of pets
    const petList = await client.pets.list();
    assert.equal(petList.value[0].name, "Kiwi");
    assert.equal(petList.value[0].age, 5);
    assert.equal(petList.value[0].ownerId, 5);
    assert.equal(petList.value[1].name, "Coco");
    assert.equal(petList.value[1].age, 6);
    assert.equal(petList.value[1].ownerId, 6);
  });

  it("pet get", async function () {
    // get a pet, return a pet
    const result = await client.pets.get(1);
    assert.equal(result.name, "Kiwi");
    assert.equal(result.age, 5);
    assert.equal(result.ownerId, 5);
  });

  it("get a invalid pet", async function () {
    // get a invalid pet, return error message is Invalid petId. 
    // refer to: https://github.com/allenjzhang/typespec-e2e-demo/blob/main/petstore/servers/aspnet/implemented_apis.md
    try {
      await client.pets.get(-1);
    } catch (error) {
      assert.equal(error.code, 0);
      assert.equal(error.message, "Invalid petId");
    }
  });

  it("get a non existent pet", async function () {
    // get a non existent pet, return error message is Pet not found
    try {
      await client.pets.get(15);
    } catch (error) {
      assert.equal(error.code, 1);
      assert.equal(error.message, "Pet not found");
    }
  });

  it("pet create", async function () {
    const result = await client.pets.create(pet);
    assert.equal(result.name, "Kiwi");
    assert.equal(result.age, 5);
    assert.equal(result.ownerId, 5);
  });

  it("pet update", async function () {
    // update a pet, return a pet
    const result = await client.pets.update(1, pet);
    assert.equal(result.name, "Kiwi");
    assert.equal(result.age, 5);
    assert.equal(result.ownerId, 5);
  });

  it("pet update a invalid pet", async function () {
    // update a invalid pet, return error message is Invalid petId
    try {
      await client.pets.update(-1, pet);
    } catch (error) {
      assert.equal(error.code, 0);
      assert.equal(error.message, "Invalid petId");
    }
  });

  it("pet update a non existent pet", async function () {
    // update a non existent pet, return error message is Pet not found
    try {
      await client.pets.update(15, pet);
    } catch (error) {
      assert.equal(error.code, 1);
      assert.equal(error.message, "Pet not found");
    }
  });

  it("pet delete", async function () {
    // delete a pet, return undefined
    const result = await client.pets.delete(1);
    assert.equal(result, undefined);
  });

  it("delete a invalid pet", async function () {
    // delete a invalid pet, return error message is Invalid petId
    try {
      await client.pets.delete(-1);
    } catch (error) {
      assert.equal(error.code, 0);
      assert.equal(error.message, "Invalid petId");
    }
  });

  it("delete a non existent pet", async function () {
    // delete a non existent pet, return error message is Pet not found
    try {
      await client.pets.delete(15);
    } catch (error) {
      assert.equal(error.code, 1);
      assert.equal(error.message, "Pet not found");
    }
  });
});
