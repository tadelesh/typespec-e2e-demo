// Copyright (c) Microsoft Corporation. All rights reserved.
// Licensed under the MIT License.
// <auto-generated />

using System;
using System.Net;
using System.Threading.Tasks;
using System.Text.Json;
using System.Text.Json.Serialization;
using Microsoft.AspNetCore.Mvc;
using PetStore.Service.Models;
using PetStore.Service;

namespace PetStore.Service.Controllers
{
    [ApiController]
    public abstract partial class OwnerCheckupsControllerBase : ControllerBase
    {

        internal abstract IOwnerCheckups OwnerCheckupsImpl { get; }

        ///<summary>
        /// Creates or update an instance of the extension resource.
        ///</summary>
        [HttpPatch]
        [Route("/owners/{ownerId}/checkups/{checkupId}")]
        [ProducesResponseType((int)HttpStatusCode.OK, Type = typeof(Checkup))]
        [ProducesResponseType((int)HttpStatusCode.Created, Type = typeof(Checkup))]
        public virtual async Task<IActionResult> CreateOrUpdate(long ownerId, int checkupId, CheckupUpdate body)
        {
            var result = await OwnerCheckupsImpl.CreateOrUpdateAsync(ownerId, checkupId, body);
            return Ok(result);
        }

        ///<summary>
        /// Lists all instances of the extension resource.
        ///</summary>
        [HttpGet]
        [Route("/owners/{ownerId}/checkups")]
        [ProducesResponseType((int)HttpStatusCode.OK, Type = typeof(CheckupCollectionWithNextLink))]
        public virtual async Task<IActionResult> List(long ownerId)
        {
            var result = await OwnerCheckupsImpl.ListAsync(ownerId);
            return Ok(result);
        }

    }
}
