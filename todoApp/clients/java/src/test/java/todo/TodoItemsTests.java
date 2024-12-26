package todo;

import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.api.Test;
import todo.todoitems.TodoItemPatch;
import todo.todoitems.TodoPage;

public class TodoItemsTests {

    private final TodoClientBuilder builder = new TodoClientBuilder()
            .endpoint("http://localhost:5244/");
    private final TodoItemsClient client = builder.buildTodoItemsClient();

    @Test
    public void test() {
        // create item
        CreateJsonResponse createTodoItemResponse = client.createJson(
                new TodoItem("Buy milk", TodoItemStatus.IN_PROGRESS)
                        .setDescription("Need to buy milk").setAssignedTo(1L));
        long todoItemId = createTodoItemResponse.getId();
        Assertions.assertEquals("Buy milk", createTodoItemResponse.getTitle());
        Assertions.assertEquals(TodoItemStatus.IN_PROGRESS, createTodoItemResponse.getStatus());

        // get item
        GetResponse getTodoItemResponse = client.get(todoItemId);
        Assertions.assertEquals(1L, getTodoItemResponse.getAssignedTo());

        // update item
        UpdateResponse updateTodoItemResponse = client.update(todoItemId, new TodoItemPatch().setStatus(TodoItemPatchStatus.COMPLETED));
        Assertions.assertEquals(TodoItemStatus.COMPLETED, updateTodoItemResponse.getStatus());

        // TODO pageable
        // list items
        TodoPage todoItemsPage = client.list();
        Assertions.assertEquals(1L, todoItemsPage.getItems().size());
        Assertions.assertEquals("Need to buy milk", todoItemsPage.getItems().get(0).getDescription());

        // delete item
        client.delete(todoItemId);
    }
}
