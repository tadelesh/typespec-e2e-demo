using Getitdone.Service.Models;

namespace Getitdone.Service.Repositories
{
    public interface ISectionRepository
    {
        Task<Section?> GetByIdAsync(string id);
        Task<IEnumerable<Section>> GetAllAsync(string projectId);
        Task<Section> AddAsync(Section section);
        Task<Section> UpdateAsync(Section section);
        Task DeleteAsync(string id);
    }
}