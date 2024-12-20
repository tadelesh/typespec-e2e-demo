# coding=utf-8

# pylint: disable=useless-super-delegation

import datetime
from typing import Any, List, Literal, Mapping, Optional, TYPE_CHECKING, overload

from .. import _model_base
from .._model_base import rest_field
from .._vendor import FileType

if TYPE_CHECKING:
    from .. import _types, models as _models


class ApiError(_model_base.Model):
    """ApiError.

    All required parameters must be populated in order to send to server.

    :ivar code: A machine readable error code. Required.
    :vartype code: str
    :ivar message: A human readable message. Required.
    :vartype message: str
    """

    code: str = rest_field()
    """A machine readable error code. Required."""
    message: str = rest_field()
    """A human readable message. Required."""

    @overload
    def __init__(
        self,
        *,
        code: str,
        message: str,
    ) -> None: ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]) -> None:
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)


class CreateFormResponse(_model_base.Model):
    """CreateFormResponse.

    Readonly variables are only populated by the server, and will be ignored when sending a request.


    :ivar id: The item's unique id. Required.
    :vartype id: int
    :ivar title: The item's title. Required.
    :vartype title: str
    :ivar created_by: User that created the todo. Required.
    :vartype created_by: int
    :ivar assigned_to: User that the todo is assigned to.
    :vartype assigned_to: int
    :ivar description: A longer description of the todo item in markdown format.
    :vartype description: str
    :ivar status: The status of the todo item. Required. Is one of the following types:
     Literal["NotStarted"], Literal["InProgress"], Literal["Completed"]
    :vartype status: str or str or str
    :ivar created_at: When the todo item was created. Required.
    :vartype created_at: ~datetime.datetime
    :ivar updated_at: When the todo item was last updated. Required.
    :vartype updated_at: ~datetime.datetime
    :ivar completed_at: When the todo item was makred as completed.
    :vartype completed_at: ~datetime.datetime
    :ivar labels: Is one of the following types: str, [str], TodoLabelRecord, [TodoLabelRecord]
    :vartype labels: str or list[str] or ~todo.models.TodoLabelRecord or
     list[~todo.models.TodoLabelRecord]
    """

    id: int = rest_field(visibility=["read"])
    """The item's unique id. Required."""
    title: str = rest_field()
    """The item's title. Required."""
    created_by: int = rest_field(name="createdBy", visibility=["read"])
    """User that created the todo. Required."""
    assigned_to: Optional[int] = rest_field(name="assignedTo")
    """User that the todo is assigned to."""
    description: Optional[str] = rest_field()
    """A longer description of the todo item in markdown format."""
    status: Literal["NotStarted", "InProgress", "Completed"] = rest_field()
    """The status of the todo item. Required. Is one of the following types: Literal[\"NotStarted\"],
     Literal[\"InProgress\"], Literal[\"Completed\"]"""
    created_at: datetime.datetime = rest_field(name="createdAt", visibility=["read"], format="rfc3339")
    """When the todo item was created. Required."""
    updated_at: datetime.datetime = rest_field(name="updatedAt", visibility=["read"], format="rfc3339")
    """When the todo item was last updated. Required."""
    completed_at: Optional[datetime.datetime] = rest_field(name="completedAt", visibility=["read"], format="rfc3339")
    """When the todo item was makred as completed."""
    labels: Optional["_types.TodoLabels"] = rest_field()
    """Is one of the following types: str, [str], TodoLabelRecord, [TodoLabelRecord]"""

    @overload
    def __init__(
        self,
        *,
        title: str,
        status: Literal["NotStarted", "InProgress", "Completed"],
        assigned_to: Optional[int] = None,
        description: Optional[str] = None,
        labels: Optional["_types.TodoLabels"] = None,
    ) -> None: ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]) -> None:
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)


