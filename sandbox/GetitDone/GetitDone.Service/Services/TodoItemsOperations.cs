using Getitdone.Service.Models;
using Getitdone.Service.Repositories;
using Getitdone.Service;

namespace Getitdone.Service.Services
{
    public class TodoItemsOperations : ITodoItemsOperations
    {
        private readonly ITodoItemRepository _todoItemRepository;

        public TodoItemsOperations(ITodoItemRepository todoItemRepository)
        {
            _todoItemRepository = todoItemRepository;
        }

        public async Task<TodoItem[]> GetTodoItemsAsync()
        {
            try
            {
                var todoItems = await _todoItemRepository.GetAllAsync();
                return todoItems.ToArray();
            }
            catch (Exception ex)
            {
                // Log the exception
                Console.WriteLine($"Error getting todo items: {ex.Message}");
                throw;
            }
        }

        public async Task<TodoItem> CreateTodoItemAsync(CreateTodoItemRequest body)
        {
            try
            {
                var newTodoItem = new TodoItem
                {
                    Id = Guid.NewGuid().ToString(),
                    Content = body.Content,
                    Description = body.Description,
                    Due = body.Due,
                    Labels = body.Labels,
                    Priority = body.Priority ?? 0,
                    ParentId = body.ParentId,
                    Order = body.Order ?? 0,
                    ProjectId = body.ProjectId,
                    SectionId = body.SectionId,
                    AssigneeId = body.AssigneeId,
                    CreatedAt = DateTime.UtcNow.ToString("o")
                };

                return await _todoItemRepository.AddAsync(newTodoItem);
            }
            catch (Exception ex)
            {
                // Log the exception
                Console.WriteLine($"Error creating todo item: {ex.Message}");
                throw;
            }
        }
    }
}