using System.Collections.Generic;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Http.HttpResults;
using PetStore.Service.Models;

namespace PetStore.Service
{
    public class OwnerInsurance : IOwnerInsurance
    {
        public Task<Insurance> GetAsync(long ownerId)
        {
            throw new NotImplementedException();
        }

        public Task<Insurance> UpdateAsync(long ownerId, InsuranceUpdate properties)
        {
            throw new NotImplementedException();
        }
    }
}