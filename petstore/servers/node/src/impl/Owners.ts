import { HttpContext } from "../../tsp-output/@typespec/http-server-javascript/helpers/router.js";
import {
  Owner,
  Owners,
  PetStoreError,
} from "../../tsp-output/@typespec/http-server-javascript/models/all/pet-store.js";
import {
  OwnerUpdate,
  ResourceDeletedResponse,
  OwnerCreate,
  OwnerResourceCreatedResponse,
  OwnerCollectionWithNextLink,
} from "../../tsp-output/@typespec/http-server-javascript/models/all/typespec/rest/resource.js";

export class OwnersImpl implements Owners<HttpContext> {
  get(ctx: HttpContext, ownerId: bigint): Promise<Owner | PetStoreError> {
    throw new Error("Method not implemented.");
  }
  update(
    ctx: HttpContext,
    ownerId: bigint,
    properties: OwnerUpdate
  ): Promise<Owner | PetStoreError> {
    throw new Error("Method not implemented.");
  }
  delete(
    ctx: HttpContext,
    ownerId: bigint
  ): Promise<ResourceDeletedResponse | PetStoreError> {
    throw new Error("Method not implemented.");
  }
  create(
    ctx: HttpContext,
    resource: OwnerCreate
  ): Promise<Owner | OwnerResourceCreatedResponse | PetStoreError> {
    throw new Error("Method not implemented.");
  }
  list(ctx: HttpContext): Promise<OwnerCollectionWithNextLink | PetStoreError> {
    throw new Error("Method not implemented.");
  }
}
