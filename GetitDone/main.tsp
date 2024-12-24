import "@typespec/http";
import "@typespec/rest";

using TypeSpec.Http;
using TypeSpec.Rest;

@service({ title: "Getitdone API" })
@server("https://api.Getitdone.com", "Production server")
namespace Getitdone {
  model Project {
    id: string;
    name: string;
    comment_count: int32;
    order: int32;
    color: string;
    is_shared: boolean;
    is_favorite: boolean;
    parent_id?: string;
    is_inbox_project: boolean;
    is_team_inbox: boolean;
    view_style: string;
    url: string;
  }

  model Section {
    id: string;
    project_id: string;
    order: int32;
    name: string;
  }

  model Due {
    date: string;
    is_recurring: boolean;
    datetime?: string;
    string: string;
    timezone?: string;
  }

  model TodoItem {
    creator_id: string;
    created_at: string;
    assignee_id: string;
    assigner_id: string;
    comment_count: int32;
    is_completed: boolean;
    content: string;
    description: string;
    due?: Due;
    duration?: string;
    id: string;
    labels: string[];
    order: int32;
    priority: int32;
    project_id: string;
    section_id?: string;
    parent_id?: string;
    url: string;
  }

  model Attachment {
    file_name: string;
    file_type: string;
    file_url: string;
    resource_type: string;
  }

  model Comment {
    content: string;
    id: string;
    posted_at: string;
    project_id?: string;
    todoitem_id?: string;
    attachment?: Attachment;
  }

  model Label {
    id: string;
    name: string;
    color: string;
    order: int32;
    is_favorite: boolean;
  }

  // Example error model. You can define more uses if needed.
  @error
  model ErrorResponse {
    error: string;
    status_code: int32;
  }

  model Collaborator {
    id: string;
    name: string;
    email: string;
  }

  model CreateProjectRequest {
    name: string;
    color?: string;
    parent_id?: string;
    order?: int32;
    is_favorite?: boolean;
  }

  model UpdateProjectRequest {
    name?: string;
    color?: string;
    parent_id?: string;
    order?: int32;
    is_favorite?: boolean;
  }

  @route("/projects")
  namespace Projects {
      @get
      op getProjects(): GetProjectsResponse;

      model GetProjectsResponse {
        @statusCode statusCode: 200;
        @body projects: Project[];
      }

      model CreateProjectResponse {
        @statusCode statusCode: 201;
        @body project: Project;
      }
      
      @post
      op createProject(@body body: CreateProjectRequest): CreateProjectResponse;

      @route("/{project_id}")
      namespace ProjectOps {
        @get
        op getProject(@path project_id: string):
              | GetProjectResponse | ErrorResponse;;
      
      model GetProjectResponse {
        @statusCode statusCode: 200;
        @body project: Project;
      }


      model UpdateProjectResponse {
        @statusCode statusCode: 200;
        @body project: Project;
      }

      @post
      op updateProject(@path project_id: string, @body body: UpdateProjectRequest): UpdateProjectResponse;

      @delete
      op deleteProject(@path project_id: string): {
        @statusCode statusCode: 204;
      };

      @route("/collaborators")
      @get
      op getCollaborators(@path project_id: string): GetCollaboratorsResponse;

      model GetCollaboratorsResponse {
        @statusCode statusCode: 200;
        @body collaborators: Collaborator[];
      }
    }
  }

  model CreateSectionRequest {
    name: string;
    project_id: string;
    order?: int32;
  }

  model UpdateSectionRequest {
    name?: string;
    order?: int32;
  }

  @route("/sections")
  namespace Sections {
    @get
    op getSections(@query project_id: string): GetSectionsResponse;

    model GetSectionsResponse {
      @statusCode statusCode: 200;
      @body sections: Section[];
    }

    @post
    op createSection(@body body: CreateSectionRequest): CreateSectionResponse;

    model CreateSectionResponse {
      @statusCode statusCode: 201;
      @body section: Section;
    }

    @route("/{section_id}")
    namespace SectionOps {
      @get
      op getSection(@path section_id: string): GetSectionResponse;

      model GetSectionResponse {
        @statusCode statusCode: 200;
        @body section: Section;
      }

      @post
      op updateSection(@path section_id: string, @body body: UpdateSectionRequest): UpdateSectionResponse;

      model UpdateSectionResponse {
        @statusCode statusCode: 200;
        @body section: Section;
      }

      @delete
      op deleteSection(@path section_id: string): DeleteSectionResponse;

      model DeleteSectionResponse {
        @statusCode statusCode: 204;
      }
    }
  }

  model CreateTodoItemRequest {
    content: string;
    description?: string;
    due?: Due;
    labels?: string[];
    priority?: int32;
    parent_id?: string;
    order?: int32;
    project_id?: string;
    section_id?: string;
    assignee_id?: string;
  }

  model UpdateTodoItemRequest {
    content?: string;
    description?: string;
    due?: Due;
    labels?: string[];
    priority?: int32;
    parent_id?: string;
    order?: int32;
    project_id?: string;
    section_id?: string;
    assignee_id?: string;
  }

