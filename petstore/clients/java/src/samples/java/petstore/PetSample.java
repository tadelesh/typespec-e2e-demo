package java.petstore;

import petstore.Pet;
import petstore.PetStoreClientBuilder;
import petstore.PetsClient;
import typespec.rest.resource.PetCreate;
import typespec.rest.resource.PetUpdate;

public final class PetSample {

    public static void main(String... args) {

        // client
        PetsClient client = new PetStoreClientBuilder()
                .endpoint("http://localhost:5118/")
                .buildPetsClient();

        // create pet
        Pet pet = client.create(new PetCreate("MyPet", 7, 7L));
        int petId = pet.getId();

        // get pet
        pet = client.get(petId);

        // update pet
        pet = client.update(petId, new PetUpdate().setAge(8));

        // delete pet
        client.delete(petId);
    }
}
