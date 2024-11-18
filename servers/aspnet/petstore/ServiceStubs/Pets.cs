using System;
using System.Collections.Generic;
using System.Threading.Tasks;
using PetStore.Service.Models;

namespace PetStore.Service
{
    public class Pets : IPets
    {
        public Task<Pet> CreateAsync(PetCreate resource)
        {
            throw new NotImplementedException();
        }

        public Task DeleteAsync(int petId)
        {
            throw new NotImplementedException();
        }

        public Task<Pet> GetAsync(int petId)
        {
            return Task.FromResult(new Pet { Id = petId, Age = 5, Name = "Kiwi", OwnerId = 5 });
        }

        public Task<PetCollectionWithNextLink> ListAsync()
        {
            throw new NotImplementedException();
        }

        public Task<Pet> UpdateAsync(int petId, PetUpdate properties)
        {
            throw new NotImplementedException();
        }
    }
}