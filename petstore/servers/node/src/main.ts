import express from "express";

import morgan from "morgan";
import { createPetStoreRouter } from "../tsp-output/@typespec/http-server-javascript/http/router.js";
import { CheckupsImpl } from "./impl/Checkups.js";
import { OwnerCheckupsImpl } from "./impl/OwnerCheckups.js";
import { OwnerInsuranceImpl } from "./impl/OwnerInsurance.js";
import { OwnersImpl } from "./impl/Owners.js";
import { PetCheckupsImpl } from "./impl/PetCheckups.js";
import { PetInsuranceImpl } from "./impl/PetInsurance.js";
import { PetsImpl } from "./impl/Pets.js";
import { ToyInsuranceImpl } from "./impl/ToyInsurance.js";
import { ToysImpl } from "./impl/Toys.js";

const app = express();
app.use(morgan("dev"));

function isStatusCode(v: any): v is number {
  return typeof v === "number" && v >= 100 && v < 600 && Number.isInteger(v);
}

const router = createPetStoreRouter(
  new PetsImpl(),
  new PetCheckupsImpl(),
  new PetInsuranceImpl(),
  new ToysImpl(),
  new ToyInsuranceImpl(),
  new CheckupsImpl(),
  new OwnersImpl(),
  new OwnerCheckupsImpl(),
  new OwnerInsuranceImpl(),
  {
    onInternalError(error: any, _request, response) {
      response.statusCode = isStatusCode(error.statusCode)
        ? error.statusCode
        : 500;

      const message =
        error instanceof Error
          ? error.message
          : typeof error === "string"
            ? error
            : "An internal error occurred";

      response.end(
        JSON.stringify({
          message,
        })
      );
    },
  }
);

app.use(router.expressMiddleware);

const port = process.env["PORT"] ?? 8080;

app.listen(port, () => {
  console.log(`Demo Service: Listening on port ${port}`);
});
