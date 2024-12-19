# Sample for PetStore client

## Overview

This sample contains a brief usage of the Python generated client for the PetStore TypeSpec API.

The operations include:
- create a pet
- get a pet from id
- update a pet by id
- list all available pets
- delete a pet by id

## How to run the sample

First, run the following command to start the server:
```
dotnet run --project <RepoRoot>/petstore/servers/aspnet/petstore.csproj
```

Create and activate your own Python virtual environment ([reference](https://docs.python.org/3/library/venv.html)), and install the library with:
```
python <RepoRoot>/petstore/clients/python/setup.py install
```

Then, run the following command to start the client in the current directory:
```
python sample.py
```