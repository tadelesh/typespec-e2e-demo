using Getitdone.Service.Controllers;
using Getitdone.Service.Models;
using Getitdone.Service.Helpers;
using Getitdone.Service;
using Microsoft.AspNetCore.Mvc;

namespace Getitdone.Service.Controllers
{
    [ApiController]
    public partial class SharedLabelsController : SharedLabelsOperationsControllerBase
    {
        internal override ISharedLabelsOperations SharedLabelsOperationsImpl { get; }

        public SharedLabelsController(ISharedLabelsOperations sharedLabelsOperations)
        {
            SharedLabelsOperationsImpl = sharedLabelsOperations;
        }

        public override async Task<IActionResult> GetSharedLabels()
        {
            try
            {
                var result = await SharedLabelsOperationsImpl.GetSharedLabelsAsync();
                return Ok(result);
            }
            catch (Exception ex)
            {
                return ControllerHelpers.HandleErrorResponse(ex);
            }
        }

        public override async Task<IActionResult> RenameSharedLabel(RenameSharedLabelRequest body)
        {
            try
            {
                await SharedLabelsOperationsImpl.RenameSharedLabelAsync(body);
                return NoContent();
            }
            catch (Exception ex)
            {
                return ControllerHelpers.HandleErrorResponse(ex);
            }
        }

        public override async Task<IActionResult> RemoveSharedLabel(RemoveSharedLabelRequest body)
        {
            try
            {
                await SharedLabelsOperationsImpl.RemoveSharedLabelAsync(body);
                return NoContent();
            }
            catch (Exception ex)
            {
                return ControllerHelpers.HandleErrorResponse(ex);
            }
        }
    }
}