// <auto-generated/>

#nullable disable

using System;
using System.ClientModel;
using System.ClientModel.Primitives;
using System.Collections.Generic;
using System.Text.Json;
using System.Threading;
using System.Threading.Tasks;
using Getitdone.Models;

namespace Getitdone
{
    /// <summary></summary>
    public partial class LabelsSharedLabels
    {
        private readonly Uri _endpoint;

        /// <summary> Initializes a new instance of LabelsSharedLabels for mocking. </summary>
        protected LabelsSharedLabels()
        {
        }

        internal LabelsSharedLabels(ClientPipeline pipeline, Uri endpoint)
        {
            _endpoint = endpoint;
            Pipeline = pipeline;
        }

        /// <summary> The HTTP pipeline for sending and receiving REST requests and responses. </summary>
        public ClientPipeline Pipeline { get; }

        /// <summary>
        /// [Protocol Method] getSharedLabels
        /// <list type="bullet">
        /// <item>
        /// <description> This <see href="https://aka.ms/azsdk/net/protocol-methods">protocol method</see> allows explicit creation of the request and processing of the response for advanced scenarios. </description>
        /// </item>
        /// </list>
        /// </summary>
        /// <param name="options"> The request options, which can override default behaviors of the client pipeline on a per-call basis. </param>
        /// <exception cref="ClientResultException"> Service returned a non-success status code. </exception>
        /// <returns> The response returned from the service. </returns>
        public virtual ClientResult GetSharedLabels(RequestOptions options)
        {
            using PipelineMessage message = CreateGetSharedLabelsRequest(options);
            return ClientResult.FromResponse(Pipeline.ProcessMessage(message, options));
        }

        /// <summary>
        /// [Protocol Method] getSharedLabels
        /// <list type="bullet">
        /// <item>
        /// <description> This <see href="https://aka.ms/azsdk/net/protocol-methods">protocol method</see> allows explicit creation of the request and processing of the response for advanced scenarios. </description>
        /// </item>
        /// </list>
        /// </summary>
        /// <param name="options"> The request options, which can override default behaviors of the client pipeline on a per-call basis. </param>
        /// <exception cref="ClientResultException"> Service returned a non-success status code. </exception>
        /// <returns> The response returned from the service. </returns>
        public virtual async Task<ClientResult> GetSharedLabelsAsync(RequestOptions options)
        {
            using PipelineMessage message = CreateGetSharedLabelsRequest(options);
            return ClientResult.FromResponse(await Pipeline.ProcessMessageAsync(message, options).ConfigureAwait(false));
        }

        /// <summary> getSharedLabels. </summary>
        /// <param name="cancellationToken"> The cancellation token that can be used to cancel the operation. </param>
        /// <exception cref="ClientResultException"> Service returned a non-success status code. </exception>
        public virtual ClientResult<IList<Label>> GetSharedLabels(CancellationToken cancellationToken = default)
        {
            ClientResult result = GetSharedLabels(cancellationToken.CanBeCanceled ? new RequestOptions { CancellationToken = cancellationToken } : null);
            IList<Label> value = new List<Label>();
            using JsonDocument document = JsonDocument.Parse(result.GetRawResponse().ContentStream);
            foreach (var item in document.RootElement.EnumerateArray())
            {
                value.Add(Label.DeserializeLabel(item, ModelSerializationExtensions.WireOptions));
            }
            return ClientResult.FromValue(value, result.GetRawResponse());
        }

