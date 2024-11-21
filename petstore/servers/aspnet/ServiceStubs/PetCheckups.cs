using System;
using System.Collections.Generic;
using System.Threading.Tasks;
using PetStore.Service.Models;

namespace PetStore.Service
{
    public class PetCheckups : IPetCheckups
    {
        public Task<Checkup> CreateOrUpdateAsync(int petId, int checkupId, CheckupUpdate resource)
        {
            throw new NotImplementedException();
        }

        public Task<CheckupCollectionWithNextLink> ListAsync(int petId)
        {
            throw new NotImplementedException();
        }
    }
}