class CreateJsonResponse(_model_base.Model):
    """CreateJsonResponse.

    Readonly variables are only populated by the server, and will be ignored when sending a request.


    :ivar id: The item's unique id. Required.
    :vartype id: int
    :ivar title: The item's title. Required.
    :vartype title: str
    :ivar created_by: User that created the todo. Required.
    :vartype created_by: int
    :ivar assigned_to: User that the todo is assigned to.
    :vartype assigned_to: int
    :ivar description: A longer description of the todo item in markdown format.
    :vartype description: str
    :ivar status: The status of the todo item. Required. Is one of the following types:
     Literal["NotStarted"], Literal["InProgress"], Literal["Completed"]
    :vartype status: str or str or str
    :ivar created_at: When the todo item was created. Required.
    :vartype created_at: ~datetime.datetime
    :ivar updated_at: When the todo item was last updated. Required.
    :vartype updated_at: ~datetime.datetime
    :ivar completed_at: When the todo item was makred as completed.
    :vartype completed_at: ~datetime.datetime
    :ivar labels: Is one of the following types: str, [str], TodoLabelRecord, [TodoLabelRecord]
    :vartype labels: str or list[str] or ~todo.models.TodoLabelRecord or
     list[~todo.models.TodoLabelRecord]
    """

    id: int = rest_field(visibility=["read"])
    """The item's unique id. Required."""
    title: str = rest_field()
    """The item's title. Required."""
    created_by: int = rest_field(name="createdBy", visibility=["read"])
    """User that created the todo. Required."""
    assigned_to: Optional[int] = rest_field(name="assignedTo")
    """User that the todo is assigned to."""
    description: Optional[str] = rest_field()
    """A longer description of the todo item in markdown format."""
    status: Literal["NotStarted", "InProgress", "Completed"] = rest_field()
    """The status of the todo item. Required. Is one of the following types: Literal[\"NotStarted\"],
     Literal[\"InProgress\"], Literal[\"Completed\"]"""
    created_at: datetime.datetime = rest_field(name="createdAt", visibility=["read"], format="rfc3339")
    """When the todo item was created. Required."""
    updated_at: datetime.datetime = rest_field(name="updatedAt", visibility=["read"], format="rfc3339")
    """When the todo item was last updated. Required."""
    completed_at: Optional[datetime.datetime] = rest_field(name="completedAt", visibility=["read"], format="rfc3339")
    """When the todo item was makred as completed."""
    labels: Optional["_types.TodoLabels"] = rest_field()
    """Is one of the following types: str, [str], TodoLabelRecord, [TodoLabelRecord]"""

    @overload
    def __init__(
        self,
        *,
        title: str,
        status: Literal["NotStarted", "InProgress", "Completed"],
        assigned_to: Optional[int] = None,
        description: Optional[str] = None,
        labels: Optional["_types.TodoLabels"] = None,
    ) -> None: ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]) -> None:
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)


class CreateResponse(_model_base.Model):
    """CreateResponse.

    Readonly variables are only populated by the server, and will be ignored when sending a request.


    :ivar id: An autogenerated unique id for the user. Required.
    :vartype id: int
    :ivar username: The user's username. Required.
    :vartype username: str
    :ivar email: The user's email address. Required.
    :vartype email: str
    :ivar token: The token to use to construct the validate email address url. Required.
    :vartype token: str
    """

    id: int = rest_field(visibility=["read"])
    """An autogenerated unique id for the user. Required."""
    username: str = rest_field()
    """The user's username. Required."""
    email: str = rest_field()
    """The user's email address. Required."""
    token: str = rest_field()
    """The token to use to construct the validate email address url. Required."""

    @overload
    def __init__(
        self,
        *,
        username: str,
        email: str,
        token: str,
    ) -> None: ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]) -> None:
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)


class FileAttachmentMultipartRequest(_model_base.Model):
    """FileAttachmentMultipartRequest.

    All required parameters must be populated in order to send to server.

    :ivar contents: Required.
    :vartype contents: ~todo._vendor.FileType
    """

    contents: FileType = rest_field(is_multipart_file_input=True)
    """Required."""

    @overload
    def __init__(
        self,
        *,
        contents: FileType,
    ) -> None: ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]) -> None:
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)


