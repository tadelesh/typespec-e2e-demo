using PetStore.Service.Models;
using System.Net;

namespace PetStore.Service
{
    public class PetException : Exception
    {
        public PetException(HttpStatusCode code, PetStoreError error)
        {
            StatusCode = code;
            Error = error;
        }

        public HttpStatusCode StatusCode { get; }

        public PetStoreError Error { get; }
    }
}
