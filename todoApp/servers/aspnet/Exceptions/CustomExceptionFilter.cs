using Microsoft.AspNetCore.Mvc;
using Microsoft.AspNetCore.Mvc.Filters;
using System.Net;

namespace Todo.Exceptions
{
    internal class CustomExceptionFilter : IExceptionFilter
    {
        public void OnException(ExceptionContext context)
        {
            switch (context.Exception)
            {
                case NotFoundException notFound:
                    context.Result = new JsonResult(notFound.Response)
                    {
                        StatusCode = (int)HttpStatusCode.NotFound
                    };
                    context.ExceptionHandled = true;
                    break;
            }
        }
    }
}
