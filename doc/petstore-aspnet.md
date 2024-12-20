# Temp Scaffolding Instructions

If you have not created a TypeSpec project for PetStore, please [create that first](./user-journey.md#overview). 

Assuming you have successfully ran `npx tsp compile .` and generated server code. Run following command to create asp.net project and copy over functional service stub code.

```bash
# Create asp.net project 
cd ./sandbox/petstore/servers/aspnet
dotnet new web
dotnet add package Swashbuckle.AspNetCore

copy ../../../../petstore/servers/aspnet/Program.cs
copy ../../../../petstore/servers/aspnet/CustomExceptionFilter.cs
copy ../../../../petstore/servers/aspnet/Controllers/ . -recurse
copy ../../../../petstore/servers/aspnet/ServiceStubs/ . -recurse  
copy ../../../../petstore/servers/aspnet/Exceptions/ . -recurse  

# should yield no error
dotnet build
```

You can then follow [the instructions](user-journey.md#server-runtest-instruction) to test the server.