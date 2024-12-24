using Getitdone.Service.Models;
using Getitdone.Service.Repositories;
using Getitdone.Service;

namespace Getitdone.Service.Services
{
    public class SectionsOperations : ISectionsOperations
    {
        private readonly ISectionRepository _sectionRepository;

        public SectionsOperations(ISectionRepository sectionRepository)
        {
            _sectionRepository = sectionRepository;
        }

        public async Task<Section[]> GetSectionsAsync(string projectId)
        {
            try
            {
                var sections = await _sectionRepository.GetAllAsync(projectId);
                return sections.ToArray();
            }
            catch (Exception ex)
            {
                // Log the exception
                Console.WriteLine($"Error getting sections: {ex.Message}");
                throw;
            }
        }

        public async Task<Section> CreateSectionAsync(CreateSectionRequest body)
        {
            try
            {
                var newSection = new Section
                {
                    Id = Guid.NewGuid().ToString(),
                    Name = body.Name,
                    ProjectId = body.ProjectId,
                    Order = body.Order ?? 0
                };

                return await _sectionRepository.AddAsync(newSection);
            }
            catch (Exception ex)
            {
                // Log the exception
                Console.WriteLine($"Error creating section: {ex.Message}");
                throw;
            }
        }
    }
}