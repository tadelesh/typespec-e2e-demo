using Getitdone.Service.Controllers;
using Getitdone.Service.Helpers;
using Getitdone.Service.Models;
using Getitdone.Service;
using Microsoft.AspNetCore.Mvc;

namespace Getitdone.Service.Controllers
{
    [ApiController]
    public partial class CommentsController : CommentsOperationsControllerBase
    {
        internal override ICommentsOperations CommentsOperationsImpl { get; }

        public CommentsController(ICommentsOperations commentsOperations)
        {
            CommentsOperationsImpl = commentsOperations;
        }

        public override async Task<IActionResult> GetComments(string? todoitemId, string? projectId)
        {
            try
            {
                var result = await CommentsOperationsImpl.GetCommentsAsync(todoitemId, projectId);
                return Ok(result);
            }
            catch (Exception ex)
            {
                return ControllerHelpers.HandleErrorResponse(ex);
            }
        }

        public override async Task<IActionResult> CreateComment(CreateCommentRequest body)
        {
            try
            {
                var result = await CommentsOperationsImpl.CreateCommentAsync(body);
                return Created($"/comments/{result.Id}", result);
            }
            catch (Exception ex)
            {
                return ControllerHelpers.HandleErrorResponse(ex);
            }
        }
    }
}