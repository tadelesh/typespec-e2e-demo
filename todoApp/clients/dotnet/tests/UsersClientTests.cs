using System.ClientModel;
using Todo.Models;

namespace Todo.Tests
{
    public class UsersClientTests
    {
        private Users _usersClient;

        [OneTimeSetUp]
        public void Setup()
        {
            var cred = new ApiKeyCredential("stub");
            _usersClient = new TodoClient(new Uri("http://localhost:5244"), cred).GetUsersClient();
        }

        [Test]
        public async Task CreateUser()
        {
            var user = new User("John Doe", "test@dummy.com", "p@ssw0rd");
            var response = await _usersClient.CreateAsync(user);

            Assert.AreEqual(200, response.GetRawResponse().Status);
            var result = response.Value;

            Assert.AreEqual(0, result.Id);
            Assert.AreEqual(user.Username, result.Username);
            Assert.AreEqual(user.Email, result.Email);
            Assert.IsNotNull(result.Token);
        }
    }
}