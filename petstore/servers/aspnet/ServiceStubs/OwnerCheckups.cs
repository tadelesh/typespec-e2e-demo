using System;
using System.Collections.Generic;
using System.Threading.Tasks;
using PetStore.Service.Models;

namespace PetStore.Service
{
    public class OwnerCheckups : IOwnerCheckups
    {
        public Task<Checkup> CreateOrUpdateAsync(long ownerId, int checkupId, CheckupUpdate resource)
        {
            throw new NotImplementedException();
        }

        public Task<CheckupCollectionWithNextLink> ListAsync(long ownerId)
        {
            throw new NotImplementedException();
        }
    }
}