using System.ClientModel;
using System.ClientModel.Primitives;
using System.Text.Json;
using Todo;
using Todo.Models;

var client = new TodoClient(new Uri("http://localhost:5244"), new ApiKeyCredential("dummy"));

// create a user
var user = await client.GetUsersClient().CreateAsync(new User("John Doe", "test@example.com", "p@ssw0rd"));
Console.WriteLine($"User {user.Value.Id} created");

// try to get a non-exist todo item
try
{
    var todoItem = await client.GetTodoItemsClient().GetAsync(0);
}
catch (ClientResultException ex)
{
    using var errorResponse = JsonDocument.Parse(ex.GetRawResponse()?.ContentStream!);
    Console.WriteLine($"Cannot find todo item, error code: {errorResponse.RootElement.GetProperty("code").GetString()}");
}

var todoItemsClient = client.GetTodoItemsClient();
// create a todo item
Console.WriteLine("create todoItem");
var item = new TodoItem("Buy milk", TodoItemStatus.InProgress)
{
    AssignedTo = 10,
    Description = "Need to buy milk",
};
var createResponse = await todoItemsClient.CreateJsonAsync(item);
Console.WriteLine($"Todo item {createResponse.Value.Id} created");

// get the todo item
Console.WriteLine("retrieve todoItem");
var getResponse = await todoItemsClient.GetAsync(createResponse.Value.Id);
Console.WriteLine($"Todo item {getResponse.Value.Id} retrieved, title: {getResponse.Value.Title}, status: {getResponse.Value.Status}, assignedTo: {getResponse.Value.AssignedTo}, description: {getResponse.Value.Description}");

Console.Write("update todoItem");
var patch = new
{
    title = "Buy milk and bread",
    status = TodoItemStatus.Completed.ToString(),
    assignedTo = 20,
};
var updateResponse = await todoItemsClient.UpdateAsync(getResponse.Value.Id, BinaryContent.Create(BinaryData.FromObjectAsJson(patch)));
var updatedItem = ModelReaderWriter.Read<TodoItem>(BinaryData.FromStream(updateResponse.GetRawResponse().ContentStream!))!;
Console.WriteLine($"Todo item updated, title: {updatedItem.Title}, status: {updatedItem.Status}, assignedTo: {updatedItem.AssignedTo}, description: {updatedItem.Description}");

// list all available todo items
Console.WriteLine("list todoItems");
var listResponse = await todoItemsClient.ListAsync();
foreach (var i in listResponse.Value.Items)
{
    Console.WriteLine($"Item title: {i.Title}, status: {i.Status}");
}

Console.WriteLine("delete item");
await todoItemsClient.DeleteAsync(getResponse.Value.Id);
Console.WriteLine("Item deleted");
