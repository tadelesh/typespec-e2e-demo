Set-Location (Resolve-Path (Join-Path $PSScriptRoot '..' '..' '..'))

# Generate
Remove-Item ./petstore/clients/java/src/main -Recurse -Force
Push-Location ./petstore/spec
npx --no-install tsp compile . --emit "@typespec/http-client-java"
Pop-Location

Remove-Item ./todoApp/clients/java/src/main -Recurse -Force
Push-Location ./todoApp/spec
npx --no-install tsp compile . --emit "@typespec/http-client-java"
Pop-Location

# Build (currently require a local install of io.clientcore:core)
Push-Location ./petstore/clients/java
mvn package -DskipTests
Pop-Location

Push-Location ./todoApp/clients/java
mvn package -DskipTests
Pop-Location
