using Getitdone.Service.Models;
using Getitdone.Service.Repositories;
using Getitdone.Service;

namespace Getitdone.Service.Services
{
    public class ProjectsOperations : IProjectsOperations
    {
        private readonly IProjectRepository _projectRepository;

        public ProjectsOperations(IProjectRepository projectRepository)
        {
            _projectRepository = projectRepository;
        }

        public async Task<Project[]> GetProjectsAsync()
        {
            try
            {
                var projects = await _projectRepository.GetAllAsync();
                return projects.ToArray();
            }
            catch (Exception ex)
            {
                // Log the exception
                Console.WriteLine($"Error getting projects: {ex.Message}");
                throw;
            }
        }

        public async Task<Project> CreateProjectAsync(CreateProjectRequest body)
        {
            try
            {
                var newProject = new Project
                {
                    Id = Guid.NewGuid().ToString(),
                    Name = body.Name,
                    Color = body.Color,
                    ParentId = body.ParentId,
                    Order = body.Order ?? 0,
                    IsFavorite = body.IsFavorite ?? false
                };

                return await _projectRepository.AddAsync(newProject);
            }
            catch (Exception ex)
            {
                // Log the exception
                Console.WriteLine($"Error creating project: {ex.Message}");
                throw;
            }
        }
    }
}