// <auto-generated/>

#nullable disable

using System;
using System.ClientModel;
using System.ClientModel.Primitives;
using System.Collections.Generic;
using System.Text.Json;
using Todo;

namespace Todo.Models
{
    /// <summary></summary>
    public partial class TodoFileAttachment : IJsonModel<TodoFileAttachment>
    {
        internal TodoFileAttachment()
        {
        }

        void IJsonModel<TodoFileAttachment>.Write(Utf8JsonWriter writer, ModelReaderWriterOptions options)
        {
            writer.WriteStartObject();
            JsonModelWriteCore(writer, options);
            writer.WriteEndObject();
        }

        /// <param name="writer"> The JSON writer. </param>
        /// <param name="options"> The client options for reading and writing models. </param>
        protected virtual void JsonModelWriteCore(Utf8JsonWriter writer, ModelReaderWriterOptions options)
        {
            string format = options.Format == "W" ? ((IPersistableModel<TodoFileAttachment>)this).GetFormatFromOptions(options) : options.Format;
            if (format != "J")
            {
                throw new FormatException($"The model {nameof(TodoFileAttachment)} does not support writing '{format}' format.");
            }
            writer.WritePropertyName("filename"u8);
            writer.WriteStringValue(Filename);
            writer.WritePropertyName("mediaType"u8);
            writer.WriteStringValue(MediaType);
            writer.WritePropertyName("contents"u8);
            writer.WriteBase64StringValue(Contents.ToArray(), "D");
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

        TodoFileAttachment IJsonModel<TodoFileAttachment>.Create(ref Utf8JsonReader reader, ModelReaderWriterOptions options) => JsonModelCreateCore(ref reader, options);

        /// <param name="reader"> The JSON reader. </param>
        /// <param name="options"> The client options for reading and writing models. </param>
        protected virtual TodoFileAttachment JsonModelCreateCore(ref Utf8JsonReader reader, ModelReaderWriterOptions options)
        {
            string format = options.Format == "W" ? ((IPersistableModel<TodoFileAttachment>)this).GetFormatFromOptions(options) : options.Format;
            if (format != "J")
            {
                throw new FormatException($"The model {nameof(TodoFileAttachment)} does not support reading '{format}' format.");
            }
            using JsonDocument document = JsonDocument.ParseValue(ref reader);
            return DeserializeTodoFileAttachment(document.RootElement, options);
        }

        internal static TodoFileAttachment DeserializeTodoFileAttachment(JsonElement element, ModelReaderWriterOptions options)
        {
            if (element.ValueKind == JsonValueKind.Null)
            {
                return null;
            }
            string filename = default;
            string mediaType = default;
            BinaryData contents = default;
            IDictionary<string, BinaryData> additionalBinaryDataProperties = new ChangeTrackingDictionary<string, BinaryData>();
            foreach (var prop in element.EnumerateObject())
            {
                if (prop.NameEquals("filename"u8))
                {
                    filename = prop.Value.GetString();
                    continue;
                }
                if (prop.NameEquals("mediaType"u8))
                {
                    mediaType = prop.Value.GetString();
                    continue;
                }
                if (prop.NameEquals("contents"u8))
                {
                    contents = BinaryData.FromBytes(prop.Value.GetBytesFromBase64("D"));
                    continue;
                }
                if (options.Format != "W")
                {
                    additionalBinaryDataProperties.Add(prop.Name, BinaryData.FromString(prop.Value.GetRawText()));
                }
            }
            return new TodoFileAttachment(filename, mediaType, contents, additionalBinaryDataProperties);
        }

        BinaryData IPersistableModel<TodoFileAttachment>.Write(ModelReaderWriterOptions options) => PersistableModelWriteCore(options);

        /// <param name="options"> The client options for reading and writing models. </param>
        protected virtual BinaryData PersistableModelWriteCore(ModelReaderWriterOptions options)
        {
            string format = options.Format == "W" ? ((IPersistableModel<TodoFileAttachment>)this).GetFormatFromOptions(options) : options.Format;
            switch (format)
            {
                case "J":
                    return ModelReaderWriter.Write(this, options);
                default:
                    throw new FormatException($"The model {nameof(TodoFileAttachment)} does not support writing '{options.Format}' format.");
            }
        }

        TodoFileAttachment IPersistableModel<TodoFileAttachment>.Create(BinaryData data, ModelReaderWriterOptions options) => PersistableModelCreateCore(data, options);

        /// <param name="data"> The data to parse. </param>
        /// <param name="options"> The client options for reading and writing models. </param>
        protected virtual TodoFileAttachment PersistableModelCreateCore(BinaryData data, ModelReaderWriterOptions options)
        {
            string format = options.Format == "W" ? ((IPersistableModel<TodoFileAttachment>)this).GetFormatFromOptions(options) : options.Format;
            switch (format)
            {
                case "J":
                    using (JsonDocument document = JsonDocument.Parse(data))
                    {
                        return DeserializeTodoFileAttachment(document.RootElement, options);
                    }
                default:
                    throw new FormatException($"The model {nameof(TodoFileAttachment)} does not support reading '{options.Format}' format.");
            }
        }

        string IPersistableModel<TodoFileAttachment>.GetFormatFromOptions(ModelReaderWriterOptions options) => "J";

        /// <param name="todoFileAttachment"> The <see cref="TodoFileAttachment"/> to serialize into <see cref="BinaryContent"/>. </param>
        public static implicit operator BinaryContent(TodoFileAttachment todoFileAttachment)
        {
            if (todoFileAttachment == null)
            {
                return null;
            }
            return BinaryContent.Create(todoFileAttachment, ModelSerializationExtensions.WireOptions);
        }

        /// <param name="result"> The <see cref="ClientResult"/> to deserialize the <see cref="TodoFileAttachment"/> from. </param>
        public static explicit operator TodoFileAttachment(ClientResult result)
        {
            using PipelineResponse response = result.GetRawResponse();
            using JsonDocument document = JsonDocument.Parse(response.Content);
            return DeserializeTodoFileAttachment(document.RootElement, ModelSerializationExtensions.WireOptions);
        }
    }
}
