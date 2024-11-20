using System;
using System.Collections.Generic;
using System.Threading.Tasks;
using PetStore.Service.Models;

namespace PetStore.Service
{
    public class Toys : IToys
    {
        private readonly Dictionary<int, Toy> _toys = new Dictionary<int, Toy>();

        public Task<Toy> GetAsync(int petId, long toyId)
        {
            throw new NotImplementedException();
        }

        public Task<ToyCollectionWithNextLink> ListAsync(int petId, string nameFilter)
        {
            throw new NotImplementedException();
        }
    }

}