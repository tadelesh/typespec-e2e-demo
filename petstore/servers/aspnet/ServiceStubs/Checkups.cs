using System;
using System.Collections.Generic;
using System.Threading.Tasks;
using PetStore.Service.Models;

namespace PetStore.Service
{
    public class Checkups : ICheckups
    {
        public Task<Checkup> CreateOrUpdateAsync(int checkupId, CheckupUpdate resource)
        {
            throw new NotImplementedException();
        }

        public Task<CheckupCollectionWithNextLink> ListAsync()
        {
            throw new NotImplementedException();
        }
    }
}