class GetResponse(_model_base.Model):
    """GetResponse.

    Readonly variables are only populated by the server, and will be ignored when sending a request.


    :ivar id: The item's unique id. Required.
    :vartype id: int
    :ivar title: The item's title. Required.
    :vartype title: str
    :ivar created_by: User that created the todo. Required.
    :vartype created_by: int
    :ivar assigned_to: User that the todo is assigned to.
    :vartype assigned_to: int
    :ivar description: A longer description of the todo item in markdown format.
    :vartype description: str
    :ivar status: The status of the todo item. Required. Is one of the following types:
     Literal["NotStarted"], Literal["InProgress"], Literal["Completed"]
    :vartype status: str or str or str
    :ivar created_at: When the todo item was created. Required.
    :vartype created_at: ~datetime.datetime
    :ivar updated_at: When the todo item was last updated. Required.
    :vartype updated_at: ~datetime.datetime
    :ivar completed_at: When the todo item was makred as completed.
    :vartype completed_at: ~datetime.datetime
    :ivar labels: Is one of the following types: str, [str], TodoLabelRecord, [TodoLabelRecord]
    :vartype labels: str or list[str] or ~todo.models.TodoLabelRecord or
     list[~todo.models.TodoLabelRecord]
    """

    id: int = rest_field(visibility=["read"])
    """The item's unique id. Required."""
    title: str = rest_field()
    """The item's title. Required."""
    created_by: int = rest_field(name="createdBy", visibility=["read"])
    """User that created the todo. Required."""
    assigned_to: Optional[int] = rest_field(name="assignedTo")
    """User that the todo is assigned to."""
    description: Optional[str] = rest_field()
    """A longer description of the todo item in markdown format."""
    status: Literal["NotStarted", "InProgress", "Completed"] = rest_field()
    """The status of the todo item. Required. Is one of the following types: Literal[\"NotStarted\"],
     Literal[\"InProgress\"], Literal[\"Completed\"]"""
    created_at: datetime.datetime = rest_field(name="createdAt", visibility=["read"], format="rfc3339")
    """When the todo item was created. Required."""
    updated_at: datetime.datetime = rest_field(name="updatedAt", visibility=["read"], format="rfc3339")
    """When the todo item was last updated. Required."""
    completed_at: Optional[datetime.datetime] = rest_field(name="completedAt", visibility=["read"], format="rfc3339")
    """When the todo item was makred as completed."""
    labels: Optional["_types.TodoLabels"] = rest_field()
    """Is one of the following types: str, [str], TodoLabelRecord, [TodoLabelRecord]"""

    @overload
    def __init__(
        self,
        *,
        title: str,
        status: Literal["NotStarted", "InProgress", "Completed"],
        assigned_to: Optional[int] = None,
        description: Optional[str] = None,
        labels: Optional["_types.TodoLabels"] = None,
    ) -> None: ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]) -> None:
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)


class InvalidTodoItem(ApiError):
    """InvalidTodoItem.

    All required parameters must be populated in order to send to server.

    :ivar code: A machine readable error code. Required.
    :vartype code: str
    :ivar message: A human readable message. Required.
    :vartype message: str
    """

    @overload
    def __init__(
        self,
        *,
        code: str,
        message: str,
    ) -> None: ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]) -> None:
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)


class InvalidUserResponse(ApiError):
    """The user is invalid (e.g. forgot to enter email address).

    Readonly variables are only populated by the server, and will be ignored when sending a request.

    All required parameters must be populated in order to send to server.

    :ivar message: A human readable message. Required.
    :vartype message: str
    :ivar code: Required. Default value is "invalid-user".
    :vartype code: str
    """

    code: Literal["invalid-user"] = rest_field()
    """Required. Default value is \"invalid-user\"."""

    @overload
    def __init__(
        self,
        *,
        message: str,
    ) -> None: ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]) -> None:
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
        self.code: Literal["invalid-user"] = "invalid-user"


