using PetStore.Models;
using System.ClientModel;
using System.IO;
using System.Text;
using System.Text.Json;

namespace PetStore.Tests
{
    public class PetsClientTests
    {
        private Pets _petsClient;

        [OneTimeSetUp]
        public void Setup()
        {
            _petsClient = new PetStoreClient(new Uri("http://localhost:5118")).GetPetsClient();
        }

        [Test]
        public async Task Validate_GetPet_Succeeded()
        {
            var response = await _petsClient.GetAsync(0);
            Assert.NotNull(response);
            Assert.NotNull(response.Value);
            Assert.AreEqual(0, response.Value.Id);
            Assert.AreEqual("Kiwi", response.Value.Name);
            Assert.AreEqual(null, response.Value.Tag);
            Assert.AreEqual(5, response.Value.Age);
            Assert.AreEqual(5, response.Value.OwnerId);
        }

        [Test]
        public async Task Validate_GetPet_Invalid()
        {
            var exception = Assert.ThrowsAsync<ClientResultException>(async () => await _petsClient.GetAsync(-10));

            Assert.NotNull(exception);
            Assert.AreEqual(400, exception.Status);

            var response = exception.GetRawResponse();
            Assert.NotNull(response);
            Assert.NotNull(response?.ContentStream);
            using var doc = JsonDocument.Parse(response.ContentStream);
            Assert.AreEqual(0, doc.RootElement.GetProperty("code").GetInt32());
            Assert.AreEqual("Invalid petId", doc.RootElement.GetProperty("message").GetString());
        }

        [Test]
        public async Task Validate_GetPet_NotFound()
        {
            var exception = Assert.ThrowsAsync<ClientResultException>(async () => await _petsClient.GetAsync(100));

            Assert.NotNull(exception);
            Assert.AreEqual(404, exception.Status);

            var response = exception.GetRawResponse();
            Assert.NotNull(response);
            Assert.NotNull(response?.ContentStream);
            using var doc = JsonDocument.Parse(response.ContentStream);
            Assert.AreEqual(1, doc.RootElement.GetProperty("code").GetInt32());
            Assert.AreEqual("Pet not found", doc.RootElement.GetProperty("message").GetString());
        }

        [Test]
        public async Task Validate_CreatePet_Succeeded()
        {
            var response = await _petsClient.CreateAsync(new PetCreate("MyPet", 5, 5)
            {
                Tag = "MyTag",
            });
            Assert.NotNull(response);
            Assert.NotNull(response.Value);
            Assert.AreEqual("MyPet", response.Value.Name);
            Assert.AreEqual("MyTag", response.Value.Tag);
            Assert.AreEqual(5, response.Value.Age);
            Assert.AreEqual(5, response.Value.OwnerId);
            Assert.AreEqual(0, response.Value.Id);
        }

        [Test]
        public async Task Validate_CreatePet_Failed()
        {
            var exception = Assert.ThrowsAsync<ClientResultException>(async () => await _petsClient.CreateAsync(new PetCreate("MyPet", 50, 100)
            {
                Tag = "MyTag",
            }));
            Assert.NotNull(exception);
            Assert.AreEqual(400, exception.Status);
            using var doc = JsonDocument.Parse(exception.GetRawResponse().ContentStream);
            Assert.AreEqual(400, doc.RootElement.GetProperty("code").GetInt32());
            Assert.AreEqual("50 is outside the allowed range of [0, 20]", doc.RootElement.GetProperty("message").GetString());
        }

        [Test]
        public async Task Validate_DeletePet()
        {
            var response = await _petsClient.DeleteAsync(0);

            Assert.NotNull(response);
            Assert.AreEqual(200, response.GetRawResponse().Status);
        }

        [Test]
        public async Task Validate_UpdatePet_Succeeded()
        {
            var update = new
            {
                age = 5,
                name = "Coco",
                ownerId = 314,
                tag = "changed"
            };
            var response = await _petsClient.UpdateAsync(0, BinaryContent.Create(BinaryData.FromObjectAsJson(update)));

            Assert.NotNull(response);
            var responseContent = response.GetRawResponse().ContentStream;
            using var doc = JsonDocument.Parse(responseContent);
            Assert.AreEqual(0, doc.RootElement.GetProperty("id").GetInt32());
            Assert.AreEqual("Coco", doc.RootElement.GetProperty("name").GetString());
            Assert.AreEqual("changed", doc.RootElement.GetProperty("tag").GetString());
            Assert.AreEqual(5, doc.RootElement.GetProperty("age").GetInt32());
            Assert.AreEqual(314, doc.RootElement.GetProperty("ownerId").GetInt32());
        }

        [Test]
        public async Task Validate_UpdatePet_Invalid()
        {
            var update = new
            {
                age = 5,
                name = "Coco",
                ownerId = 314,
                tag = "changed"
            };

            var exception = Assert.ThrowsAsync<ClientResultException>(async () => await _petsClient.UpdateAsync(-10, BinaryContent.Create(BinaryData.FromObjectAsJson(update))));
            Assert.NotNull(exception);
            Assert.AreEqual(400, exception.Status);
            using var doc = JsonDocument.Parse(exception.GetRawResponse().ContentStream);
            Assert.AreEqual(0, doc.RootElement.GetProperty("code").GetInt32());
            Assert.AreEqual("Invalid petId", doc.RootElement.GetProperty("message").GetString());
        }

        [Test]
        public async Task Validate_UpdatePet_NotFound()
        {
            var update = new
            {
                age = 5,
                name = "Coco",
                ownerId = 314,
                tag = "changed"
            };

            var exception = Assert.ThrowsAsync<ClientResultException>(async () => await _petsClient.UpdateAsync(100, BinaryContent.Create(BinaryData.FromObjectAsJson(update))));
            Assert.NotNull(exception);
            Assert.AreEqual(404, exception.Status);
            using var doc = JsonDocument.Parse(exception.GetRawResponse().ContentStream);
            Assert.AreEqual(1, doc.RootElement.GetProperty("code").GetInt32());
            Assert.AreEqual("Pet not found", doc.RootElement.GetProperty("message").GetString());
        }

        [Test]
        public async Task Validate_List()
        {
            // TODO -- paging is not supported yet
            var response = await _petsClient.ListAsync();

            Assert.NotNull(response);
            Assert.NotNull(response.Value);
            Assert.AreEqual(2, response.Value.Value.Count);

            var first = response.Value.Value[0];
            Assert.AreEqual(1, first.Id);
            Assert.AreEqual("Kiwi", first.Name);
            Assert.AreEqual(null, first.Tag);
            Assert.AreEqual(5, first.Age);
            Assert.AreEqual(5, first.OwnerId);

            var second = response.Value.Value[1];
            Assert.AreEqual(2, second.Id);
            Assert.AreEqual("Coco", second.Name);
            Assert.AreEqual(null, second.Tag);
            Assert.AreEqual(6, second.Age);
            Assert.AreEqual(6, second.OwnerId);
        }
    }
}