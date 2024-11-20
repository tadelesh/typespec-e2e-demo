using Microsoft.AspNetCore.Mvc;

namespace PetStore.Service.Controllers
{
    [ApiController]
    public class OwnersController : OwnersControllerBase
    {

        internal override IOwners OwnersImpl => new Owners();

    }
}
