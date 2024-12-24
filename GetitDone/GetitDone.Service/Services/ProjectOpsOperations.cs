using Getitdone.Service.Models;
using Getitdone.Service.Repositories;
using Getitdone.Service;

namespace Getitdone.Service.Services
{
    public class ProjectOpsOperations : IProjectOpsOperations
    {
        private readonly IProjectRepository _projectRepository;

        public ProjectOpsOperations(IProjectRepository projectRepository)
        {
            _projectRepository = projectRepository;
        }

        public async Task<Project> GetProjectAsync(string projectId)
        {
            try
            {
                var project = await _projectRepository.GetByIdAsync(projectId);
                if (project == null)
                {
                    throw new KeyNotFoundException($"Project with id '{projectId}' not found.");
                }
                return project;
            }
            catch (KeyNotFoundException)
            {
                throw;
            }
            catch (Exception ex)
            {
                // Log the exception
                Console.WriteLine($"Error getting project: {ex.Message}");
                throw;
            }
        }

        public async Task<Project> UpdateProjectAsync(string projectId, UpdateProjectRequest body)
        {
            try
            {
                var existingProject = await _projectRepository.GetByIdAsync(projectId);
                if (existingProject == null)
                {
                    throw new KeyNotFoundException($"Project with id '{projectId}' not found.");
                }

                existingProject.Name = body.Name;
                existingProject.Color = body.Color;
                existingProject.ParentId = body.ParentId;
                existingProject.Order = body.Order ?? existingProject.Order;
                existingProject.IsFavorite = body.IsFavorite ?? existingProject.IsFavorite;

                return await _projectRepository.UpdateAsync(existingProject);
            }
            catch (KeyNotFoundException)
            {
                throw;
            }
            catch (Exception ex)
            {
                // Log the exception
                Console.WriteLine($"Error updating project: {ex.Message}");
                throw;
            }
        }

        public async Task DeleteProjectAsync(string projectId)
        {
            try
            {
                var existingProject = await _projectRepository.GetByIdAsync(projectId);
                if (existingProject == null)
                {
                    throw new KeyNotFoundException($"Project with id '{projectId}' not found.");
                }
                await _projectRepository.DeleteAsync(projectId);
            }
            catch (KeyNotFoundException)
            {
                throw;
            }
            catch (Exception ex)
            {
                // Log the exception
                Console.WriteLine($"Error deleting project: {ex.Message}");
                throw;
            }
        }

        public async Task<Collaborator[]> GetCollaboratorsAsync(string projectId)
        {
            try
            {
                var collaborators = await _projectRepository.GetCollaboratorsAsync(projectId);
                return collaborators.ToArray();
            }
            catch (Exception ex)
            {
                // Log the exception
                Console.WriteLine($"Error getting collaborators: {ex.Message}");
                throw;
            }
        }
    }
}