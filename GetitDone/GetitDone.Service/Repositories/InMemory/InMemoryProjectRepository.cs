using System.Collections.Concurrent;
using Getitdone.Service.Models;

namespace Getitdone.Service.Repositories.InMemory
{
    public class InMemoryProjectRepository : IProjectRepository
    {
        private readonly ConcurrentDictionary<string, Project> _projects = new();
        private readonly ConcurrentDictionary<string, List<Collaborator>> _collaborators = new();

        public Task<Project?> GetByIdAsync(string id)
        {
            _projects.TryGetValue(id, out var project);
            return Task.FromResult(project);
        }

        public Task<IEnumerable<Project>> GetAllAsync()
        {
            return Task.FromResult<IEnumerable<Project>>(_projects.Values);
        }

        public Task<Project> AddAsync(Project project)
        {
            _projects.TryAdd(project.Id, project);
            _collaborators.TryAdd(project.Id, new List<Collaborator>());
            return Task.FromResult(project);
        }

        public Task<Project> UpdateAsync(Project project)
        {
            _projects.TryUpdate(project.Id, project, _projects[project.Id]);
            return Task.FromResult(project);
        }

        public Task DeleteAsync(string id)
        {
            _projects.TryRemove(id, out _);
            _collaborators.TryRemove(id, out _);
            return Task.CompletedTask;
        }

        public Task<IEnumerable<Collaborator>> GetCollaboratorsAsync(string projectId)
        {
            _collaborators.TryGetValue(projectId, out var collaborators);
            return Task.FromResult<IEnumerable<Collaborator>>(collaborators ?? Enumerable.Empty<Collaborator>());
        }
    }
}