        /// <summary> getSharedLabels. </summary>
        /// <param name="cancellationToken"> The cancellation token that can be used to cancel the operation. </param>
        /// <exception cref="ClientResultException"> Service returned a non-success status code. </exception>
        public virtual async Task<ClientResult<IList<Label>>> GetSharedLabelsAsync(CancellationToken cancellationToken = default)
        {
            ClientResult result = await GetSharedLabelsAsync(cancellationToken.CanBeCanceled ? new RequestOptions { CancellationToken = cancellationToken } : null).ConfigureAwait(false);
            IList<Label> value = new List<Label>();
            using JsonDocument document = await JsonDocument.ParseAsync(result.GetRawResponse().ContentStream, default, default).ConfigureAwait(false);
            foreach (var item in document.RootElement.EnumerateArray())
            {
                value.Add(Label.DeserializeLabel(item, ModelSerializationExtensions.WireOptions));
            }
            return ClientResult.FromValue(value, result.GetRawResponse());
        }

        /// <summary>
        /// [Protocol Method] renameSharedLabel
        /// <list type="bullet">
        /// <item>
        /// <description> This <see href="https://aka.ms/azsdk/net/protocol-methods">protocol method</see> allows explicit creation of the request and processing of the response for advanced scenarios. </description>
        /// </item>
        /// </list>
        /// </summary>
        /// <param name="content"> The content to send as the body of the request. </param>
        /// <param name="options"> The request options, which can override default behaviors of the client pipeline on a per-call basis. </param>
        /// <exception cref="ArgumentNullException"> <paramref name="content"/> is null. </exception>
        /// <exception cref="ClientResultException"> Service returned a non-success status code. </exception>
        /// <returns> The response returned from the service. </returns>
        public virtual ClientResult RenameSharedLabel(BinaryContent content, RequestOptions options = null)
        {
            Argument.AssertNotNull(content, nameof(content));

            using PipelineMessage message = CreateRenameSharedLabelRequest(content, options);
            return ClientResult.FromResponse(Pipeline.ProcessMessage(message, options));
        }

        /// <summary>
        /// [Protocol Method] renameSharedLabel
        /// <list type="bullet">
        /// <item>
        /// <description> This <see href="https://aka.ms/azsdk/net/protocol-methods">protocol method</see> allows explicit creation of the request and processing of the response for advanced scenarios. </description>
        /// </item>
        /// </list>
        /// </summary>
        /// <param name="content"> The content to send as the body of the request. </param>
        /// <param name="options"> The request options, which can override default behaviors of the client pipeline on a per-call basis. </param>
        /// <exception cref="ArgumentNullException"> <paramref name="content"/> is null. </exception>
        /// <exception cref="ClientResultException"> Service returned a non-success status code. </exception>
        /// <returns> The response returned from the service. </returns>
        public virtual async Task<ClientResult> RenameSharedLabelAsync(BinaryContent content, RequestOptions options = null)
        {
            Argument.AssertNotNull(content, nameof(content));

            using PipelineMessage message = CreateRenameSharedLabelRequest(content, options);
            return ClientResult.FromResponse(await Pipeline.ProcessMessageAsync(message, options).ConfigureAwait(false));
        }

        /// <summary> renameSharedLabel. </summary>
        /// <param name="body"></param>
        /// <param name="cancellationToken"> The cancellation token that can be used to cancel the operation. </param>
        /// <exception cref="ArgumentNullException"> <paramref name="body"/> is null. </exception>
        /// <exception cref="ClientResultException"> Service returned a non-success status code. </exception>
        public virtual ClientResult RenameSharedLabel(RenameSharedLabelRequest body, CancellationToken cancellationToken = default)
        {
            Argument.AssertNotNull(body, nameof(body));

            return RenameSharedLabel(body, cancellationToken.CanBeCanceled ? new RequestOptions { CancellationToken = cancellationToken } : null);
        }

        /// <summary> renameSharedLabel. </summary>
        /// <param name="body"></param>
        /// <param name="cancellationToken"> The cancellation token that can be used to cancel the operation. </param>
        /// <exception cref="ArgumentNullException"> <paramref name="body"/> is null. </exception>
        /// <exception cref="ClientResultException"> Service returned a non-success status code. </exception>
        public virtual async Task<ClientResult> RenameSharedLabelAsync(RenameSharedLabelRequest body, CancellationToken cancellationToken = default)
        {
            Argument.AssertNotNull(body, nameof(body));

            return await RenameSharedLabelAsync(body, cancellationToken.CanBeCanceled ? new RequestOptions { CancellationToken = cancellationToken } : null).ConfigureAwait(false);
        }

