using Microsoft.AspNetCore.Mvc;

namespace PetStore.Service.Controllers
{
    [ApiController]
    public class OwnerCheckupsController : OwnerCheckupsControllerBase
    {

        internal override IOwnerCheckups OwnerCheckupsImpl => new OwnerCheckups();

    }
}
