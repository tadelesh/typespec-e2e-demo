using System.Collections.Generic;
using System.Threading.Tasks;
using PetStore.Service.Models;

namespace PetStore.Service
{
    public class PetInsurance : IPetInsurance
    {
        private readonly Dictionary<int, Insurance> _policies = new Dictionary<int, Insurance>();

        public Task<Insurance> GetAsync(int petId)
        {
            throw new NotImplementedException();
        }

        public Task<Insurance> UpdateAsync(int petId, InsuranceUpdate properties)
        {
            throw new NotImplementedException();
        }
    }
}