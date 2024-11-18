using Microsoft.AspNetCore.Mvc;

namespace PetStore.Service.Controllers
{
    [ApiController]
    public class ToyInsuranceController : ToyInsuranceControllerBase
    {

        internal override IToyInsurance ToyInsuranceImpl => new ToyInsurance();

    }
}
