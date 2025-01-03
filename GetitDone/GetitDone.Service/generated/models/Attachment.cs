// Copyright (c) Microsoft Corporation. All rights reserved.
// Licensed under the MIT License.
// <auto-generated />

using System;
using System.Text.Json;
using System.Text.Json.Serialization;

namespace Getitdone.Service.Models
{

    public partial class Attachment
    {
        [JsonPropertyName("file_name")]
        public string FileName { get; set; }

        [JsonPropertyName("file_type")]
        public string FileType { get; set; }

        [JsonPropertyName("file_url")]
        public string FileUrl { get; set; }

        [JsonPropertyName("resource_type")]
        public string ResourceType { get; set; }


    }
}
