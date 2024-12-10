using PetStore.Service.Models;
using System.Net;

namespace PetStore.Service
{
    public class Pets : IPets
    {
        public Task<Pet> CreateAsync(PetCreate resource)
        {
            return Task.FromResult(new Pet()
            {
                Id = 0,
                Age = resource.Age,
                Name = resource.Name,
                OwnerId = resource.OwnerId,
                Tag = resource.Tag
            });
        }

        public Task DeleteAsync(int petId)
        {
            ValidatePetId(petId);
            return Task.CompletedTask;
        }

        public Task<Pet> GetAsync(int petId)
        {
            ValidatePetId(petId);
            return Task.FromResult(new Pet { Id = petId, Age = 5, Name = "Kiwi", OwnerId = 5 });
        }

        public Task<PetCollectionWithNextLink> ListAsync()
        {
            return Task.FromResult(new PetCollectionWithNextLink()
            {
                Value = [
                    new Pet { Id = 1, Age = 5, Name = "Kiwi", OwnerId = 5 },
                    new Pet { Id = 2, Age = 6, Name = "Coco", OwnerId = 6 },
                ]
            });
        }

        public Task<Pet> UpdateAsync(int petId, PetUpdate properties)
        {
            ValidatePetId(petId);
            return Task.FromResult(new Pet()
            {
                Id = petId,
                Age = properties.Age ?? 0,
                Name = properties.Name,
                OwnerId = properties.OwnerId ?? 0,
                Tag = properties.Tag
            });
        }

        private void ValidatePetId(int petId)
        {
            if (petId < 0)
            {
                throw new PetException(HttpStatusCode.BadRequest, new PetStoreError()
                {
                    Code = 0,
                    Message = "Invalid petId"
                });
            }
            if (petId > 10)
            {
                throw new PetException(HttpStatusCode.NotFound, new PetStoreError()
                {
                    Code = 1,
                    Message = "Pet not found"
                });
            }
        }
    }
}