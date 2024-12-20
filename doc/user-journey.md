# TypeSpec Out-of-box User Journey

## North Star

**We envision a seamless experience where TypeSpec users can leverage the `tsp init` command or VSCode to effortlessly create new projects. With intuitive options to select from a variety of emitters, users can kickstart their projects with confidence, knowing that each selected emitter is fully integrated, properly configured, and ready to work out-of-the-box. This empowers developers to focus on designing great APIs without being burdened by setup complexities.**

This document outlines the streamlined user experience for creating and working with a TypeSpec project, from the initial setup to generating client and server projects. It provides guidance on two primary workflows:

- [Using the Command-Line Interface (CLI)](#cli)
- [Using the Visual Studio Code (VSCode) IDE with the TypeSpec Extension](#vscode)

These workflows are designed to offer a seamless and productive experience for new and experienced users alike, ensuring they can get started quickly while exploring the full capabilities of TypeSpec.

## CLI

### Overview

Leveraging built-in or separate [test template file](../tsptemplate.json), `tsp init` provides a convenient way to scaffold TypeSpec projects. [The tsptemplate.json](../tsptemplate.json) contains list of known client and server emitters for you to choose from. We can decide later if we will make this a built-in template.

- You can use `sandbox` folder to test out the CLI experience.
- During `npx tsp init`, you will be prompted to select include different protocol/client/server emitters.
- Please review the post creation message and install any development kit required for that language.

```bash
# Available Project Spec: widget, petstore, todoApp. Replace XXXX with one of these.
cd sandbox
md XXXX && cd XXXX

# In emitter selection step, you can multi-select various client/server emitters. PLEASE leave `openapi3` emitter selected.
npx tsp init ../../tsptemplate.json

# Replace default empty main.tsp with actual spec
copy ../../XXXX/spec/main.tsp

npm install

# This should generate openapi and any selected client and/or server code.
npx tsp compile .
```

Once the above steps are completed, you should see the following folder structure depending on the emitters you have selected.
```
    \XXXX
        \openapi                    # Generated OpenAPI 3.0 spec
            openapi.yaml
        \clients                    # Generated Client SDK for selected language
            \dotnet
            \java
            ...
        \servers                    # Generated Server Code
            \aspnet
            \node
        main.tsp
        tspconfig.yaml
        package.json
```

### Compile Client SDKs

If you have selected client emitters, you can use the following commands to compile the client project in the client sdk folder.

| **Language** | **Command**                |
| ------------ | -------------------------- |
| C#           | `dotnet build`             |
| Java         | `mvn package`              |
| Python       | N/A                        |
| JS/TS        | `npm install && npm build` |

### Compile and Test Server

Server implementations are often highly opinionated and customized. To broaden the appeal and usability of the TypeSpec service emitter, it is crucial to support multiple levels of layered generated artifacts. For instance, the output could range from generating just models, to models with routers and controller/handler interfaces, and even to a fully functioning stack that includes mocked or basic service stubs, or a complete runnable project scaffolding. While these advanced features are planned next, the current emitters do not yet support generating basic service stubs or scaffolding entire projects. As a result, some custom steps are necessary until these additional capabilities are available. Instructions for each demo specification are provided in individual files—please refer to the table below for links to complete debug solutions.

The ultimate goal is to eliminate or significantly simplify these steps by enabling out-of-the-box runnable projects through the emission of basic functional projects and service stubs. Once these features are implemented, this section will be updated accordingly.

#### Scaffolding Instruction

| **Web Stack** | **Widget Instruction** | **PetStore Instruction**       | **ToDoApp Instruction** |
| ------------- | ---------------------- | ------------------------------ | ----------------------- |
| asp.net       | [Widget](.)            | [PetStore](petstore-aspnet.md) | TBA                     |
| node/express  | TBA                    | TBA                            | TBA                     |

#### Server Run/Test Instruction

- asp.net: 
  - Run `dotnet run`
  - use browser to `http://localhost:XXXX/swagger/index.html` where XXXX is the port number shown
  - You can use Swagger UI's `Try it out` to interact with the running service

- node/express: TBA

## VSCode

TBA
