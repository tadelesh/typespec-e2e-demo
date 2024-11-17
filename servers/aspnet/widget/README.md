# Widget ASP.NET WebAPI project

The current folder contains Widget ASP.NET core basic project with basic service stub code for out of box run-ability.

If you want to recreate this folder from scratch, please see [steps below.](#steps-to-create)

## Testing the server code

[Follow these steps](../README.md#testing-the-server-code)

## Steps to create the executable server project

If you would like to recreate the server folder from scratch, please follow these steps.

1. First follow the [basic ASP.NET project setup steps](../README.md#steps-to-create-the-executable-server-projects).

1. Create `Controllers` folder and add concrete controller class `WidgetServiceController.cs`. This bare bone controller extends generated base controller and instantiate service implementation.

    ```csharp
    using Microsoft.AspNetCore.Mvc;
    
    namespace DemoService.Service.Controllers
    {
        [ApiController]
        public class WidgetServiceController : WidgetServiceControllerBase
        {
            static WidgetService serviceImpl = new WidgetService();
            internal override IWidgetService WidgetServiceImpl => serviceImpl;
        }
    }
    ```

1. Add `WidgetService.cs` to provide a simple in-memory data store service implementation for each of the operations.

    ```csharp
    using DemoService.Service.Models;
    
    namespace DemoService.Service
    {
        public class WidgetService : IWidgetService
        {
            internal static Dictionary<string, Widget> _store = new Dictionary<string, Widget> {
                { "1", new Widget {Id="1", Weight=10, Color= "red"} },
                { "2",  new Widget {Id="2", Weight=20, Color= "green"} },
                { "3",  new Widget {Id="3", Weight=30, Color= "yellow"} },
            };
            public Task<Widget> GetAsync(string id)
            {
                if (_store.ContainsKey(id))
                {
                    return Task.FromResult(_store[id]);
                }
                else
                {
                    throw new Exception("Widget not found");
                }
            }
            public Task<Widget> UpdateAsync(string id, WidgetUpdate properties)
            {
                if (_store.ContainsKey(id))
                {
                    var widget = _store[id];
                    widget.Weight = properties.Weight??0;
                    widget.Color = properties.Color??"unknown";
                    return Task.FromResult(_store[id]);
                }
                else
                {
                    throw new Exception("Widget not found");
                }
            }
            public Task DeleteAsync(string id)
            {
                if (_store.ContainsKey(id))
                {
                    _store.Remove(id);
                    return Task.CompletedTask;
                }
                else
                {
                    throw new Exception("Widget not found");
                }
            }
            public Task<Widget> CreateAsync(WidgetCreate resource)
            {
                var newId = (_store.Count + 1).ToString();
                _store.Add(newId, new Widget { Id = newId, Weight = resource.Weight, Color = resource.Color });
                return Task.FromResult(_store[newId]);
            }
            public Task<WidgetCollectionWithNextLink> ListAsync()
            {
                return Task.FromResult(new WidgetCollectionWithNextLink { Value = _store.Values.ToArray() });
            }
            public Task<Widget> CustomGetAsync()
            {
                throw new NotImplementedException();
            }
        }
    }
    
    ```