class NotFoundErrorResponse(_model_base.Model):
    """NotFoundErrorResponse.

    Readonly variables are only populated by the server, and will be ignored when sending a request.

    All required parameters must be populated in order to send to server.

    :ivar code: Required. Default value is "not-found".
    :vartype code: str
    """

    code: Literal["not-found"] = rest_field()
    """Required. Default value is \"not-found\"."""

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
        self.code: Literal["not-found"] = "not-found"


class Standard4XXResponse(ApiError):
    """Something is wrong with you.

    All required parameters must be populated in order to send to server.

    :ivar code: A machine readable error code. Required.
    :vartype code: str
    :ivar message: A human readable message. Required.
    :vartype message: str
    """

    @overload
    def __init__(
        self,
        *,
        code: str,
        message: str,
    ) -> None: ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]) -> None:
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)


class Standard5XXResponse(ApiError):
    """Something is wrong with me.

    All required parameters must be populated in order to send to server.

    :ivar code: A machine readable error code. Required.
    :vartype code: str
    :ivar message: A human readable message. Required.
    :vartype message: str
    """

    @overload
    def __init__(
        self,
        *,
        code: str,
        message: str,
    ) -> None: ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]) -> None:
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)


class TodoAttachment(_model_base.Model):
    """TodoAttachment.


    :ivar filename: The file name of the attachment. Required.
    :vartype filename: str
    :ivar media_type: The media type of the attachment. Required.
    :vartype media_type: str
    :ivar contents: The contents of the file. Required.
    :vartype contents: bytes
    """

    filename: str = rest_field()
    """The file name of the attachment. Required."""
    media_type: str = rest_field(name="mediaType")
    """The media type of the attachment. Required."""
    contents: bytes = rest_field(format="base64")
    """The contents of the file. Required."""

    @overload
    def __init__(
        self,
        *,
        filename: str,
        media_type: str,
        contents: bytes,
    ) -> None: ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]) -> None:
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)


class TodoItem(_model_base.Model):
    """TodoItem.

    Readonly variables are only populated by the server, and will be ignored when sending a request.


    :ivar id: The item's unique id. Required.
    :vartype id: int
    :ivar title: The item's title. Required.
    :vartype title: str
    :ivar created_by: User that created the todo. Required.
    :vartype created_by: int
    :ivar assigned_to: User that the todo is assigned to.
    :vartype assigned_to: int
    :ivar description: A longer description of the todo item in markdown format.
    :vartype description: str
    :ivar status: The status of the todo item. Required. Is one of the following types:
     Literal["NotStarted"], Literal["InProgress"], Literal["Completed"]
    :vartype status: str or str or str
    :ivar created_at: When the todo item was created. Required.
    :vartype created_at: ~datetime.datetime
    :ivar updated_at: When the todo item was last updated. Required.
    :vartype updated_at: ~datetime.datetime
    :ivar completed_at: When the todo item was makred as completed.
    :vartype completed_at: ~datetime.datetime
    :ivar labels: Is one of the following types: str, [str], TodoLabelRecord, [TodoLabelRecord]
    :vartype labels: str or list[str] or ~todo.models.TodoLabelRecord or
     list[~todo.models.TodoLabelRecord]
    :ivar _dummy:
    :vartype _dummy: str
    """

    id: int = rest_field(visibility=["read"])
    """The item's unique id. Required."""
    title: str = rest_field()
    """The item's title. Required."""
    created_by: int = rest_field(name="createdBy", visibility=["read"])
    """User that created the todo. Required."""
    assigned_to: Optional[int] = rest_field(name="assignedTo")
    """User that the todo is assigned to."""
    description: Optional[str] = rest_field()
    """A longer description of the todo item in markdown format."""
    status: Literal["NotStarted", "InProgress", "Completed"] = rest_field()
    """The status of the todo item. Required. Is one of the following types: Literal[\"NotStarted\"],
     Literal[\"InProgress\"], Literal[\"Completed\"]"""
    created_at: datetime.datetime = rest_field(name="createdAt", visibility=["read"], format="rfc3339")
    """When the todo item was created. Required."""
    updated_at: datetime.datetime = rest_field(name="updatedAt", visibility=["read"], format="rfc3339")
    """When the todo item was last updated. Required."""
    completed_at: Optional[datetime.datetime] = rest_field(name="completedAt", visibility=["read"], format="rfc3339")
    """When the todo item was makred as completed."""
    labels: Optional["_types.TodoLabels"] = rest_field()
    """Is one of the following types: str, [str], TodoLabelRecord, [TodoLabelRecord]"""
    _dummy: Optional[str] = rest_field(visibility=["create"])

    @overload
    def __init__(
        self,
        *,
        title: str,
        status: Literal["NotStarted", "InProgress", "Completed"],
        assigned_to: Optional[int] = None,
        description: Optional[str] = None,
        labels: Optional["_types.TodoLabels"] = None,
        _dummy: Optional[str] = None,
    ) -> None: ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]) -> None:
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)


