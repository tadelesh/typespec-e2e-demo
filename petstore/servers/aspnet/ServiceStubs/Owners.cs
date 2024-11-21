using System;
using System.Collections.Generic;
using System.Threading.Tasks;
using PetStore.Service.Models;

namespace PetStore.Service
{
    public class Owners : IOwners
    {
        private readonly Dictionary<int, Owner> _owners = new Dictionary<int, Owner>();

        public Task<Owner> CreateAsync(OwnerCreate resource)
        {
            throw new NotImplementedException();
        }

        public Task DeleteAsync(long ownerId)
        {
            throw new NotImplementedException();
        }

        public Task<Owner> GetAsync(long ownerId)
        {
            throw new NotImplementedException();
        }

        public Task<OwnerCollectionWithNextLink> ListAsync()
        {
            throw new NotImplementedException();
        }

        public Task<Owner> UpdateAsync(long ownerId, OwnerUpdate properties)
        {
            throw new NotImplementedException();
        }
    }
}