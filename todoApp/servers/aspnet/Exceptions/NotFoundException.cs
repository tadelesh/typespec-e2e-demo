using Todo.Service.Models;

namespace Todo.Exceptions
{
    internal class NotFoundException : Exception
    {
        public NotFoundErrorResponse Response { get; }
        public NotFoundException(NotFoundErrorResponse response)
        {
            Response = response;
        }
    }
}