        /// <summary>
        /// [Protocol Method] removeSharedLabel
        /// <list type="bullet">
        /// <item>
        /// <description> This <see href="https://aka.ms/azsdk/net/protocol-methods">protocol method</see> allows explicit creation of the request and processing of the response for advanced scenarios. </description>
        /// </item>
        /// </list>
        /// </summary>
        /// <param name="content"> The content to send as the body of the request. </param>
        /// <param name="options"> The request options, which can override default behaviors of the client pipeline on a per-call basis. </param>
        /// <exception cref="ArgumentNullException"> <paramref name="content"/> is null. </exception>
        /// <exception cref="ClientResultException"> Service returned a non-success status code. </exception>
        /// <returns> The response returned from the service. </returns>
        public virtual ClientResult RemoveSharedLabel(BinaryContent content, RequestOptions options = null)
        {
            Argument.AssertNotNull(content, nameof(content));

            using PipelineMessage message = CreateRemoveSharedLabelRequest(content, options);
            return ClientResult.FromResponse(Pipeline.ProcessMessage(message, options));
        }

        /// <summary>
        /// [Protocol Method] removeSharedLabel
        /// <list type="bullet">
        /// <item>
        /// <description> This <see href="https://aka.ms/azsdk/net/protocol-methods">protocol method</see> allows explicit creation of the request and processing of the response for advanced scenarios. </description>
        /// </item>
        /// </list>
        /// </summary>
        /// <param name="content"> The content to send as the body of the request. </param>
        /// <param name="options"> The request options, which can override default behaviors of the client pipeline on a per-call basis. </param>
        /// <exception cref="ArgumentNullException"> <paramref name="content"/> is null. </exception>
        /// <exception cref="ClientResultException"> Service returned a non-success status code. </exception>
        /// <returns> The response returned from the service. </returns>
        public virtual async Task<ClientResult> RemoveSharedLabelAsync(BinaryContent content, RequestOptions options = null)
        {
            Argument.AssertNotNull(content, nameof(content));

            using PipelineMessage message = CreateRemoveSharedLabelRequest(content, options);
            return ClientResult.FromResponse(await Pipeline.ProcessMessageAsync(message, options).ConfigureAwait(false));
        }

        /// <summary> removeSharedLabel. </summary>
        /// <param name="body"></param>
        /// <param name="cancellationToken"> The cancellation token that can be used to cancel the operation. </param>
        /// <exception cref="ArgumentNullException"> <paramref name="body"/> is null. </exception>
        /// <exception cref="ClientResultException"> Service returned a non-success status code. </exception>
        public virtual ClientResult RemoveSharedLabel(RemoveSharedLabelRequest body, CancellationToken cancellationToken = default)
        {
            Argument.AssertNotNull(body, nameof(body));

            return RemoveSharedLabel(body, cancellationToken.CanBeCanceled ? new RequestOptions { CancellationToken = cancellationToken } : null);
        }

        /// <summary> removeSharedLabel. </summary>
        /// <param name="body"></param>
        /// <param name="cancellationToken"> The cancellation token that can be used to cancel the operation. </param>
        /// <exception cref="ArgumentNullException"> <paramref name="body"/> is null. </exception>
        /// <exception cref="ClientResultException"> Service returned a non-success status code. </exception>
        public virtual async Task<ClientResult> RemoveSharedLabelAsync(RemoveSharedLabelRequest body, CancellationToken cancellationToken = default)
        {
            Argument.AssertNotNull(body, nameof(body));

            return await RemoveSharedLabelAsync(body, cancellationToken.CanBeCanceled ? new RequestOptions { CancellationToken = cancellationToken } : null).ConfigureAwait(false);
        }
    }
}