using System.Collections.Concurrent;
using Getitdone.Service.Models;

namespace Getitdone.Service.Repositories.InMemory
{
    public class InMemoryLabelRepository : ILabelRepository
    {
        private readonly ConcurrentDictionary<string, Label> _labels = new();

        public Task<Label?> GetByIdAsync(string id)
        {
            _labels.TryGetValue(id, out var label);
            return Task.FromResult(label);
        }

        public Task<IEnumerable<Label>> GetAllAsync()
        {
            return Task.FromResult<IEnumerable<Label>>(_labels.Values);
        }

        public Task<Label> AddAsync(Label label)
        {
            _labels.TryAdd(label.Id, label);
            return Task.FromResult(label);
        }

        public Task<Label> UpdateAsync(Label label)
        {
            _labels.TryUpdate(label.Id, label, _labels[label.Id]);
            return Task.FromResult(label);
        }

        public Task DeleteAsync(string id)
        {
            _labels.TryRemove(id, out _);
            return Task.CompletedTask;
        }
    }
}