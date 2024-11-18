using System.Collections.Generic;
using System.Threading.Tasks;
using PetStore.Service.Models;

namespace PetStore.Service
{
    public class ToyInsurance : IToyInsurance
    {
        private readonly Dictionary<int, Insurance> _policies = new Dictionary<int, Insurance>();

        public Task<Insurance> GetAsync(int petId, long toyId)
        {
            throw new NotImplementedException();
        }

        public Task<Insurance> UpdateAsync(int petId, long toyId, InsuranceUpdate properties)
        {
            throw new NotImplementedException();
        }
    }
}