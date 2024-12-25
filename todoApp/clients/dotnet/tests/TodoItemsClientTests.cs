using System.ClientModel;
using System.Text.Json;
using Todo.Models;

namespace Todo.Tests
{
    public class TodoItemsClientTests
    {
        private TodoItems _itemsClient;

        [OneTimeSetUp]
        public void Setup()
        {
            var cred = new ApiKeyCredential("stub");
            _itemsClient = new TodoClient(new Uri("http://localhost:5244"), cred).GetTodoItemsClient();
        }

        [TearDown]
        public async Task Cleanup()
        {
            try
            {
                await _itemsClient.DeleteAsync(0);
            }
            catch { }
        }

        [Test]
        public async Task CreateJson()
        {
            var item = new TodoItem("Buy milk", TodoItemStatus.NotStarted)
            {
                AssignedTo = 1,
                Description = "Need to buy milk from the store",
            };
            var response = await _itemsClient.CreateJsonAsync(item);

            Assert.AreEqual(200, response.GetRawResponse().Status);
            var result = response.Value;

            Assert.AreEqual(0, result.Id);
            Assert.AreEqual(item.Title, result.Title);
            Assert.AreEqual(item.Status, result.Status);
            Assert.IsNotNull(result.CreatedAt);
            Assert.IsNotNull(result.UpdatedAt);
            Assert.IsNull(result.CompletedAt);
        }

        [Test]
        public async Task Get()
        {
            // get when not exist we should get a 404
            var exception = Assert.ThrowsAsync<ClientResultException>(async () => await _itemsClient.GetAsync(0));
            Assert.IsNotNull(exception);
            Assert.AreEqual(404, exception.GetRawResponse().Status);

            // create one and then get
            var item = new TodoItem("Buy milk", TodoItemStatus.NotStarted)
            {
                AssignedTo = 1,
                Description = "Need to buy milk from the store",
            };
            var createResponse = await _itemsClient.CreateJsonAsync(item);

            var response = await _itemsClient.GetAsync(createResponse.Value.Id);
            Assert.AreEqual(200, response.GetRawResponse().Status);

            Assert.AreEqual(createResponse.Value.Id, response.Value.Id);
            Assert.AreEqual(item.Title, response.Value.Title);
            Assert.AreEqual(item.Status, response.Value.Status);
            Assert.AreEqual(item.AssignedTo, response.Value.AssignedTo);
            Assert.AreEqual(item.Description, response.Value.Description);
        }

        [Test]
        public async Task Update()
        {
            var item = new TodoItem("Buy milk", TodoItemStatus.NotStarted)
            {
                AssignedTo = 1,
                Description = "Need to buy milk from the store",
            };
            var createResponse = await _itemsClient.CreateJsonAsync(item);
            var patch = new
            {
                title = "Buy milk and eggs",
                status = TodoItemStatus.InProgress.ToString(),
                assignedTo = 2,
                description = "Need to buy milk and eggs from the store",
            };
            var updateResponse = await _itemsClient.UpdateAsync(createResponse.Value.Id, BinaryContent.Create(BinaryData.FromObjectAsJson(patch)));
            Assert.AreEqual(200, updateResponse.GetRawResponse().Status);
            
            using var document = JsonDocument.Parse(updateResponse.GetRawResponse().ContentStream!);
            Assert.AreEqual(patch.title, document.RootElement.GetProperty("title").GetString());
            Assert.AreEqual(patch.status, document.RootElement.GetProperty("status").GetString());
            Assert.AreEqual(patch.assignedTo, document.RootElement.GetProperty("assignedTo").GetInt64());
            Assert.AreEqual(patch.description, document.RootElement.GetProperty("description").GetString());
        }

        [Test]
        public async Task Delete()
        {
            // delete when it does not exist should get a 404
            var exception = Assert.ThrowsAsync<ClientResultException>(async () => await _itemsClient.DeleteAsync(0));
            Assert.IsNotNull(exception);
            Assert.AreEqual(404, exception.GetRawResponse().Status);

            // create one and then delete
            var item = new TodoItem("Buy milk", TodoItemStatus.NotStarted)
            {
                AssignedTo = 1,
                Description = "Need to buy milk from the store",
            };
            var createResponse = await _itemsClient.CreateJsonAsync(item);

            var response = await _itemsClient.DeleteAsync(createResponse.Value.Id);
            Assert.AreEqual(204, response.GetRawResponse().Status);
        }

        [Test]
        public async Task List()
        {
            var response = await _itemsClient.ListAsync();
            Assert.AreEqual(200, response.GetRawResponse().Status);
            Assert.AreEqual(0, response.Value.Items.Count);
            var item = new TodoItem("Buy milk", TodoItemStatus.NotStarted)
            {
                AssignedTo = 1,
                Description = "Need to buy milk from the store",
            };
            await _itemsClient.CreateJsonAsync(item);
            response = await _itemsClient.ListAsync();
            Assert.AreEqual(200, response.GetRawResponse().Status);
            Assert.AreEqual(1, response.Value.Items.Count);
        }
    }
}