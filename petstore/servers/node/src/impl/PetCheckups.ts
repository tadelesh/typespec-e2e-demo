import { HttpContext } from "../../tsp-output/@typespec/http-server-javascript/helpers/router.js";
import {
  Checkup,
  PetCheckups,
  PetStoreError,
} from "../../tsp-output/@typespec/http-server-javascript/models/all/pet-store.js";
import {
  CheckupUpdate,
  CheckupResourceCreatedResponse,
  CheckupCollectionWithNextLink,
} from "../../tsp-output/@typespec/http-server-javascript/models/all/typespec/rest/resource.js";

export class PetCheckupsImpl implements PetCheckups<HttpContext> {
  createOrUpdate(
    ctx: HttpContext,
    petId: number,
    checkupId: number,
    resource: CheckupUpdate
  ): Promise<Checkup | CheckupResourceCreatedResponse | PetStoreError> {
    throw new Error("Method not implemented.");
  }
  list(
    ctx: HttpContext,
    petId: number
  ): Promise<CheckupCollectionWithNextLink | PetStoreError> {
    throw new Error("Method not implemented.");
  }
}
