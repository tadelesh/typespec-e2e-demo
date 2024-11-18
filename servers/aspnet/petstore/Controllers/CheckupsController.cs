using Microsoft.AspNetCore.Mvc;

namespace PetStore.Service.Controllers
{
    [ApiController]
    public class CheckupsController : CheckupsControllerBase
    {

        internal override ICheckups CheckupsImpl => new Checkups();

    }
}
