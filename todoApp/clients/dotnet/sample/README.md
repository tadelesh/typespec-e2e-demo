# Sample for TodoApp client

## Overview

This sample contains a brief usage of the .Net generated client for the PetStore TypeSpec API.

The operations include:
- create a user
- get a non-exist todo item
- create a todo item
- get the created todo item
- list all available todo items
- delete the todo item

## How to run the sample

First, run the following command to start the server:
```
dotnet run --project <RepoRoot>/todoApp/servers/aspnet/Todo.csproj
```

Then, run the following command to start the client in the current directory:
```
dotnet run
```
