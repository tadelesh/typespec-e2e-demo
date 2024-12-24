using Getitdone.Service.Models;

namespace Getitdone.Service.Repositories
{
    public interface ITodoItemRepository
    {
        Task<TodoItem?> GetByIdAsync(string id);
        Task<IEnumerable<TodoItem>> GetAllAsync();
        Task<TodoItem> AddAsync(TodoItem todoItem);
        Task<TodoItem> UpdateAsync(TodoItem todoItem);
        Task DeleteAsync(string id);
    }
}