# TodoApp ASP.NET WebAPI project

The current folder contains ASP.NET core basic project with basic service stub code for out of box run-ability.

## Testing the server code

[Follow these steps](../../../how-to-test-server-api.md)

## How the server implements the API

The spec contains three parts:
- `Users`
- `TodoItems`
- `TodoItems.Attachments`

All operations are implemented with internal memory storage.

For create operations, the server will echo your request back and update the internal storage with an id `0` (see the next section for details).

For get and list operations, the server will query the internal storage and give back the results.

For delete operations, the server will remove the item from the internal storage, therefore next time you call get using that id should get an error.

### Possible issues and questions

1. `Users.create`

The request body in `Users.create` has `@key` on the request body, but because this operation is not using the template, therefore there is no approach that the client could send the id to the server.
The current implementation will always return 0 as id. And if you call create with a different body, it will override the old user.
