# Build a ToDoIst clone API with C#/.NET using service code generated from TypeSpec

## Introduction

This guide will walk you through the process of building a RESTful API using C# and .NET. We'll be creating a backend for a "Todo" style application, leveraging pre-generated code and adding custom logic to complete the implementation. We'll cover essential concepts like data persistence, data access layers, dependency injection, and error handling. We'll test our API using Thunder Client and a simple HTML front-end.

## Prerequisites

Before you begin, make sure you have the following installed:

*   **\.NET SDK:** Download and install the .NET SDK from [https://dotnet.microsoft.com/download](https://dotnet.microsoft.com/download).
*   **Visual Studio Code (VS Code):** Download and install VS Code from [https://code.visualstudio.com/](https://code.visualstudio.com/).
*   **C# Extension for VS Code:** Install the C# extension in VS Code.
*   **Thunder Client Extension for VS Code:** Install the Thunder Client extension in VS Code.

## Step 1: Create a New ASP.NET Core Web API Project

1.  **Open a Terminal:** Open your terminal or command prompt.
2.  **Navigate to a Directory:** Navigate to the directory where you want to create your project.
3.  **Create the Project:** Run the following command:

    ```bash
    dotnet new webapi -o Getitdone.Service
    ```

    This command creates a new ASP.NET Core Web API project in a folder named `Getitdone.Service`.

## Step 2: Organize the Project Structure

1.  **Open the Project:** Open the `Getitdone.Service` folder in VS Code.
2.  **Create Folders:** Create the following folders within the project:
    *   `Controllers`
    *   `generated`
    *   `generated/controllers`
    *   `generated/lib`
    *   `generated/models`
    *   `generated/operations`
    *   `Helpers`
    *   `Repositories`
    *   `Repositories/InMemory`
    *   `Services`

## Step 3: Add Generated Code

1.  **Copy Generated Files:** Copy the generated files you have into the corresponding folders:
    *   `generated/controllers`: All files ending with `ControllerBase.cs`
    *   `generated/lib`: All files ending with `.cs`
    *   `generated/models`: All files ending with `.cs`
    *   `generated/operations`: All files ending with `.cs`

## Step 4: Create Repository Interfaces

1.  **Create Files:** Create the following files in the `Repositories` folder:
    *   `ICommentRepository.cs`
    *   `ILabelRepository.cs`
    *   `IProjectRepository.cs`
    *   `ISectionRepository.cs`
    *   `ITodoItemRepository.cs`
2.  **Add Code:** Use the following prompts with an AI (like me) to generate the code for each file.

    *   **Prompt for `ICommentRepository.cs`:**

        ```
        Create a C# interface named `ICommentRepository` in the namespace `Getitdone.Service.Repositories`. It should have the following methods:
        - `Task<Comment?> GetByIdAsync(string id)`
        - `Task<IEnumerable<Comment>> GetAllAsync(string? todoitemId, string? projectId)`
        - `Task<Comment> AddAsync(Comment comment)`
        - `Task<Comment> UpdateAsync(Comment comment)`
        - `Task DeleteAsync(string id)`
        Use the `Getitdone.Service.Models` namespace for the `Comment` type.
        ```

    *   **Prompt for `ILabelRepository.cs`:**

        ```
        Create a C# interface named `ILabelRepository` in the namespace `Getitdone.Service.Repositories`. It should have the following methods:
        - `Task<Label?> GetByIdAsync(string id)`
        - `Task<IEnumerable<Label>> GetAllAsync()`
        - `Task<Label> AddAsync(Label label)`
        - `Task<Label> UpdateAsync(Label label)`
        - `Task DeleteAsync(string id)`
        Use the `Getitdone.Service.Models` namespace for the `Label` type.
        ```

    *   **Prompt for `IProjectRepository.cs`:**

        ```
        Create a C# interface named `IProjectRepository` in the namespace `Getitdone.Service.Repositories`. It should have the following methods:
        - `Task<Project?> GetByIdAsync(string id)`
        - `Task<IEnumerable<Project>> GetAllAsync()`
        - `Task<Project> AddAsync(Project project)`
        - `Task<Project> UpdateAsync(Project project)`
        - `Task DeleteAsync(string id)`
        - `Task<IEnumerable<Collaborator>> GetCollaboratorsAsync(string projectId)`
        Use the `Getitdone.Service.Models` namespace for the `Project` and `Collaborator` types.
        ```

    *   **Prompt for `ISectionRepository.cs`:**

        ```
        Create a C# interface named `ISectionRepository` in the namespace `Getitdone.Service.Repositories`. It should have the following methods:
        - `Task<Section?> GetByIdAsync(string id)`
        - `Task<IEnumerable<Section>> GetAllAsync(string projectId)`
        - `Task<Section> AddAsync(Section section)`
        - `Task<Section> UpdateAsync(Section section)`
        - `Task DeleteAsync(string id)`
        Use the `Getitdone.Service.Models` namespace for the `Section` type.
        ```

    *   **Prompt for `ITodoItemRepository.cs`:**

        ```
        Create a C# interface named `ITodoItemRepository` in the namespace `Getitdone.Service.Repositories`. It should have the following methods:
        - `Task<TodoItem?> GetByIdAsync(string id)`
        - `Task<IEnumerable<TodoItem>> GetAllAsync()`
        - `Task<TodoItem> AddAsync(TodoItem todoItem)`
        - `Task<TodoItem> UpdateAsync(TodoItem todoItem)`
        - `Task DeleteAsync(string id)`
        Use the `Getitdone.Service.Models` namespace for the `TodoItem` type.
        ```

## Step 5: Create In-Memory Repository Implementations

1.  **Create Files:** Create the following files in the `Repositories/InMemory` folder:
    *   `InMemoryCommentRepository.cs`
    *   `InMemoryLabelRepository.cs`
    *   `InMemoryProjectRepository.cs`
    *   `InMemorySectionRepository.cs`
    *   `InMemoryTodoItemRepository.cs`
2.  **Add Code:** Use the following prompts with an AI (like me) to generate the code for each file.

    *   **Prompt for `InMemoryCommentRepository.cs`:**

        ```
        Create a C# class named `InMemoryCommentRepository` in the namespace `Getitdone.Service.Repositories.InMemory` that implements the `ICommentRepository` interface. Use a `ConcurrentDictionary<string, Comment>` to store the data. Implement all the methods of the interface using the in-memory dictionary.
        Use the `Getitdone.Service.Models` namespace for the `Comment` type.
        ```

    *   **Prompt for `InMemoryLabelRepository.cs`:**

        ```
        Create a C# class named `InMemoryLabelRepository` in the namespace `Getitdone.Service.Repositories.InMemory` that implements the `ILabelRepository` interface. Use a `ConcurrentDictionary<string, Label>` to store the data. Implement all the methods of the interface using the in-memory dictionary.
        Use the `Getitdone.Service.Models` namespace for the `Label` type.
        ```

    *   **Prompt for `InMemoryProjectRepository.cs`:**

        ```
        Create a C# class named `InMemoryProjectRepository` in the namespace `Getitdone.Service.Repositories.InMemory` that implements the `IProjectRepository` interface. Use a `ConcurrentDictionary<string, Project>` to store the project data and a `ConcurrentDictionary<string, List<Collaborator>>` to store the collaborators. Implement all the methods of the interface using the in-memory dictionaries.
        Use the `Getitdone.Service.Models` namespace for the `Project` and `Collaborator` types.
        ```

    *   **Prompt for `InMemorySectionRepository.cs`:**

        ```
        Create a C# class named `InMemorySectionRepository` in the namespace `Getitdone.Service.Repositories.InMemory` that implements the `ISectionRepository` interface. Use a `ConcurrentDictionary<string, Section>` to store the data. Implement all the methods of the interface using the in-memory dictionary.
        Use the `Getitdone.Service.Models` namespace for the `Section` type.
        ```

    *   **Prompt for `InMemoryTodoItemRepository.cs`:**

        ```
        Create a C# class named `InMemoryTodoItemRepository` in the namespace `Getitdone.Service.Repositories.InMemory` that implements the `ITodoItemRepository` interface. Use a `ConcurrentDictionary<string, TodoItem>` to store the data. Implement all the methods of the interface using the in-memory dictionary.
        Use the `Getitdone.Service.Models` namespace for the `TodoItem` type.
        ```

## Step 6: Create Service Layer Implementations

1.  **Create Files:** Create the following files in the `Services` folder:
    *   `CommentOpsOperations.cs`
    *   `CommentsOperations.cs`
    *   `LabelOpsOperations.cs`
    *   `LabelsOperations.cs`
    *   `ProjectOpsOperations.cs`
    *   `ProjectsOperations.cs`
    *   `SectionOpsOperations.cs`
    *   `SectionsOperations.cs`
    *   `SharedLabelsOperations.cs`
    *   `TodoItemOpsOperations.cs`
    *   `TodoItemsOperations.cs`
2.  **Add Code:** Use the following prompts with an AI (like me) to generate the code for each file.

    *   **Prompt for `CommentOpsOperations.cs`:**

        ```
        Create a C# class named `CommentOpsOperations` in the namespace `Getitdone.Service.Services` that implements the `ICommentOpsOperations` interface. Inject an `ICommentRepository` through the constructor. Implement all the methods of the interface, including error handling with try-catch blocks. Log exceptions to the console.
        Use the `Getitdone.Service.Models` namespace for the model types and `Getitdone.Service` namespace for the interface.
        ```

    *   **Prompt for `CommentsOperations.cs`:**

        ```
        Create a C# class named `CommentsOperations` in the namespace `Getitdone.Service.Services` that implements the `ICommentsOperations` interface. Inject an `ICommentRepository` through the constructor. Implement all the methods of the interface, including error handling with try-catch blocks. Log exceptions to the console.
        Use the `Getitdone.Service.Models` namespace for the model types and `Getitdone.Service` namespace for the interface.
        ```

    *   **Prompt for `LabelOpsOperations.cs`:**

        ```
        Create a C# class named `LabelOpsOperations` in the namespace `Getitdone.Service.Services` that implements the `ILabelOpsOperations` interface. Inject an `ILabelRepository` through the constructor. Implement all the methods of the interface, including error handling with try-catch blocks. Log exceptions to the console.
        Use the `Getitdone.Service.Models` namespace for the model types and `Getitdone.Service` namespace for the interface.
        ```

    *   **Prompt for `LabelsOperations.cs`:**

        ```
        Create a C# class named `LabelsOperations` in the namespace `Getitdone.Service.Services` that implements the `ILabelsOperations` interface. Inject an `ILabelRepository` through the constructor. Implement all the methods of the interface, including error handling with try-catch blocks. Log exceptions to the console.
        Use the `Getitdone.Service.Models` namespace for the model types and `Getitdone.Service` namespace for the interface.
        ```

    *   **Prompt for `ProjectOpsOperations.cs`:**

        ```
        Create a C# class named `ProjectOpsOperations` in the namespace `Getitdone.Service.Services` that implements the `IProjectOpsOperations` interface. Inject an `IProjectRepository` through the constructor. Implement all the methods of the interface, including error handling with try-catch blocks. Log exceptions to the console.
        Use the `Getitdone.Service.Models` namespace for the model types and `Getitdone.Service` namespace for the interface.
        ```

    *   **Prompt for `ProjectsOperations.cs`:**

        ```
        Create a C# class named `ProjectsOperations` in the namespace `Getitdone.Service.Services` that implements the `IProjectsOperations` interface. Inject an `IProjectRepository` through the constructor. Implement all the methods of the interface, including error handling with try-catch blocks. Log exceptions to the console.
        Use the `Getitdone.Service.Models` namespace for the model types and `Getitdone.Service` namespace for the interface.
        ```

    *   **Prompt for `SectionOpsOperations.cs`:**

        ```
        Create a C# class named `SectionOpsOperations` in the namespace `Getitdone.Service.Services` that implements the `ISectionOpsOperations` interface. Inject an `ISectionRepository` through the constructor. Implement all the methods of the interface, including error handling with try-catch blocks. Log exceptions to the console.
        Use the `Getitdone.Service.Models` namespace for the model types and `Getitdone.Service` namespace for the interface.
        ```

    *   **Prompt for `SectionsOperations.cs`:**

        ```
        Create a C# class named `SectionsOperations` in the namespace `Getitdone.Service.Services` that implements the `ISectionsOperations` interface. Inject an `ISectionRepository` through the constructor. Implement all the methods of the interface, including error handling with try-catch blocks. Log exceptions to the console.
        Use the `Getitdone.Service.Models` namespace for the model types and `Getitdone.Service` namespace for the interface.
        ```

    *   **Prompt for `SharedLabelsOperations.cs`:**

        ```
        Create a C# class named `SharedLabelsOperations` in the namespace `Getitdone.Service.Services` that implements the `ISharedLabelsOperations` interface. Inject an `ILabelRepository` through the constructor. Implement all the methods of the interface, including error handling with try-catch blocks. Log exceptions to the console.
        Use the `Getitdone.Service.Models` namespace for the model types and `Getitdone.Service` namespace for the interface.
        ```

    *   **Prompt for `TodoItemOpsOperations.cs`:**

        ```
        Create a C# class named `TodoItemOpsOperations` in the namespace `Getitdone.Service.Services` that implements the `ITodoItemOpsOperations` interface. Inject an `ITodoItemRepository` through the constructor. Implement all the methods of the interface, including error handling with try-catch blocks. Log exceptions to the console.
        Use the `Getitdone.Service.Models` namespace for the model types and `Getitdone.Service` namespace for the interface.
        ```

    *   **Prompt for `TodoItemsOperations.cs`:**

        ```
        Create a C# class named `TodoItemsOperations` in the namespace `Getitdone.Service.Services` that implements the `ITodoItemsOperations` interface. Inject an `ITodoItemRepository` through the constructor. Implement all the methods of the interface, including error handling with try-catch blocks. Log exceptions to the console.
        Use the `Getitdone.Service.Models` namespace for the model types and `Getitdone.Service` namespace for the interface.
        ```

## Step 7: Create Controller Helper

1.  **Create File:** Create a file named `ControllerHelpers.cs` in the `Helpers` folder.
2.  **Add Code:** Use the following prompt with an AI (like me) to generate the code for the file.

    *   **Prompt for `ControllerHelpers.cs`:**

        ```
        Create a static C# class named `ControllerHelpers` in the namespace `Getitdone.Service.Helpers`. It should have a static method named `HandleErrorResponse` that takes an `Exception` as a parameter and returns an `IActionResult`. The method should return a `NotFound` response for `KeyNotFoundException` and an `InternalServerError` response for other exceptions. Use the `Getitdone.Service.Models` namespace for the `ErrorResponse` type.
        ```

## Step 8: Create Concrete Controllers

1.  **Create Files:** Create the following files in the `Controllers` folder:
    *   `CommentOpsController.cs`
    *   `CommentsController.cs`
    *   `LabelOpsController.cs`
    *   `LabelsController.cs`
    *   `ProjectOpsController.cs`
    *   `ProjectsController.cs`
    *   `SectionOpsController.cs`
    *   `SectionsController.cs`
    *   `SharedLabelsController.cs`
    *   `TodoItemOpsController.cs`
    *   `TodoItemsController.cs`
2.  **Add Code:** For each of these files, use the following prompt with an AI (like me), replacing `[ControllerName]` with the actual name of the controller (e.g., `CommentOpsController`):

    ```
    Create a C# class named `[ControllerName]` in the namespace `Getitdone.Service.Controllers` that inherits from the corresponding generated controller base class (e.g., `CommentOpsOperationsControllerBase`). Inject the corresponding service interface (e.g., `ICommentOpsOperations`) through the constructor. Implement all the methods of the base class, using the injected service and the `ControllerHelpers.HandleErrorResponse` method for error handling.
    Use the `Getitdone.Service.Models` namespace for the model types, `Getitdone.Service.Helpers` for the `ControllerHelpers` class, and `Getitdone.Service` for the service interface.
    ```

## Step 9: Configure Dependency Injection

1.  **Open `Program.cs`:** Open the `Program.cs` file in your project.
2.  **Add DI Registrations:** Add the following code to register the repositories and services with the dependency injection container:

    ```csharp
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
    ```

## Step 10: Build and Run the Application

1.  **Open a Terminal:** Open your terminal or command prompt.
2.  **Navigate to the Project Directory:** Navigate to the `Getitdone.Service` directory.
3.  **Build the Project:** Run the following command:

    ```bash
    dotnet build
    ```

4.  **Run the Project:** After a successful build, run the project:

    ```bash
    dotnet run
    ```

    The console output will display the base URL where your API is running (e.g., `http://localhost:5000` or `https://localhost:7000`).

## Step 11: Test the API with Thunder Client and a Simple HTML Front-End

### Using Thunder Client

1.  **Open Thunder Client:** In VS Code, click on the Thunder Client icon in the Activity Bar.
2.  **Create Requests:** Use the following user journey to test your API:

    *   **Create a New Project:**
        *   **Method:** `POST`
        *   **URL:** `http://localhost:5000/projects` (or your base URL)
        *   **Headers:** `Content-Type: application/json`
        *   **Body:**

            ```json
            {
              "name": "My First Project",
              "color": "#3498db",
              "parentId": null,
              "order": 1,
              "isFavorite": false
            }
            ```

        *   **Verify:** `201 Created` status code and a JSON body with the new project's details, including its `id`.
    *   **Get All Projects:**
        *   **Method:** `GET`
        *   **URL:** `http://localhost:5000/projects`
        *   **Verify:** `200 OK` status code and a JSON body with an array of projects.
    *   **Create a New Section:**
        *   **Method:** `POST`
        *   **URL:** `http://localhost:5000/sections`
        *   **Headers:** `Content-Type: application/json`
        *   **Body:**

            ```json
            {
              "name": "My First Section",
              "projectId": "{project_id}",
              "order": 1
            }
            ```

            (Replace `{project_id}` with the `id` from the previous step)
        *   **Verify:** `201 Created` status code and a JSON body with the new section's details, including its `id`.
    *   **Get All Sections for a Project:**
        *   **Method:** `GET`
        *   **URL:** `http://localhost:5000/sections?project_id={project_id}` (Replace `{project_id}` with the project ID)
        *   **Verify:** `200 OK` status code and a JSON body with an array of sections.
    *   **Create a New Todo Item:**
        *   **Method:** `POST`
        *   **URL:** `http://localhost:5000/todoitems`
        *   **Headers:** `Content-Type: application/json`
        *   **Body:**

            ```json
            {
              "content": "My First Task",
              "description": "This is my first task in this project",
              "due": {
                "date": null,
                "isRecurring": false,
                "datetime": null,
                "string": null,
                "timezone": null
              },
              "labels": [],
              "priority": 1,
              "parentId": null,
              "order": 1,
              "projectId": "{project_id}",
              "sectionId": "{section_id}",
              "assigneeId": null
            }
            ```

            (Replace `{project_id}` and `{section_id}` with the appropriate IDs)
        *   **Verify:** `201 Created` status code and a JSON body with the new todo item's details, including its `id`.
    *   **Get All Todo Items:**
        *   **Method:** `GET`
        *   **URL:** `http://localhost:5000/todoitems`
        *   **Verify:** `200 OK` status code and a JSON body with an array of todo items.
    *   **Create a New Label:**
        *   **Method:** `POST`
        *   **URL:** `http://localhost:5000/labels`
        *   **Headers:** `Content-Type: application/json`
        *   **Body:**

            ```json
            {
              "name": "My First Label",
              "color": "#e74c3c",
              "order": 1,
              "isFavorite": true
            }
            ```

        *   **Verify:** `201 Created` status code and a JSON body with the new label's details, including its `id`.
    *   **Get All Labels:**
        *   **Method:** `GET`
        *   **URL:** `http://localhost:5000/labels`
        *   **Verify:** `200 OK` status code and a JSON body with an array of labels.
    *   **Update a Todo Item with a Label:**
        *   **Method:** `POST`
        *   **URL:** `http://localhost:5000/todoitems/{todoitem_id}` (Replace `{todoitem_id}` with the todo item ID)
        *   **Headers:** `Content-Type: application/json`
        *   **Body:**

            ```json
            {
              "content": "My First Task",
              "description": "This is my first task in this project",
              "due": {
                "date": null,
                "isRecurring": false,
                "datetime": null,
                "string": null,
                "timezone": null
              },
              "labels": ["{label_id}"],
              "priority": 1,
              "parentId": null,
              "order": 1,
              "projectId": "{project_id}",
              "sectionId": "{section_id}",
              "assigneeId": null
            }
            ```

            (Replace `{todoitem_id}`, `{label_id}`, `{project_id}`, and `{section_id}` with the appropriate IDs)
        *   **Verify:** `200 OK` status code and a JSON body with the updated todo item.
    *   **Get a Todo Item:**
        *   **Method:** `GET`
        *   **URL:** `http://localhost:5000/todoitems/{todoitem_id}` (Replace `{todoitem_id}` with the todo item ID)
        *   **Verify:** `200 OK` status code and a JSON body with the todo item.

### Using the Simple HTML Front-End

1.  **Locate `index.html`:** The `index.html` file is located in the `Getitdone.Frontend` folder within your project.
2.  **Open in Browser:** Open the `index.html` file in your web browser. You can do this by right-clicking the file in VS Code and selecting "Open in Default Browser" or by navigating to the file path in your browser's address bar.
3.  **Interact with the API:**
    *   Enter data into the input fields.
    *   Click the buttons to trigger API requests.
    *   View the responses in the output area.

**Key Points for Using the Front-End:**

*   **API URL:** Ensure that the `apiUrl` variable in the `index.html` file (located within the `<script>` tag) is set to the correct base URL where your API is running (e.g., `http://localhost:5000`, `https://localhost:7000`, or `http://localhost:5091`). You can find this URL in the console output when you run your API using `dotnet run`.
*   **Input Fields:** Use the input fields to provide data for creating projects, sections, todo items, and labels.
*   **Buttons:** Click the buttons to trigger the corresponding API requests.
*   **Output Area:** The responses from the API will be displayed in the output area below the buttons.
*   **Basic Functionality:** This front-end provides basic functionality for creating and retrieving resources. It is intended for demonstration and testing purposes.
Conclusion

By following this guide, you've successfully built a RESTful API using C# and .NET, leveraging generated code and adding custom logic. You've also learned how to test your API using Thunder Client and a simple HTML front-end. This provides a solid foundation for building more complex applications.

Remember to replace placeholders like {project_id}, {section_id}, {todoitem_id}, and {label_id} with the actual IDs you receive from the API responses when testing with Thunder Client. Also, make sure to replace the apiUrl in index.html with the correct URL for your API.

This completes the `README.md` file. It now includes:

*   A clear title and introduction.
*   A list of prerequisites.
*   Step-by-step instructions for building the API.
*   Instructions for testing the API using both Thunder Client and the provided `index.html` file.
*   Details about the `index.html` file and how to use it.
