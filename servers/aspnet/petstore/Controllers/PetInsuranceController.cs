using Microsoft.AspNetCore.Mvc;

namespace PetStore.Service.Controllers
{
    [ApiController]
    public class PetInsuranceController : PetInsuranceControllerBase
    {

        internal override IPetInsurance PetInsuranceImpl => new PetInsurance();

    }
}
