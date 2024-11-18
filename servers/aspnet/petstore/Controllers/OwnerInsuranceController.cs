using Microsoft.AspNetCore.Mvc;

namespace PetStore.Service.Controllers
{
    [ApiController]
    public class OwnerInsuranceController : OwnerInsuranceControllerBase
    {

        internal override IOwnerInsurance OwnerInsuranceImpl => new OwnerInsurance();

    }
}
