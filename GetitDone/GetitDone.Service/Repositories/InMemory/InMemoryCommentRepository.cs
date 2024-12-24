using System.Collections.Concurrent;
using Getitdone.Service.Models;

namespace Getitdone.Service.Repositories.InMemory
{
    public class InMemoryCommentRepository : ICommentRepository
    {
        private readonly ConcurrentDictionary<string, Comment> _comments = new();

        public Task<Comment?> GetByIdAsync(string id)
        {
            _comments.TryGetValue(id, out var comment);
            return Task.FromResult(comment);
        }

        public Task<IEnumerable<Comment>> GetAllAsync(string? todoitemId, string? projectId)
        {
            var filteredComments = _comments.Values.Where(c =>
                (todoitemId == null || c.TodoitemId == todoitemId) &&
                (projectId == null || c.ProjectId == projectId));
            return Task.FromResult(filteredComments);
        }

        public Task<Comment> AddAsync(Comment comment)
        {
            _comments.TryAdd(comment.Id, comment);
            return Task.FromResult(comment);
        }

        public Task<Comment> UpdateAsync(Comment comment)
        {
            _comments.TryUpdate(comment.Id, comment, _comments[comment.Id]);
            return Task.FromResult(comment);
        }

        public Task DeleteAsync(string id)
        {
            _comments.TryRemove(id, out _);
            return Task.CompletedTask;
        }
    }
}