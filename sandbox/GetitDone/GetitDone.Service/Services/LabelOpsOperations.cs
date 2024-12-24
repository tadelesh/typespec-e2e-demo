using Getitdone.Service.Models;
using Getitdone.Service.Repositories;
using Getitdone.Service;

namespace Getitdone.Service.Services
{
    public class LabelOpsOperations : ILabelOpsOperations
    {
        private readonly ILabelRepository _labelRepository;

        public LabelOpsOperations(ILabelRepository labelRepository)
        {
            _labelRepository = labelRepository;
        }

        public async Task<Label> GetPersonalLabelAsync(string labelId)
        {
            try
            {
                var label = await _labelRepository.GetByIdAsync(labelId);
                if (label == null)
                {
                    throw new KeyNotFoundException($"Label with id '{labelId}' not found.");
                }
                return label;
            }
            catch (KeyNotFoundException)
            {
                throw;
            }
            catch (Exception ex)
            {
                // Log the exception
                Console.WriteLine($"Error getting label: {ex.Message}");
                throw;
            }
        }

        public async Task<Label> UpdateLabelAsync(string labelId, UpdateLabelRequest body)
        {
            try
            {
                var existingLabel = await _labelRepository.GetByIdAsync(labelId);
                if (existingLabel == null)
                {
                    throw new KeyNotFoundException($"Label with id '{labelId}' not found.");
                }

                existingLabel.Name = body.Name;
                existingLabel.Color = body.Color;
                existingLabel.Order = body.Order ?? existingLabel.Order;
                existingLabel.IsFavorite = body.IsFavorite ?? existingLabel.IsFavorite;

                return await _labelRepository.UpdateAsync(existingLabel);
            }
            catch (KeyNotFoundException)
            {
                throw;
            }
            catch (Exception ex)
            {
                // Log the exception
                Console.WriteLine($"Error updating label: {ex.Message}");
                throw;
            }
        }

        public async Task DeleteLabelAsync(string labelId)
        {
            try
            {
                var existingLabel = await _labelRepository.GetByIdAsync(labelId);
                if (existingLabel == null)
                {
                    throw new KeyNotFoundException($"Label with id '{labelId}' not found.");
                }
                await _labelRepository.DeleteAsync(labelId);
            }
            catch (KeyNotFoundException)
            {
                throw;
            }
            catch (Exception ex)
            {
                // Log the exception
                Console.WriteLine($"Error deleting label: {ex.Message}");
                throw;
            }
        }
    }
}