package petstore;

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
        System.out.println("pet created, id=" + petId);

        // get pet
        pet = client.get(petId);
        System.out.println("pet queried, name=" + pet.getName());

        // update pet
        pet = client.update(petId, new PetUpdate().setAge(8));
        System.out.println("pet updated, age=" + pet.getAge());

        // delete pet
        client.delete(petId);
        System.out.println("pet deleted, id=" + petId);

        System.exit(0);
    }
}
