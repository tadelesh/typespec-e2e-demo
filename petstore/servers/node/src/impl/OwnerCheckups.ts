import { HttpContext } from "../../tsp-output/@typespec/http-server-javascript/helpers/router.js";
import {
  Checkup,
  OwnerCheckups,
  PetStoreError,
} from "../../tsp-output/@typespec/http-server-javascript/models/all/pet-store.js";
import {
  CheckupUpdate,
  CheckupResourceCreatedResponse,
  CheckupCollectionWithNextLink,
} from "../../tsp-output/@typespec/http-server-javascript/models/all/typespec/rest/resource.js";

export class OwnerCheckupsImpl implements OwnerCheckups<HttpContext> {
  createOrUpdate(
    ctx: HttpContext,
    ownerId: bigint,
    checkupId: number,
    resource: CheckupUpdate
  ): Promise<Checkup | CheckupResourceCreatedResponse | PetStoreError> {
    throw new Error("Method not implemented.");
  }
  list(
    ctx: HttpContext,
    ownerId: bigint
  ): Promise<CheckupCollectionWithNextLink | PetStoreError> {
    throw new Error("Method not implemented.");
  }
}
