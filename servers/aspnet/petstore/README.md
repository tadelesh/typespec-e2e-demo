# PetStore ASP.NET WebAPI project

The current folder contains Widget ASP.NET core basic project with basic service stub code for out of box run-ability.

If you want to recreate this folder from scratch, please see [steps below.](#steps-to-create)

## Testing the server code

[Follow these steps](../README.md#testing-the-server-code)

## Steps to create the executable server project

If you would like to recreate the server folder from scratch, please follow these steps.

1. First follow the [basic ASP.NET project setup steps](../README.md#steps-to-create-the-executable-server-projects).

1. Add service stub classes to provide service implementation for each of the operations interfaces under `generated/operations`. We placed them under `ServiceStubs` folder but you are free to organize your actual server code.

1. Create `Controllers` folder and add controller classes `XXXServiceController.cs`. These bare bone controller extends emitter ControllerBase code and links to the service stub code in previous step.

    ```csharp
    using Microsoft.AspNetCore.Mvc;
    
    // Replace `XXX` with the name of the controller
    namespace PetStore.Service.Controllers
    {
        [ApiController]
        public class `XXX`Controller : `XXX`ControllerBase
        {
            internal override I`XXX` `XXX`Impl => new `XXX`();
        }
    }
    ```
