// Copyright (c) Microsoft Corporation. All rights reserved.
// Licensed under the MIT License.
// <auto-generated />

using System;
using System.Net;
using System.Threading.Tasks;
using System.Text.Json;
using System.Text.Json.Serialization;
using Microsoft.AspNetCore.Mvc;
using Todo.Service.Models;
using Todo.Service;

namespace Todo.Service.Controllers
{
    [ApiController]
    public abstract partial class AttachmentsOperationsControllerBase : ControllerBase
    {

        internal abstract IAttachmentsOperations AttachmentsOperationsImpl { get; }


        [HttpGet]
        [Route("/items/{itemId}/attachments")]
        [ProducesResponseType((int)HttpStatusCode.OK, Type = typeof(Placeholder))]
        public virtual async Task<IActionResult> List(long itemId)
        {
            var result = await AttachmentsOperationsImpl.ListAsync(itemId);
            return Ok(result);
        }


        [HttpPost]
        [Route("/items/{itemId}/attachments")]
        [ProducesResponseType((int)HttpStatusCode.NoContent, Type = typeof(void))]
        public virtual async Task<IActionResult> CreateJsonAttachment([FromHeader(Name = "Content-Type")] string contentType = "application/json", long itemId, TodoAttachment body)
        {
            await AttachmentsOperationsImpl.CreateJsonAttachmentAsync(contentType, itemId, body);
            return Ok();
        }


        [HttpPost]
        [Route("/items/{itemId}/attachments")]
        [ProducesResponseType((int)HttpStatusCode.NoContent, Type = typeof(void))]
        public virtual async Task<IActionResult> CreateFileAttachment([FromHeader(Name = "Content-Type")] string contentType = "multipart/form-data", long itemId, FileAttachmentMultipartRequest body)
        {
            await AttachmentsOperationsImpl.CreateFileAttachmentAsync(contentType, itemId, body);
            return Ok();
        }

    }
}
