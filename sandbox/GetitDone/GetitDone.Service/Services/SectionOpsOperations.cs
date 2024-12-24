using Getitdone.Service.Models;
using Getitdone.Service.Repositories;
using Getitdone.Service;

namespace Getitdone.Service.Services
{
    public class SectionOpsOperations : ISectionOpsOperations
    {
        private readonly ISectionRepository _sectionRepository;

        public SectionOpsOperations(ISectionRepository sectionRepository)
        {
            _sectionRepository = sectionRepository;
        }

        public async Task<Section> GetSectionAsync(string sectionId)
        {
            try
            {
                var section = await _sectionRepository.GetByIdAsync(sectionId);
                if (section == null)
                {
                    throw new KeyNotFoundException($"Section with id '{sectionId}' not found.");
                }
                return section;
            }
            catch (KeyNotFoundException)
            {
                throw;
            }
            catch (Exception ex)
            {
                // Log the exception
                Console.WriteLine($"Error getting section: {ex.Message}");
                throw;
            }
        }

        public async Task<Section> UpdateSectionAsync(string sectionId, UpdateSectionRequest body)
        {
            try
            {
                var existingSection = await _sectionRepository.GetByIdAsync(sectionId);
                if (existingSection == null)
                {
                    throw new KeyNotFoundException($"Section with id '{sectionId}' not found.");
                }

                existingSection.Name = body.Name;
                existingSection.Order = body.Order ?? existingSection.Order;

                return await _sectionRepository.UpdateAsync(existingSection);
            }
            catch (KeyNotFoundException)
            {
                throw;
            }
            catch (Exception ex)
            {
                // Log the exception
                Console.WriteLine($"Error updating section: {ex.Message}");
                throw;
            }
        }

        public async Task DeleteSectionAsync(string sectionId)
        {
            try
            {
                var existingSection = await _sectionRepository.GetByIdAsync(sectionId);
                if (existingSection == null)
                {
                    throw new KeyNotFoundException($"Section with id '{sectionId}' not found.");
                }
                await _sectionRepository.DeleteAsync(sectionId);
            }
            catch (KeyNotFoundException)
            {
                throw;
            }
            catch (Exception ex)
            {
                // Log the exception
                Console.WriteLine($"Error deleting section: {ex.Message}");
                throw;
            }
        }
    }
}