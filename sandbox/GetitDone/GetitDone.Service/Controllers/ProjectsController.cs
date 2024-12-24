using Getitdone.Service.Controllers;
using Getitdone.Service.Helpers;
using Getitdone.Service.Models;
using Getitdone.Service;
using Microsoft.AspNetCore.Mvc;

namespace Getitdone.Service.Controllers
{
    [ApiController]
    public partial class ProjectsController : ProjectsOperationsControllerBase
    {
        internal override IProjectsOperations ProjectsOperationsImpl { get; }

        public ProjectsController(IProjectsOperations projectsOperations)
        {
            ProjectsOperationsImpl = projectsOperations;
        }

        public override async Task<IActionResult> GetProjects()
        {
            try
            {
                var result = await ProjectsOperationsImpl.GetProjectsAsync();
                return Ok(result);
            }
            catch (Exception ex)
            {
                return ControllerHelpers.HandleErrorResponse(ex);
            }
        }

        public override async Task<IActionResult> CreateProject(CreateProjectRequest body)
        {
            try
            {
                var result = await ProjectsOperationsImpl.CreateProjectAsync(body);
                return Created($"/projects/{result.Id}", result);
            }
            catch (Exception ex)
            {
                return ControllerHelpers.HandleErrorResponse(ex);
            }
        }
    }
}