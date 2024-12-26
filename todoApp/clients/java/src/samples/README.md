# Sample for TodoApp client

## Prerequisite

Install [Java](https://docs.microsoft.com/java/openjdk/download) 17 or above. (Verify by running `java --version`)

Install [Maven](https://maven.apache.org/install.html). (Verify by running `mvn --version`)

## Start the server

Run `dotnet run --project <RepoRoot>/todoApp/servers/aspnet/Todo.csproj`.

## Build TodoApp Java SDK

Run `mvn clean package -DskipTests -f <RepoRoot>/todoApp/clients/java/pom.xml`.

## Run TodoApp Java sample

Run `mvn exec:java -f <RepoRoot>/todoApp/clients/java/pom.xml`.

Output be like
```
user created, id=0
todo item created, id=0
todo item queried, title=Buy milk
todo item updated, status=Completed
todo item in list, title=Buy milk, status=Completed
todo item deleted
```