class ToDoItemMultipartRequest(_model_base.Model):
    """ToDoItemMultipartRequest.

    All required parameters must be populated in order to send to server.

    :ivar item: Required.
    :vartype item: ~todo.models.TodoItem
    :ivar attachments:
    :vartype attachments: list[~todo._vendor.FileType]
    """

    item: "_models.TodoItem" = rest_field()
    """Required."""
    attachments: Optional[List[FileType]] = rest_field(is_multipart_file_input=True)

    @overload
    def __init__(
        self,
        *,
        item: "_models.TodoItem",
        attachments: Optional[List[FileType]] = None,
    ) -> None: ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]) -> None:
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)


class TodoItemPatch(_model_base.Model):
    """TodoItemPatch.

    :ivar title: The item's title.
    :vartype title: str
    :ivar assigned_to: User that the todo is assigned to.
    :vartype assigned_to: int
    :ivar description: A longer description of the todo item in markdown format.
    :vartype description: str
    :ivar status: The status of the todo item. Is one of the following types:
     Literal["NotStarted"], Literal["InProgress"], Literal["Completed"]
    :vartype status: str or str or str
    """

    title: Optional[str] = rest_field()
    """The item's title."""
    assigned_to: Optional[int] = rest_field(name="assignedTo")
    """User that the todo is assigned to."""
    description: Optional[str] = rest_field()
    """A longer description of the todo item in markdown format."""
    status: Optional[Literal["NotStarted", "InProgress", "Completed"]] = rest_field()
    """The status of the todo item. Is one of the following types: Literal[\"NotStarted\"],
     Literal[\"InProgress\"], Literal[\"Completed\"]"""

    @overload
    def __init__(
        self,
        *,
        title: Optional[str] = None,
        assigned_to: Optional[int] = None,
        description: Optional[str] = None,
        status: Optional[Literal["NotStarted", "InProgress", "Completed"]] = None,
    ) -> None: ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]) -> None:
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)


class TodoLabelRecord(_model_base.Model):
    """TodoLabelRecord.


    :ivar name: Required.
    :vartype name: str
    :ivar color:
    :vartype color: str
    """

    name: str = rest_field()
    """Required."""
    color: Optional[str] = rest_field()

    @overload
    def __init__(
        self,
        *,
        name: str,
        color: Optional[str] = None,
    ) -> None: ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]) -> None:
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)


