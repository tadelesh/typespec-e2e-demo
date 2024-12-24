# Sample for PetStore client

## Prerequisite

Install [Java](https://docs.microsoft.com/java/openjdk/download) 17 or above. (Verify by running `java --version`)

Install [Maven](https://maven.apache.org/install.html). (Verify by running `mvn --version`)

## Start the server

Run `dotnet run --project <RepoRoot>/petstore/servers/aspnet/petstore.csproj`.

## Build PetStore Java SDK

Run `mvn clean package -DskipTests -f <RepoRoot>/petstore/clients/java/pom.xml`.

## Run PetStore Java sample

Run `mvn exec:java -f <RepoRoot>/petstore/clients/java/pom.xml`.

Output be like
```
pet created, id=0
pet queried, name=Kiwi
pet updated, age=8
pet deleted, id=0
```
