using Getitdone.Service.Models;
using Getitdone.Service.Repositories;
using Getitdone.Service;

namespace Getitdone.Service.Services
{
    public class SharedLabelsOperations : ISharedLabelsOperations
    {
        private readonly ILabelRepository _labelRepository;

        public SharedLabelsOperations(ILabelRepository labelRepository)
        {
            _labelRepository = labelRepository;
        }

        public async Task<Label[]> GetSharedLabelsAsync()
        {
            try
            {
                var labels = await _labelRepository.GetAllAsync();
                // In a real app, you'd filter these by some shared criteria
                return labels.ToArray();
            }
            catch (Exception ex)
            {
                // Log the exception
                Console.WriteLine($"Error getting shared labels: {ex.Message}");
                throw;
            }
        }

        public async Task RenameSharedLabelAsync(RenameSharedLabelRequest body)
        {
            try
            {
                var existingLabel = (await _labelRepository.GetAllAsync()).FirstOrDefault(l => l.Name == body.Name);
                if (existingLabel == null)
                {
                    throw new KeyNotFoundException($"Shared label with name '{body.Name}' not found.");
                }

                existingLabel.Name = body.NewName;
                await _labelRepository.UpdateAsync(existingLabel);
            }
            catch (KeyNotFoundException)
            {
                throw;
            }
            catch (Exception ex)
            {
                // Log the exception
                Console.WriteLine($"Error renaming shared label: {ex.Message}");
                throw;
            }
        }

        public async Task RemoveSharedLabelAsync(RemoveSharedLabelRequest body)
        {
            try
            {
                var existingLabel = (await _labelRepository.GetAllAsync()).FirstOrDefault(l => l.Name == body.Name);
                if (existingLabel == null)
                {
                    throw new KeyNotFoundException($"Shared label with name '{body.Name}' not found.");
                }
                await _labelRepository.DeleteAsync(existingLabel.Id);
            }
            catch (KeyNotFoundException)
            {
                throw;
            }
            catch (Exception ex)
            {
                // Log the exception
                Console.WriteLine($"Error removing shared label: {ex.Message}");
                throw;
            }
        }
    }
}