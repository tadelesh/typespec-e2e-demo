using System.Collections.Concurrent;
using Getitdone.Service.Models;

namespace Getitdone.Service.Repositories.InMemory
{
    public class InMemoryTodoItemRepository : ITodoItemRepository
    {
        private readonly ConcurrentDictionary<string, TodoItem> _todoItems = new();

        public Task<TodoItem?> GetByIdAsync(string id)
        {
            _todoItems.TryGetValue(id, out var todoItem);
            return Task.FromResult(todoItem);
        }

        public Task<IEnumerable<TodoItem>> GetAllAsync()
        {
            return Task.FromResult<IEnumerable<TodoItem>>(_todoItems.Values);
        }

        public Task<TodoItem> AddAsync(TodoItem todoItem)
        {
            _todoItems.TryAdd(todoItem.Id, todoItem);
            return Task.FromResult(todoItem);
        }

        public Task<TodoItem> UpdateAsync(TodoItem todoItem)
        {
            _todoItems.TryUpdate(todoItem.Id, todoItem, _todoItems[todoItem.Id]);
            return Task.FromResult(todoItem);
        }

        public Task DeleteAsync(string id)
        {
            _todoItems.TryRemove(id, out _);
            return Task.CompletedTask;
        }
    }
}