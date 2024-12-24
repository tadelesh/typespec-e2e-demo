using System.Collections.Concurrent;
using Getitdone.Service.Models;

namespace Getitdone.Service.Repositories.InMemory
{
    public class InMemorySectionRepository : ISectionRepository
    {
        private readonly ConcurrentDictionary<string, Section> _sections = new();

        public Task<Section?> GetByIdAsync(string id)
        {
            _sections.TryGetValue(id, out var section);
            return Task.FromResult(section);
        }

        public Task<IEnumerable<Section>> GetAllAsync(string projectId)
        {
            return Task.FromResult<IEnumerable<Section>>(_sections.Values.Where(s => s.ProjectId == projectId));
        }

        public Task<Section> AddAsync(Section section)
        {
            _sections.TryAdd(section.Id, section);
            return Task.FromResult(section);
        }

        public Task<Section> UpdateAsync(Section section)
        {
            _sections.TryUpdate(section.Id, section, _sections[section.Id]);
            return Task.FromResult(section);
        }

        public Task DeleteAsync(string id)
        {
            _sections.TryRemove(id, out _);
            return Task.CompletedTask;
        }
    }
}