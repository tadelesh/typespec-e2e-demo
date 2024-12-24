using Getitdone.Service.Models;
using Getitdone.Service.Repositories;
using Microsoft.AspNetCore.Mvc;
using Getitdone.Service;

namespace Getitdone.Service.Services
{
    public class CommentOpsOperations : ICommentOpsOperations
    {
        private readonly ICommentRepository _commentRepository;

        public CommentOpsOperations(ICommentRepository commentRepository)
        {
            _commentRepository = commentRepository;
        }

        public async Task<Comment> GetCommentAsync(string commentId)
        {
            try
            {
                var comment = await _commentRepository.GetByIdAsync(commentId);
                if (comment == null)
                {
                    throw new KeyNotFoundException($"Comment with id '{commentId}' not found.");
                }
                return comment;
            }
            catch (KeyNotFoundException)
            {
                throw;
            }
            catch (Exception ex)
            {
                // Log the exception
                Console.WriteLine($"Error getting comment: {ex.Message}");
                throw;
            }
        }

        public async Task<Comment> UpdateCommentAsync(string commentId, UpdateCommentRequest body)
        {
            try
            {
                var existingComment = await _commentRepository.GetByIdAsync(commentId);
                if (existingComment == null)
                {
                    throw new KeyNotFoundException($"Comment with id '{commentId}' not found.");
                }

                existingComment.Content = body.Content;
                existingComment.Attachment = body.Attachment;

                return await _commentRepository.UpdateAsync(existingComment);
            }
            catch (KeyNotFoundException)
            {
                throw;
            }
            catch (Exception ex)
            {
                // Log the exception
                Console.WriteLine($"Error updating comment: {ex.Message}");
                throw;
            }
        }

        public async Task DeleteCommentAsync(string commentId)
        {
            try
            {
                var existingComment = await _commentRepository.GetByIdAsync(commentId);
                if (existingComment == null)
                {
                    throw new KeyNotFoundException($"Comment with id '{commentId}' not found.");
                }
                await _commentRepository.DeleteAsync(commentId);
            }
            catch (KeyNotFoundException)
            {
                throw;
            }
            catch (Exception ex)
            {
                // Log the exception
                Console.WriteLine($"Error deleting comment: {ex.Message}");
                throw;
            }
        }
    }
}