  @route("/todoitems")
  namespace TodoItems {
    @get
    op getTodoItems(): GetTodoItemsResponse;

    model GetTodoItemsResponse {
      @statusCode statusCode: 200;
      @body todoitems: TodoItem[];
    }

    @post
    op createTodoItem(@body body: CreateTodoItemRequest): CreateTodoItemResponse;

    model CreateTodoItemResponse {
      @statusCode statusCode: 201;
      @body todoitem: TodoItem;
    }

    @route("/{todoitem_id}")
    namespace TodoItemOps {
      @get
      op getTodoItem(@path todoitem_id: string): GetTodoItemResponse;

      model GetTodoItemResponse {
        @statusCode statusCode: 200;
        @body todoitem: TodoItem;
      }

      @post
      op updateTodoItem(@path todoitem_id: string, @body body: UpdateTodoItemRequest): UpdateTodoItemResponse;

      model UpdateTodoItemResponse {
        @statusCode statusCode: 200;
        @body todoitem: TodoItem;
      }

      @route("/close")
      @post
      op closeTodoItem(@path todoitem_id: string): {
        @statusCode statusCode: 204;
      };

      @route("/reopen")
      @post
      op reopenTodoItem(@path todoitem_id: string): {
        @statusCode statusCode: 204;
      };

      @delete
      op deleteTodoItem(@path todoitem_id: string): {
        @statusCode statusCode: 204;
      };
    }
  }

  model CreateCommentRequest {
    content: string;
    todoitem_id?: string;
    project_id?: string;
    attachment?: Attachment;
  }

  model UpdateCommentRequest {
    content?: string;
    attachment?: Attachment;
  }

  @route("/comments")
  namespace Comments {
    @get
    op getComments(@query todoitem_id?: string, @query project_id?: string): GetCommentsResponse;

    model GetCommentsResponse {
      @statusCode statusCode: 200;
      @body comments: Comment[];
    }

    @post
    op createComment(@body body: CreateCommentRequest): CreateCommentResponse;

    model CreateCommentResponse {
      @statusCode statusCode: 201;
      @body comment: Comment;
    }

    @route("/{comment_id}")
    namespace CommentOps {
      @get
      op getComment(@path comment_id: string): GetCommentResponse;

      model GetCommentResponse {
        @statusCode statusCode: 200;
        @body comment: Comment;
      }

      @post
      op updateComment(@path comment_id: string, @body body: UpdateCommentRequest): UpdateCommentResponse;

      model UpdateCommentResponse {
        @statusCode statusCode: 200;
        @body comment: Comment;
      }

      @delete
      op deleteComment(@path comment_id: string): DeleteCommentResponse;

      model DeleteCommentResponse {
        @statusCode statusCode: 204;
      }
    }
  }

  model CreateLabelRequest {
    name: string;
    color?: string;
    order?: int32;
    is_favorite?: boolean;
  }

  model UpdateLabelRequest {
    name?: string;
    color?: string;
    order?: int32;
    is_favorite?: boolean;
  }

  model RenameSharedLabelRequest {
    name: string;
    new_name: string;
  }

  model RemoveSharedLabelRequest {
    name: string;
  }

  @route("/labels")
  namespace Labels {
    @get
    op getPersonalLabels(): GetPersonalLabelsResponse;

    model GetPersonalLabelsResponse {
      @statusCode statusCode: 200;
      @body labels: Label[];
    }

    @post
    op createLabel(@body body: CreateLabelRequest): CreateLabelResponse;

    model CreateLabelResponse {
      @statusCode statusCode: 201;
      @body label: Label;
    }

    @route("/{label_id}")
    namespace LabelOps {
      @get
      op getPersonalLabel(@path label_id: string): GetPersonalLabelResponse;

      model GetPersonalLabelResponse {
        @statusCode statusCode: 200;
        @body label: Label;
      }

      @post
      op updateLabel(@path label_id: string, @body body: UpdateLabelRequest): UpdateLabelResponse;

      model UpdateLabelResponse {
        @statusCode statusCode: 200;
        @body label: Label;
      }

      @delete
      op deleteLabel(@path label_id: string): DeleteLabelResponse;

      model DeleteLabelResponse {
        @statusCode statusCode: 204;
      }
    }

    @route("/shared")
    namespace SharedLabels {
      @get
      op getSharedLabels(): GetSharedLabelsResponse;

      model GetSharedLabelsResponse {
        @statusCode statusCode: 200;
        @body labels: Label[];
      }

      @route("/rename")
      @post
      op renameSharedLabel(@body body: RenameSharedLabelRequest): RenameSharedLabelResponse;

      model RenameSharedLabelResponse {
        @statusCode statusCode: 204;
      }

      @route("/remove")
      @post
      op removeSharedLabel(@body body: RemoveSharedLabelRequest): RemoveSharedLabelResponse;

      model RemoveSharedLabelResponse {
        @statusCode statusCode: 204;
      }
    }
  }
}