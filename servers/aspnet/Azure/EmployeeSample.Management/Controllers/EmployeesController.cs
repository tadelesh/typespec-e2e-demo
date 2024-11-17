using Microsoft.AspNetCore.Mvc;

namespace Microsoft.ContosoProviderHub.Service.Controllers
{
    [ApiController]
    public class EmployeesController : EmployeesControllerBase
    {
        internal override IEmployees EmployeesImpl => new IEmployees
        {
            // GetAsync = return new Employee { Name = "JohnDoe", Properties = new EmployeeProperties { Age = 30, City = "Redmond, WA", ProvisioningState = "Succeeded" } },
            GetAsync = throw new System.NotImplementedException(),
            CreateOrUpdateAsync = throw new System.NotImplementedException(),
            UpdateAsync = throw new System.NotImplementedException(),
            DeleteAsync = throw new System.NotImplementedException(),
            ListByResourceGroupAsync = throw new System.NotImplementedException(),
            ListBySubscriptionAsync = throw new System.NotImplementedException(),
            MoveAsync = throw new System.NotImplementedException(),
            CheckExistenceAsync = throw new System.NotImplementedException(),
        };
    }
}