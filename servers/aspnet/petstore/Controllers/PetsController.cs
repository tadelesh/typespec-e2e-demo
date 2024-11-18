using Microsoft.AspNetCore.Mvc;

namespace PetStore.Service.Controllers
{
    [ApiController]
    public class PetsController : PetsControllerBase
    {

        internal override IPets PetsImpl => new Pets();

    }
}
