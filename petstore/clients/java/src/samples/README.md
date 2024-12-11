# Sample for PetStore client

## Prerequisite

Install [Java](https://docs.microsoft.com/java/openjdk/download) 17 or above. (Verify by running `java --version`)

Install [Maven](https://maven.apache.org/install.html). (Verify by running `mvn --version`)

## Install the clientcore library

Since `io.clientcore:core` library is not published to Maven, we need to build and install it locally.

1. Checkout [azure-sdk-for-java](https://github.com/Azure/azure-sdk-for-java) repository.
2. Use commit ID `259567d86d457b6d2d428278665ddbe48885c9bb`. Run `git checkout 259567d86d457b6d2d428278665ddbe48885c9bb`.
3. Build and install `io.clientcore:core`. Run `mvn install -pl io.clientcore:core -am` in its root directory.

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
