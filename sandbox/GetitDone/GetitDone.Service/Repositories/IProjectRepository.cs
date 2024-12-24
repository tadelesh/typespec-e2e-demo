using Getitdone.Service.Models;

namespace Getitdone.Service.Repositories
{
    public interface IProjectRepository
    {
        Task<Project?> GetByIdAsync(string id);
        Task<IEnumerable<Project>> GetAllAsync();
        Task<Project> AddAsync(Project project);
        Task<Project> UpdateAsync(Project project);
        Task DeleteAsync(string id);
        Task<IEnumerable<Collaborator>> GetCollaboratorsAsync(string projectId);
    }
}