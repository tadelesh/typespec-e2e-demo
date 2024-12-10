using Microsoft.AspNetCore.Mvc;
using PetStore.Service.Models;

namespace PetStore.Service.Controllers
{
    [ApiController]
    public class PetsController : PetsControllerBase
    {
        internal override IPets PetsImpl => new Pets();
    }
}
