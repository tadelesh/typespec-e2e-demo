using Getitdone.Service.Models;
using Getitdone.Service.Repositories;
using Getitdone.Service;

namespace Getitdone.Service.Services
{
    public class CommentsOperations : ICommentsOperations
    {
        private readonly ICommentRepository _commentRepository;

        public CommentsOperations(ICommentRepository commentRepository)
        {
            _commentRepository = commentRepository;
        }

        public async Task<Comment[]> GetCommentsAsync(string? todoitemId, string? projectId)
        {
            try
            {
                var comments = await _commentRepository.GetAllAsync(todoitemId, projectId);
                return comments.ToArray();
            }
            catch (Exception ex)
            {
                // Log the exception
                Console.WriteLine($"Error getting comments: {ex.Message}");
                throw;
            }
        }

        public async Task<Comment> CreateCommentAsync(CreateCommentRequest body)
        {
            try
            {
                var newComment = new Comment
                {
                    Id = Guid.NewGuid().ToString(),
                    Content = body.Content,
                    PostedAt = DateTime.UtcNow.ToString("o"),
                    ProjectId = body.ProjectId,
                    TodoitemId = body.TodoitemId,
                    Attachment = body.Attachment
                };

                return await _commentRepository.AddAsync(newComment);
            }
            catch (Exception ex)
            {
                // Log the exception
                Console.WriteLine($"Error creating comment: {ex.Message}");
                throw;
            }
        }
    }
}