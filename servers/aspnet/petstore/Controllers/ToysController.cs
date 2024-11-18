using Microsoft.AspNetCore.Mvc;

namespace PetStore.Service.Controllers
{
    [ApiController]
    public class ToysController : ToysControllerBase
    {

        internal override IToys ToysImpl => new Toys();

    }
}
