using Getitdone.Service.Models;

namespace Getitdone.Service.Repositories
{
    public interface ILabelRepository
    {
        Task<Label?> GetByIdAsync(string id);
        Task<IEnumerable<Label>> GetAllAsync();
        Task<Label> AddAsync(Label label);
        Task<Label> UpdateAsync(Label label);
        Task DeleteAsync(string id);
    }
}