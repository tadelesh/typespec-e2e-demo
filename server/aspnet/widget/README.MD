# Widget ASP.NET WebAPI project

The current folder contains Widget ASP.NET core basic project with basic service stub code for out of box run-ability.

If you want to recreate this folder from scratch, please see [steps below.](#steps-to-create)

## Testing the server code

1. Compile TypeSpec under `/specifications/widget` with `npx tsp compile
1. Build and run Asp.net server project
1. Test the server via http://localhost:[PORT]/swagger/index.html

## Steps to create the executable server project

This folder was created from scratch with following steps.

1. Create an `ASP.NET Core Web API` project with following command:

    ```dotnetcli
       dotnet new webapi --use-controllers
    ```

2. Run following command to add Swagger endpoint to project for easy testing

    ```dotnetcli
       dotnet add package Swashbuckle.AspNetCore
    ```

3. Replace content of `Program.cs` with code below:

    ```csharp
        var builder = WebApplication.CreateBuilder(args);
        
        builder.Services.AddControllers();
        builder.Services.AddEndpointsApiExplorer();
        builder.Services.AddSwaggerGen();
        
        var app = builder.Build();
        
        // Configure the HTTP request pipeline.
        if (app.Environment.IsDevelopment())
        {
            app.UseSwagger();
            app.UseSwaggerUI();
        }
        
        app.UseAuthorization();
        app.MapControllers();
        
        app.Run();
    ```

4. Create `Controllers` folder and add concrete controller class `WidgetServiceController.cs`. This bare bone controller extends generated base controller and instantiate service implementation.

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

5. Add `WidgetService.cs` to provide a simple in-memory data store service implementation for each of the operations.

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