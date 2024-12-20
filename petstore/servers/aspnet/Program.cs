using Microsoft.AspNetCore.Mvc;
using PetStore.Service;
using PetStore.Service.Models;
using System.Net;

var builder = WebApplication.CreateBuilder(args);

builder.Services.AddControllers(options =>
{
    options.Filters.Add(new CustomExceptionFilter());
}).ConfigureApiBehaviorOptions(options =>
{
    options.InvalidModelStateResponseFactory = HandleInvalidModelStateResponse;
});
builder.Services.AddEndpointsApiExplorer();
builder.Services.AddSwaggerGen();

var app = builder.Build();

// Configure the HTTP request pipeline.
if (app.Environment.IsDevelopment())
{
    app.UseSwagger();
    app.UseSwaggerUI(c =>
    {
        c.DocumentTitle = "TypeSpec Generated OpenAPI Viewer";
        c.SwaggerEndpoint("/openapi.yaml", "TypeSpec Generated OpenAPI Docs");
        c.RoutePrefix = "swagger";
    });
}
app.MapGet("/openapi.yaml", async (HttpContext context) =>
{
    var externalFilePath = "../../openapi/openapi.yaml"; // Full path to the file outside the project
    if (!File.Exists(externalFilePath))
    {
        context.Response.StatusCode = StatusCodes.Status404NotFound;
        await context.Response.WriteAsync("OpenAPI spec not found.");
        return;
    }
    context.Response.ContentType = "application/json";
    await context.Response.SendFileAsync(externalFilePath);
});

app.UseAuthorization();
app.MapControllers();

app.Run();

static IActionResult HandleInvalidModelStateResponse(ActionContext context)
{
    var errors = context.ModelState
        .Where(e => e.Value != null && e.Value.Errors.Count > 0)
        .Select(e => string.Join(',', e.Value.Errors.Select(x => x.ErrorMessage)));
    return new JsonResult(new PetStoreError()
    {
        Code = (int)HttpStatusCode.BadRequest,
        Message = string.Join('\n', errors)
    })
    {
        StatusCode = (int)HttpStatusCode.BadRequest
    };
}