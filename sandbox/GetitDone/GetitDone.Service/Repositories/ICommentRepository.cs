using Getitdone.Service.Models;

namespace Getitdone.Service.Repositories
{
    public interface ICommentRepository
    {
        Task<Comment?> GetByIdAsync(string id);
        Task<IEnumerable<Comment>> GetAllAsync(string? todoitemId, string? projectId);
        Task<Comment> AddAsync(Comment comment);
        Task<Comment> UpdateAsync(Comment comment);
        Task DeleteAsync(string id);
    }
}