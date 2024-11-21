namespace PetStore.Tests
{
    public class PetsClientTests
    {
        [Test]
        public async Task Validate_GetPet()
        {
            var client = new PetStoreClient(new Uri("http://localhost:5118")).GetPetsClient();
            var response = await client.GetAsync(0);
            Assert.NotNull(response);
            Assert.NotNull(response.Value);
            Assert.AreEqual(0, response.Value.Id);
            Assert.AreEqual("Kiwi", response.Value.Name);
            Assert.AreEqual(null, response.Value.Tag);
            Assert.AreEqual(5, response.Value.Age);
            Assert.AreEqual(5, response.Value.OwnerId);
        }
    }
}