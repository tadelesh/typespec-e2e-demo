// <auto-generated/>

#nullable disable

using System;
using System.ClientModel;
using System.ClientModel.Primitives;
using System.Collections.Generic;
using System.Text.Json;
using Getitdone;

namespace Getitdone.Models
{
    /// <summary></summary>
    public partial class CreateCommentRequest : IJsonModel<CreateCommentRequest>
    {
        internal CreateCommentRequest()
        {
        }

        void IJsonModel<CreateCommentRequest>.Write(Utf8JsonWriter writer, ModelReaderWriterOptions options)
        {
            writer.WriteStartObject();
            JsonModelWriteCore(writer, options);
            writer.WriteEndObject();
        }

        /// <param name="writer"> The JSON writer. </param>
        /// <param name="options"> The client options for reading and writing models. </param>
        protected virtual void JsonModelWriteCore(Utf8JsonWriter writer, ModelReaderWriterOptions options)
        {
            string format = options.Format == "W" ? ((IPersistableModel<CreateCommentRequest>)this).GetFormatFromOptions(options) : options.Format;
            if (format != "J")
            {
                throw new FormatException($"The model {nameof(CreateCommentRequest)} does not support writing '{format}' format.");
            }
            writer.WritePropertyName("content"u8);
            writer.WriteStringValue(Content);
            if (Optional.IsDefined(TodoitemId))
            {
                writer.WritePropertyName("todoitem_id"u8);
                writer.WriteStringValue(TodoitemId);
            }
            if (Optional.IsDefined(ProjectId))
            {
                writer.WritePropertyName("project_id"u8);
                writer.WriteStringValue(ProjectId);
            }
            if (Optional.IsDefined(Attachment))
            {
                writer.WritePropertyName("attachment"u8);
                writer.WriteObjectValue(Attachment, options);
            }
            if (options.Format != "W" && _additionalBinaryDataProperties != null)
            {
                foreach (var item in _additionalBinaryDataProperties)
                {
                    writer.WritePropertyName(item.Key);
#if NET6_0_OR_GREATER
                    writer.WriteRawValue(item.Value);
#else
                    using (JsonDocument document = JsonDocument.Parse(item.Value))
                    {
                        JsonSerializer.Serialize(writer, document.RootElement);
                    }
#endif
                }
            }
        }

        CreateCommentRequest IJsonModel<CreateCommentRequest>.Create(ref Utf8JsonReader reader, ModelReaderWriterOptions options) => JsonModelCreateCore(ref reader, options);

        /// <param name="reader"> The JSON reader. </param>
        /// <param name="options"> The client options for reading and writing models. </param>
        protected virtual CreateCommentRequest JsonModelCreateCore(ref Utf8JsonReader reader, ModelReaderWriterOptions options)
        {
            string format = options.Format == "W" ? ((IPersistableModel<CreateCommentRequest>)this).GetFormatFromOptions(options) : options.Format;
            if (format != "J")
            {
                throw new FormatException($"The model {nameof(CreateCommentRequest)} does not support reading '{format}' format.");
            }
            using JsonDocument document = JsonDocument.ParseValue(ref reader);
            return DeserializeCreateCommentRequest(document.RootElement, options);
        }

        internal static CreateCommentRequest DeserializeCreateCommentRequest(JsonElement element, ModelReaderWriterOptions options)
        {
            if (element.ValueKind == JsonValueKind.Null)
            {
                return null;
            }
            string content = default;
            string todoitemId = default;
            string projectId = default;
            Attachment attachment = default;
            IDictionary<string, BinaryData> additionalBinaryDataProperties = new ChangeTrackingDictionary<string, BinaryData>();
            foreach (var prop in element.EnumerateObject())
            {
                if (prop.NameEquals("content"u8))
                {
                    content = prop.Value.GetString();
                    continue;
                }
                if (prop.NameEquals("todoitem_id"u8))
                {
                    todoitemId = prop.Value.GetString();
                    continue;
                }
                if (prop.NameEquals("project_id"u8))
                {
                    projectId = prop.Value.GetString();
                    continue;
                }
                if (prop.NameEquals("attachment"u8))
                {
                    if (prop.Value.ValueKind == JsonValueKind.Null)
                    {
                        continue;
                    }
                    attachment = Attachment.DeserializeAttachment(prop.Value, options);
                    continue;
                }
                if (options.Format != "W")
                {
                    additionalBinaryDataProperties.Add(prop.Name, BinaryData.FromString(prop.Value.GetRawText()));
                }
            }
            return new CreateCommentRequest(content, todoitemId, projectId, attachment, additionalBinaryDataProperties);
        }

        BinaryData IPersistableModel<CreateCommentRequest>.Write(ModelReaderWriterOptions options) => PersistableModelWriteCore(options);

        /// <param name="options"> The client options for reading and writing models. </param>
        protected virtual BinaryData PersistableModelWriteCore(ModelReaderWriterOptions options)
        {
            string format = options.Format == "W" ? ((IPersistableModel<CreateCommentRequest>)this).GetFormatFromOptions(options) : options.Format;
            switch (format)
            {
                case "J":
                    return ModelReaderWriter.Write(this, options);
                default:
                    throw new FormatException($"The model {nameof(CreateCommentRequest)} does not support writing '{options.Format}' format.");
            }
        }

        CreateCommentRequest IPersistableModel<CreateCommentRequest>.Create(BinaryData data, ModelReaderWriterOptions options) => PersistableModelCreateCore(data, options);

        /// <param name="data"> The data to parse. </param>
        /// <param name="options"> The client options for reading and writing models. </param>
        protected virtual CreateCommentRequest PersistableModelCreateCore(BinaryData data, ModelReaderWriterOptions options)
        {
            string format = options.Format == "W" ? ((IPersistableModel<CreateCommentRequest>)this).GetFormatFromOptions(options) : options.Format;
            switch (format)
            {
                case "J":
                    using (JsonDocument document = JsonDocument.Parse(data))
                    {
                        return DeserializeCreateCommentRequest(document.RootElement, options);
                    }
                default:
                    throw new FormatException($"The model {nameof(CreateCommentRequest)} does not support reading '{options.Format}' format.");
            }
        }

        string IPersistableModel<CreateCommentRequest>.GetFormatFromOptions(ModelReaderWriterOptions options) => "J";

        /// <param name="createCommentRequest"> The <see cref="CreateCommentRequest"/> to serialize into <see cref="BinaryContent"/>. </param>
        public static implicit operator BinaryContent(CreateCommentRequest createCommentRequest)
        {
            if (createCommentRequest == null)
            {
                return null;
            }
            return BinaryContent.Create(createCommentRequest, ModelSerializationExtensions.WireOptions);
        }

        /// <param name="result"> The <see cref="ClientResult"/> to deserialize the <see cref="CreateCommentRequest"/> from. </param>
        public static explicit operator CreateCommentRequest(ClientResult result)
        {
            using PipelineResponse response = result.GetRawResponse();
            using JsonDocument document = JsonDocument.Parse(response.Content);
            return DeserializeCreateCommentRequest(document.RootElement, ModelSerializationExtensions.WireOptions);
        }
    }
}
