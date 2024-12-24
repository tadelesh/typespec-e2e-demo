using Getitdone.Service.Models;
using Getitdone.Service.Repositories;
using Getitdone.Service;

namespace Getitdone.Service.Services
{
    public class TodoItemOpsOperations : ITodoItemOpsOperations
    {
        private readonly ITodoItemRepository _todoItemRepository;

        public TodoItemOpsOperations(ITodoItemRepository todoItemRepository)
        {
            _todoItemRepository = todoItemRepository;
        }

        public async Task<TodoItem> GetTodoItemAsync(string todoitemId)
        {
            try
            {
                var todoItem = await _todoItemRepository.GetByIdAsync(todoitemId);
                if (todoItem == null)
                {
                    throw new KeyNotFoundException($"TodoItem with id '{todoitemId}' not found.");
                }
                return todoItem;
            }
            catch (KeyNotFoundException)
            {
                throw;
            }
            catch (Exception ex)
            {
                // Log the exception
                Console.WriteLine($"Error getting todo item: {ex.Message}");
                throw;
            }
        }

        public async Task<TodoItem> UpdateTodoItemAsync(string todoitemId, UpdateTodoItemRequest body)
        {
            try
            {
                var existingTodoItem = await _todoItemRepository.GetByIdAsync(todoitemId);
                if (existingTodoItem == null)
                {
                    throw new KeyNotFoundException($"TodoItem with id '{todoitemId}' not found.");
                }

                existingTodoItem.Content = body.Content;
                existingTodoItem.Description = body.Description;
                existingTodoItem.Due = body.Due;
                existingTodoItem.Labels = body.Labels;
                existingTodoItem.Priority = body.Priority ?? existingTodoItem.Priority;
                existingTodoItem.ParentId = body.ParentId;
                existingTodoItem.Order = body.Order ?? existingTodoItem.Order;
                existingTodoItem.ProjectId = body.ProjectId;
                existingTodoItem.SectionId = body.SectionId;
                existingTodoItem.AssigneeId = body.AssigneeId;

                return await _todoItemRepository.UpdateAsync(existingTodoItem);
            }
            catch (KeyNotFoundException)
            {
                throw;
            }
            catch (Exception ex)
            {
                // Log the exception
                Console.WriteLine($"Error updating todo item: {ex.Message}");
                throw;
            }
        }

        public async Task CloseTodoItemAsync(string todoitemId)
        {
            try
            {
                var existingTodoItem = await _todoItemRepository.GetByIdAsync(todoitemId);
                if (existingTodoItem == null)
                {
                    throw new KeyNotFoundException($"TodoItem with id '{todoitemId}' not found.");
                }

                existingTodoItem.IsCompleted = true;
                await _todoItemRepository.UpdateAsync(existingTodoItem);
            }
            catch (KeyNotFoundException)
            {
                throw;
            }
            catch (Exception ex)
            {
                // Log the exception
                Console.WriteLine($"Error closing todo item: {ex.Message}");
                throw;
            }
        }

        public async Task ReopenTodoItemAsync(string todoitemId)
        {
            try
            {
                var existingTodoItem = await _todoItemRepository.GetByIdAsync(todoitemId);
                if (existingTodoItem == null)
                {
                    throw new KeyNotFoundException($"TodoItem with id '{todoitemId}' not found.");
                }

                existingTodoItem.IsCompleted = false;
                await _todoItemRepository.UpdateAsync(existingTodoItem);
            }
            catch (KeyNotFoundException)
            {
                throw;
            }
            catch (Exception ex)
            {
                // Log the exception
                Console.WriteLine($"Error reopening todo item: {ex.Message}");
                throw;
            }
        }

        public async Task DeleteTodoItemAsync(string todoitemId)
        {
            try
            {
                var existingTodoItem = await _todoItemRepository.GetByIdAsync(todoitemId);
                if (existingTodoItem == null)
                {
                    throw new KeyNotFoundException($"TodoItem with id '{todoitemId}' not found.");
                }
                await _todoItemRepository.DeleteAsync(todoitemId);
            }
            catch (KeyNotFoundException)
            {
                throw;
            }
            catch (Exception ex)
            {
                // Log the exception
                Console.WriteLine($"Error deleting todo item: {ex.Message}");
                throw;
            }
        }
    }
}