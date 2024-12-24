using Getitdone.Service.Repositories;
using Getitdone.Service.Repositories.InMemory;
using Getitdone.Service.Services;
using Getitdone.Service;

var builder = WebApplication.CreateBuilder(args);

// Add services to the container.
builder.Services.AddControllers();
builder.Services.AddEndpointsApiExplorer();

// Add CORS configuration
builder.Services.AddCors(options =>
{
    options.AddDefaultPolicy(builder =>
    {
        builder.AllowAnyOrigin()
               .AllowAnyMethod()
               .AllowAnyHeader();
    });
});

// Register Repositories
builder.Services.AddSingleton<ICommentRepository, InMemoryCommentRepository>();
builder.Services.AddSingleton<ILabelRepository, InMemoryLabelRepository>();
builder.Services.AddSingleton<IProjectRepository, InMemoryProjectRepository>();
builder.Services.AddSingleton<ISectionRepository, InMemorySectionRepository>();
builder.Services.AddSingleton<ITodoItemRepository, InMemoryTodoItemRepository>();

// Register Services
builder.Services.AddScoped<ICommentOpsOperations, CommentOpsOperations>();
builder.Services.AddScoped<ICommentsOperations, CommentsOperations>();
builder.Services.AddScoped<ILabelOpsOperations, LabelOpsOperations>();
builder.Services.AddScoped<ILabelsOperations, LabelsOperations>();
builder.Services.AddScoped<IProjectOpsOperations, ProjectOpsOperations>();
builder.Services.AddScoped<IProjectsOperations, ProjectsOperations>();
builder.Services.AddScoped<ISectionOpsOperations, SectionOpsOperations>();
builder.Services.AddScoped<ISectionsOperations, SectionsOperations>();
builder.Services.AddScoped<ISharedLabelsOperations, SharedLabelsOperations>();
builder.Services.AddScoped<ITodoItemOpsOperations, TodoItemOpsOperations>();
builder.Services.AddScoped<ITodoItemsOperations, TodoItemsOperations>();

var app = builder.Build();

// Configure the HTTP request pipeline.
app.UseCors();

app.UseHttpsRedirection();

app.UseAuthorization();

app.MapControllers();

app.Run();