import { HttpContext } from "../../tsp-output/@typespec/http-server-javascript/helpers/router.js";
import {
  Pet,
  Pets,
  PetStoreError,
} from "../../tsp-output/@typespec/http-server-javascript/models/all/pet-store.js";
import {
  PetUpdate,
  ResourceDeletedResponse,
  PetCreate,
  PetResourceCreatedResponse,
  PetCollectionWithNextLink,
} from "../../tsp-output/@typespec/http-server-javascript/models/all/typespec/rest/resource.js";

export class PetsImpl implements Pets<HttpContext> {
  get(ctx: HttpContext, petId: number): Promise<Pet | PetStoreError> {
    throw new Error("Method not implemented.");
  }
  update(
    ctx: HttpContext,
    petId: number,
    properties: PetUpdate
  ): Promise<Pet | PetStoreError> {
    throw new Error("Method not implemented.");
  }
  delete(
    ctx: HttpContext,
    petId: number
  ): Promise<ResourceDeletedResponse | PetStoreError> {
    throw new Error("Method not implemented.");
  }
  create(
    ctx: HttpContext,
    resource: PetCreate
  ): Promise<Pet | PetResourceCreatedResponse | PetStoreError> {
    throw new Error("Method not implemented.");
  }
  list(ctx: HttpContext): Promise<PetCollectionWithNextLink | PetStoreError> {
    throw new Error("Method not implemented.");
  }
}
