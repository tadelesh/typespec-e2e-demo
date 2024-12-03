package petstore;

import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.api.Test;
import petstore.models.Pet;

public final class PetsTests {

    private final PetsClient client = new PetStoreClientBuilder()
            .endpoint("http://localhost:5118/")
            .buildPetsClient();

    @Test
    public void get() {
        int petId = 1;
        Pet pet = client.get(petId);
        Assertions.assertEquals(petId, pet.getId());
        Assertions.assertEquals("Kiwi", pet.getName());
    }
}
