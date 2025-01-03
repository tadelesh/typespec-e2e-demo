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
    public partial class Comment : IJsonModel<Comment>
    {
        internal Comment()
        {
        }

        void IJsonModel<Comment>.Write(Utf8JsonWriter writer, ModelReaderWriterOptions options)
        {
            writer.WriteStartObject();
            JsonModelWriteCore(writer, options);
            writer.WriteEndObject();
        }

        /// <param name="writer"> The JSON writer. </param>
        /// <param name="options"> The client options for reading and writing models. </param>
        protected virtual void JsonModelWriteCore(Utf8JsonWriter writer, ModelReaderWriterOptions options)
        {
            string format = options.Format == "W" ? ((IPersistableModel<Comment>)this).GetFormatFromOptions(options) : options.Format;
            if (format != "J")
            {
                throw new FormatException($"The model {nameof(Comment)} does not support writing '{format}' format.");
            }
            writer.WritePropertyName("content"u8);
            writer.WriteStringValue(Content);
            writer.WritePropertyName("id"u8);
            writer.WriteStringValue(Id);
            writer.WritePropertyName("posted_at"u8);
            writer.WriteStringValue(PostedAt);
            if (Optional.IsDefined(ProjectId))
            {
                writer.WritePropertyName("project_id"u8);
                writer.WriteStringValue(ProjectId);
            }
            if (Optional.IsDefined(TodoitemId))
            {
                writer.WritePropertyName("todoitem_id"u8);
                writer.WriteStringValue(TodoitemId);
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

        Comment IJsonModel<Comment>.Create(ref Utf8JsonReader reader, ModelReaderWriterOptions options) => JsonModelCreateCore(ref reader, options);

        /// <param name="reader"> The JSON reader. </param>
        /// <param name="options"> The client options for reading and writing models. </param>
        protected virtual Comment JsonModelCreateCore(ref Utf8JsonReader reader, ModelReaderWriterOptions options)
        {
            string format = options.Format == "W" ? ((IPersistableModel<Comment>)this).GetFormatFromOptions(options) : options.Format;
            if (format != "J")
            {
                throw new FormatException($"The model {nameof(Comment)} does not support reading '{format}' format.");
            }
            using JsonDocument document = JsonDocument.ParseValue(ref reader);
            return DeserializeComment(document.RootElement, options);
        }

        internal static Comment DeserializeComment(JsonElement element, ModelReaderWriterOptions options)
        {
            if (element.ValueKind == JsonValueKind.Null)
            {
                return null;
            }
            string content = default;
            string id = default;
            string postedAt = default;
            string projectId = default;
            string todoitemId = default;
            Attachment attachment = default;
            IDictionary<string, BinaryData> additionalBinaryDataProperties = new ChangeTrackingDictionary<string, BinaryData>();
            foreach (var prop in element.EnumerateObject())
            {
                if (prop.NameEquals("content"u8))
                {
                    content = prop.Value.GetString();
                    continue;
                }
                if (prop.NameEquals("id"u8))
                {
                    id = prop.Value.GetString();
                    continue;
                }
                if (prop.NameEquals("posted_at"u8))
                {
                    postedAt = prop.Value.GetString();
                    continue;
                }
                if (prop.NameEquals("project_id"u8))
                {
                    projectId = prop.Value.GetString();
                    continue;
                }
                if (prop.NameEquals("todoitem_id"u8))
                {
                    todoitemId = prop.Value.GetString();
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
            return new Comment(
                content,
                id,
                postedAt,
                projectId,
                todoitemId,
                attachment,
                additionalBinaryDataProperties);
        }

        BinaryData IPersistableModel<Comment>.Write(ModelReaderWriterOptions options) => PersistableModelWriteCore(options);

        /// <param name="options"> The client options for reading and writing models. </param>
        protected virtual BinaryData PersistableModelWriteCore(ModelReaderWriterOptions options)
        {
            string format = options.Format == "W" ? ((IPersistableModel<Comment>)this).GetFormatFromOptions(options) : options.Format;
            switch (format)
            {
                case "J":
                    return ModelReaderWriter.Write(this, options);
                default:
                    throw new FormatException($"The model {nameof(Comment)} does not support writing '{options.Format}' format.");
            }
        }

        Comment IPersistableModel<Comment>.Create(BinaryData data, ModelReaderWriterOptions options) => PersistableModelCreateCore(data, options);

        /// <param name="data"> The data to parse. </param>
        /// <param name="options"> The client options for reading and writing models. </param>
        protected virtual Comment PersistableModelCreateCore(BinaryData data, ModelReaderWriterOptions options)
        {
            string format = options.Format == "W" ? ((IPersistableModel<Comment>)this).GetFormatFromOptions(options) : options.Format;
            switch (format)
            {
                case "J":
                    using (JsonDocument document = JsonDocument.Parse(data))
                    {
                        return DeserializeComment(document.RootElement, options);
                    }
                default:
                    throw new FormatException($"The model {nameof(Comment)} does not support reading '{options.Format}' format.");
            }
        }

        string IPersistableModel<Comment>.GetFormatFromOptions(ModelReaderWriterOptions options) => "J";

        /// <param name="comment"> The <see cref="Comment"/> to serialize into <see cref="BinaryContent"/>. </param>
        public static implicit operator BinaryContent(Comment comment)
        {
            if (comment == null)
            {
                return null;
            }
            return BinaryContent.Create(comment, ModelSerializationExtensions.WireOptions);
        }

        /// <param name="result"> The <see cref="ClientResult"/> to deserialize the <see cref="Comment"/> from. </param>
        public static explicit operator Comment(ClientResult result)
        {
            using PipelineResponse response = result.GetRawResponse();
            using JsonDocument document = JsonDocument.Parse(response.Content);
            return DeserializeComment(document.RootElement, ModelSerializationExtensions.WireOptions);
        }
    }
}