class UpdateResponse(_model_base.Model):
    """UpdateResponse.

    Readonly variables are only populated by the server, and will be ignored when sending a request.


    :ivar id: The item's unique id. Required.
    :vartype id: int
    :ivar title: The item's title. Required.
    :vartype title: str
    :ivar created_by: User that created the todo. Required.
    :vartype created_by: int
    :ivar assigned_to: User that the todo is assigned to.
    :vartype assigned_to: int
    :ivar description: A longer description of the todo item in markdown format.
    :vartype description: str
    :ivar status: The status of the todo item. Required. Is one of the following types:
     Literal["NotStarted"], Literal["InProgress"], Literal["Completed"]
    :vartype status: str or str or str
    :ivar created_at: When the todo item was created. Required.
    :vartype created_at: ~datetime.datetime
    :ivar updated_at: When the todo item was last updated. Required.
    :vartype updated_at: ~datetime.datetime
    :ivar completed_at: When the todo item was makred as completed.
    :vartype completed_at: ~datetime.datetime
    :ivar labels: Is one of the following types: str, [str], TodoLabelRecord, [TodoLabelRecord]
    :vartype labels: str or list[str] or ~todo.models.TodoLabelRecord or
     list[~todo.models.TodoLabelRecord]
    """

    id: int = rest_field(visibility=["read"])
    """The item's unique id. Required."""
    title: str = rest_field()
    """The item's title. Required."""
    created_by: int = rest_field(name="createdBy", visibility=["read"])
    """User that created the todo. Required."""
    assigned_to: Optional[int] = rest_field(name="assignedTo")
    """User that the todo is assigned to."""
    description: Optional[str] = rest_field()
    """A longer description of the todo item in markdown format."""
    status: Literal["NotStarted", "InProgress", "Completed"] = rest_field()
    """The status of the todo item. Required. Is one of the following types: Literal[\"NotStarted\"],
     Literal[\"InProgress\"], Literal[\"Completed\"]"""
    created_at: datetime.datetime = rest_field(name="createdAt", visibility=["read"], format="rfc3339")
    """When the todo item was created. Required."""
    updated_at: datetime.datetime = rest_field(name="updatedAt", visibility=["read"], format="rfc3339")
    """When the todo item was last updated. Required."""
    completed_at: Optional[datetime.datetime] = rest_field(name="completedAt", visibility=["read"], format="rfc3339")
    """When the todo item was makred as completed."""
    labels: Optional["_types.TodoLabels"] = rest_field()
    """Is one of the following types: str, [str], TodoLabelRecord, [TodoLabelRecord]"""

    @overload
    def __init__(
        self,
        *,
        title: str,
        status: Literal["NotStarted", "InProgress", "Completed"],
        assigned_to: Optional[int] = None,
        description: Optional[str] = None,
        labels: Optional["_types.TodoLabels"] = None,
    ) -> None: ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]) -> None:
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)


class User(_model_base.Model):
    """User.

    Readonly variables are only populated by the server, and will be ignored when sending a request.

    All required parameters must be populated in order to send to server.

    :ivar id: An autogenerated unique id for the user. Required.
    :vartype id: int
    :ivar username: The user's username. Required.
    :vartype username: str
    :ivar email: The user's email address. Required.
    :vartype email: str
    :ivar password: The user's password, provided when creating a user
     but is otherwise not visible (and hashed by the backend). Required.
    :vartype password: str
    """

    id: int = rest_field(visibility=["read"])
    """An autogenerated unique id for the user. Required."""
    username: str = rest_field()
    """The user's username. Required."""
    email: str = rest_field()
    """The user's email address. Required."""
    password: str = rest_field(visibility=["create"])
    """The user's password, provided when creating a user
     but is otherwise not visible (and hashed by the backend). Required."""

    @overload
    def __init__(
        self,
        *,
        username: str,
        email: str,
        password: str,
    ) -> None: ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]) -> None:
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)


class UserExistsResponse(ApiError):
    """The user already exists.

    Readonly variables are only populated by the server, and will be ignored when sending a request.

    All required parameters must be populated in order to send to server.

    :ivar message: A human readable message. Required.
    :vartype message: str
    :ivar code: Required. Default value is "user-exists".
    :vartype code: str
    """

    code: Literal["user-exists"] = rest_field()
    """Required. Default value is \"user-exists\"."""

    @overload
    def __init__(
        self,
        *,
        message: str,
    ) -> None: ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]) -> None:
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
        self.code: Literal["user-exists"] = "user-exists"
