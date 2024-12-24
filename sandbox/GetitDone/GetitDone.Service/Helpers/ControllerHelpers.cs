using Getitdone.Service.Models;
using Microsoft.AspNetCore.Mvc;
using System.Net;

namespace Getitdone.Service.Helpers
{
    public static class ControllerHelpers
    {
        public static IActionResult HandleErrorResponse(Exception ex)
        {
            var statusCode = ex switch
            {
                KeyNotFoundException => HttpStatusCode.NotFound,
                _ => HttpStatusCode.InternalServerError
            };

            var errorResponse = new ErrorResponse
            {
                Error = ex.Message,
                StatusCode = (int)statusCode
            };

            return new ObjectResult(errorResponse)
            {
                StatusCode = (int)statusCode
            };
        }
    }
}