using Getitdone.Service.Models;
using Getitdone.Service.Repositories;
using Getitdone.Service;

namespace Getitdone.Service.Services
{
    public class LabelsOperations : ILabelsOperations
    {
        private readonly ILabelRepository _labelRepository;

        public LabelsOperations(ILabelRepository labelRepository)
        {
            _labelRepository = labelRepository;
        }

        public async Task<Label[]> GetPersonalLabelsAsync()
        {
            try
            {
                var labels = await _labelRepository.GetAllAsync();
                return labels.ToArray();
            }
            catch (Exception ex)
            {
                // Log the exception
                Console.WriteLine($"Error getting labels: {ex.Message}");
                throw;
            }
        }

        public async Task<Label> CreateLabelAsync(CreateLabelRequest body)
        {
            try
            {
                var newLabel = new Label
                {
                    Id = Guid.NewGuid().ToString(),
                    Name = body.Name,
                    Color = body.Color,
                    Order = body.Order ?? 0,
                    IsFavorite = body.IsFavorite ?? false
                };

                return await _labelRepository.AddAsync(newLabel);
            }
            catch (Exception ex)
            {
                // Log the exception
                Console.WriteLine($"Error creating label: {ex.Message}");
                throw;
            }
        }
    }
}