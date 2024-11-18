using Microsoft.AspNetCore.Mvc;

namespace PetStore.Service.Controllers
{
    [ApiController]
    public class PetCheckupsController : PetCheckupsControllerBase
    {

        internal override IPetCheckups PetCheckupsImpl => new PetCheckups();

    }
}
