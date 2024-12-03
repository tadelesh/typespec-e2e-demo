using Microsoft.AspNetCore.Mvc;
using Microsoft.AspNetCore.Mvc.Filters;
using System.Net;

namespace PetStore.Service
{
    internal class CustomExceptionFilter : IExceptionFilter
    {
        public void OnException(ExceptionContext context)
        {
            switch (context.Exception)
            {
                case PetException ex:
                    context.Result = new JsonResult(ex.Error)
                    {
                        StatusCode = (int)ex.StatusCode
                    };
                    context.ExceptionHandled = true;
                    break;
            }
        }
    }
}
