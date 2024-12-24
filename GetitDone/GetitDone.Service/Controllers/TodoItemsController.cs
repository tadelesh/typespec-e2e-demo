using Getitdone.Service.Controllers;
using Getitdone.Service.Helpers;
using Getitdone.Service.Models;
using Getitdone.Service;
using Microsoft.AspNetCore.Mvc;

namespace Getitdone.Service.Controllers
{
    [ApiController]
    public partial class TodoItemsController : TodoItemsOperationsControllerBase
    {
        internal override ITodoItemsOperations TodoItemsOperationsImpl { get; }

        public TodoItemsController(ITodoItemsOperations todoItemsOperations)
        {
            TodoItemsOperationsImpl = todoItemsOperations;
        }

        public override async Task<IActionResult> GetTodoItems()
        {
            try
            {
                var result = await TodoItemsOperationsImpl.GetTodoItemsAsync();
                return Ok(result);
            }
            catch (Exception ex)
            {
                return ControllerHelpers.HandleErrorResponse(ex);
            }
        }

        public override async Task<IActionResult> CreateTodoItem(CreateTodoItemRequest body)
        {
            try
            {
                var result = await TodoItemsOperationsImpl.CreateTodoItemAsync(body);
                return Created($"/todoitems/{result.Id}", result);
            }
            catch (Exception ex)
            {
                return ControllerHelpers.HandleErrorResponse(ex);
            }
        }
    }
}