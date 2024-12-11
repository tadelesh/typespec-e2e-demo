# Sample for PetStore client

## Install the clientcore library

Since `io.clientcore:core` library is not published to Maven, we need to build and install it locally.

1. Checkout [azure-sdk-for-java](https://github.com/Azure/azure-sdk-for-java) repository. (if you already have the local checkout, please update it to latest "main" branch)
2. Build and install `io.clientcore:core`. Run `mvn install -pl io.clientcore:core -am` in its root directory.

## Start the server

Run `dotnet run --project petstore/servers/aspnet/petstore.csproj` in root directory of this `typespec-e2e-demo` repository.
