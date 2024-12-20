# TypeSpec E2E Demo Repo

This repository contains a number of TypeSpec API specifications and has been set up to test generated client and server code.

As the server implementations vary, TypeSpec service emitters currently only generate API artifacts such as Models and Controllers as building blocks. This allows automatic updates to the service API and eliminates the need to manually keep them in sync with the API definitions.

With these generated building blocks, you will still need service scaffolding and business logic for a runnable server. However, in this repository, scaffolding code and minimal service stub code have been added so that the demo server projects can all be started for testing. README.md in `/servers` and each of service folders will provide more information.

If you wish to recreate this folder from scratch or review the scaffolding steps, please see [this guide](./how-to-test-server-api.md).

## Prerequisites

Before you begin, ensure you have met the following requirements:

- You have installed [Node.js](https://nodejs.org/) (version 14.x or later).
- You have installed [npm](https://www.npmjs.com/) (version 6.x or later).
- To test C#/ASP.NET service, please install [.NET](https://dotnet.microsoft.com/en-us/download) (version 8.0 or later).

## Repo Initialization

Run the following command **once or every time `package.json` is updated**:

```sh
npm install
```

## Take TypeSpec For a Spin

To experience the API First development with TypeSpec from scratch, please see [user-journey](./doc/user-journey.md)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
