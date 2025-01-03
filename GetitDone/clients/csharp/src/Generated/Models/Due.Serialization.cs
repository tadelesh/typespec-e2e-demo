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
    public partial class Due : IJsonModel<Due>
    {
        internal Due()
        {
        }

        void IJsonModel<Due>.Write(Utf8JsonWriter writer, ModelReaderWriterOptions options)
        {
            writer.WriteStartObject();
            JsonModelWriteCore(writer, options);
            writer.WriteEndObject();
        }

        /// <param name="writer"> The JSON writer. </param>
        /// <param name="options"> The client options for reading and writing models. </param>
        protected virtual void JsonModelWriteCore(Utf8JsonWriter writer, ModelReaderWriterOptions options)
        {
            string format = options.Format == "W" ? ((IPersistableModel<Due>)this).GetFormatFromOptions(options) : options.Format;
            if (format != "J")
            {
                throw new FormatException($"The model {nameof(Due)} does not support writing '{format}' format.");
            }
            writer.WritePropertyName("date"u8);
            writer.WriteStringValue(Date);
            writer.WritePropertyName("is_recurring"u8);
            writer.WriteBooleanValue(IsRecurring);
            if (Optional.IsDefined(Datetime))
            {
                writer.WritePropertyName("datetime"u8);
                writer.WriteStringValue(Datetime);
            }
            writer.WritePropertyName("string"u8);
            writer.WriteStringValue(String);
            if (Optional.IsDefined(Timezone))
            {
                writer.WritePropertyName("timezone"u8);
                writer.WriteStringValue(Timezone);
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

        Due IJsonModel<Due>.Create(ref Utf8JsonReader reader, ModelReaderWriterOptions options) => JsonModelCreateCore(ref reader, options);

        /// <param name="reader"> The JSON reader. </param>
        /// <param name="options"> The client options for reading and writing models. </param>
        protected virtual Due JsonModelCreateCore(ref Utf8JsonReader reader, ModelReaderWriterOptions options)
        {
            string format = options.Format == "W" ? ((IPersistableModel<Due>)this).GetFormatFromOptions(options) : options.Format;
            if (format != "J")
            {
                throw new FormatException($"The model {nameof(Due)} does not support reading '{format}' format.");
            }
            using JsonDocument document = JsonDocument.ParseValue(ref reader);
            return DeserializeDue(document.RootElement, options);
        }

        internal static Due DeserializeDue(JsonElement element, ModelReaderWriterOptions options)
        {
            if (element.ValueKind == JsonValueKind.Null)
            {
                return null;
            }
            string date = default;
            bool isRecurring = default;
            string datetime = default;
            string @string = default;
            string timezone = default;
            IDictionary<string, BinaryData> additionalBinaryDataProperties = new ChangeTrackingDictionary<string, BinaryData>();
            foreach (var prop in element.EnumerateObject())
            {
                if (prop.NameEquals("date"u8))
                {
                    date = prop.Value.GetString();
                    continue;
                }
                if (prop.NameEquals("is_recurring"u8))
                {
                    isRecurring = prop.Value.GetBoolean();
                    continue;
                }
                if (prop.NameEquals("datetime"u8))
                {
                    datetime = prop.Value.GetString();
                    continue;
                }
                if (prop.NameEquals("string"u8))
                {
                    @string = prop.Value.GetString();
                    continue;
                }
                if (prop.NameEquals("timezone"u8))
                {
                    timezone = prop.Value.GetString();
                    continue;
                }
                if (options.Format != "W")
                {
                    additionalBinaryDataProperties.Add(prop.Name, BinaryData.FromString(prop.Value.GetRawText()));
                }
            }
            return new Due(
                date,
                isRecurring,
                datetime,
                @string,
                timezone,
                additionalBinaryDataProperties);
        }

        BinaryData IPersistableModel<Due>.Write(ModelReaderWriterOptions options) => PersistableModelWriteCore(options);

        /// <param name="options"> The client options for reading and writing models. </param>
        protected virtual BinaryData PersistableModelWriteCore(ModelReaderWriterOptions options)
        {
            string format = options.Format == "W" ? ((IPersistableModel<Due>)this).GetFormatFromOptions(options) : options.Format;
            switch (format)
            {
                case "J":
                    return ModelReaderWriter.Write(this, options);
                default:
                    throw new FormatException($"The model {nameof(Due)} does not support writing '{options.Format}' format.");
            }
        }

        Due IPersistableModel<Due>.Create(BinaryData data, ModelReaderWriterOptions options) => PersistableModelCreateCore(data, options);

        /// <param name="data"> The data to parse. </param>
        /// <param name="options"> The client options for reading and writing models. </param>
        protected virtual Due PersistableModelCreateCore(BinaryData data, ModelReaderWriterOptions options)
        {
            string format = options.Format == "W" ? ((IPersistableModel<Due>)this).GetFormatFromOptions(options) : options.Format;
            switch (format)
            {
                case "J":
                    using (JsonDocument document = JsonDocument.Parse(data))
                    {
                        return DeserializeDue(document.RootElement, options);
                    }
                default:
                    throw new FormatException($"The model {nameof(Due)} does not support reading '{options.Format}' format.");
            }
        }

        string IPersistableModel<Due>.GetFormatFromOptions(ModelReaderWriterOptions options) => "J";

        /// <param name="due"> The <see cref="Due"/> to serialize into <see cref="BinaryContent"/>. </param>
        public static implicit operator BinaryContent(Due due)
        {
            if (due == null)
            {
                return null;
            }
            return BinaryContent.Create(due, ModelSerializationExtensions.WireOptions);
        }

        /// <param name="result"> The <see cref="ClientResult"/> to deserialize the <see cref="Due"/> from. </param>
        public static explicit operator Due(ClientResult result)
        {
            using PipelineResponse response = result.GetRawResponse();
            using JsonDocument document = JsonDocument.Parse(response.Content);
            return DeserializeDue(document.RootElement, ModelSerializationExtensions.WireOptions);
        }
    }
}
