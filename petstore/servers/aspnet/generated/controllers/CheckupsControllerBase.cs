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
    public abstract partial class CheckupsControllerBase : ControllerBase
    {

        internal abstract ICheckups CheckupsImpl { get; }

        ///<summary>
        /// Creates or update an instance of the resource.
        ///</summary>
        [HttpPatch]
        [Route("/checkups/{checkupId}")]
        [ProducesResponseType((int)HttpStatusCode.OK, Type = typeof(Checkup))]
        [ProducesResponseType((int)HttpStatusCode.Created, Type = typeof(Checkup))]
        public virtual async Task<IActionResult> CreateOrUpdate(int checkupId, CheckupUpdate body)
        {
            var result = await CheckupsImpl.CreateOrUpdateAsync(checkupId, body);
            return Ok(result);
        }

        ///<summary>
        /// Lists all instances of the resource.
        ///</summary>
        [HttpGet]
        [Route("/checkups")]
        [ProducesResponseType((int)HttpStatusCode.OK, Type = typeof(CheckupCollectionWithNextLink))]
        public virtual async Task<IActionResult> List()
        {
            var result = await CheckupsImpl.ListAsync();
            return Ok(result);
        }

    }
}
