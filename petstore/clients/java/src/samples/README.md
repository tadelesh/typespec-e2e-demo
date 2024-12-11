# Sample for PetStore client

## Install the clientcore library

Since `io.clientcore:core` library is not published to Maven, we need to build and install it locally.

1. Checkout [azure-sdk-for-java](https://github.com/Azure/azure-sdk-for-java) repository.
2. Use commit ID `259567d86d457b6d2d428278665ddbe48885c9bb`. Run `git checkout 259567d86d457b6d2d428278665ddbe48885c9bb`.
3. Build and install `io.clientcore:core`. Run `mvn install -pl io.clientcore:core -am` in its root directory.

## Start the server

Run `dotnet run --project <RepoRoot>/petstore/servers/aspnet/petstore.csproj`.

## Build PetStore

Run `mvn clean package -DskipTests -f <RepoRoot>/petstore/clients/java/pom.xml`.

## Run PetStore Java sample

Run `mvn exec:java -f <RepoRoot>/petstore/clients/java/pom.xml`.
