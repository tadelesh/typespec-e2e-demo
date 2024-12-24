using Getitdone.Service.Controllers;
using Getitdone.Service.Helpers;
using Getitdone.Service.Models;
using Getitdone.Service;
using Microsoft.AspNetCore.Mvc;

namespace Getitdone.Service.Controllers
{
    [ApiController]
    public partial class SectionsController : SectionsOperationsControllerBase
    {
        internal override ISectionsOperations SectionsOperationsImpl { get; }

        public SectionsController(ISectionsOperations sectionsOperations)
        {
            SectionsOperationsImpl = sectionsOperations;
        }

        public override async Task<IActionResult> GetSections(string projectId)
        {
            try
            {
                var result = await SectionsOperationsImpl.GetSectionsAsync(projectId);
                return Ok(result);
            }
            catch (Exception ex)
            {
                return ControllerHelpers.HandleErrorResponse(ex);
            }
        }

        public override async Task<IActionResult> CreateSection(CreateSectionRequest body)
        {
            try
            {
                var result = await SectionsOperationsImpl.CreateSectionAsync(body);
                return Created($"/sections/{result.Id}", result);
            }
            catch (Exception ex)
            {
                return ControllerHelpers.HandleErrorResponse(ex);
            }
        }
    }
}