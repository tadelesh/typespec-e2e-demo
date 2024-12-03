import { HttpContext } from "../../tsp-output/@typespec/http-server-javascript/helpers/router.js";
import {
  Checkup,
  Checkups,
  PetStoreError,
} from "../../tsp-output/@typespec/http-server-javascript/models/all/pet-store.js";
import {
  CheckupUpdate,
  CheckupResourceCreatedResponse,
  CheckupCollectionWithNextLink,
} from "../../tsp-output/@typespec/http-server-javascript/models/all/typespec/rest/resource.js";

export class CheckupsImpl implements Checkups<HttpContext> {
  createOrUpdate(
    ctx: HttpContext,
    checkupId: number,
    resource: CheckupUpdate
  ): Promise<Checkup | CheckupResourceCreatedResponse | PetStoreError> {
    throw new Error("Method not implemented.");
  }
  list(
    ctx: HttpContext
  ): Promise<CheckupCollectionWithNextLink | PetStoreError> {
    throw new Error("Method not implemented.");
  }
}
