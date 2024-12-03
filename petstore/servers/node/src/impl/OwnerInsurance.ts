import { HttpContext } from "../../tsp-output/@typespec/http-server-javascript/helpers/router.js";
import {
  Insurance,
  OwnerInsurance,
  PetStoreError,
} from "../../tsp-output/@typespec/http-server-javascript/models/all/pet-store.js";
import { InsuranceUpdate } from "../../tsp-output/@typespec/http-server-javascript/models/all/typespec/rest/resource.js";

export class OwnerInsuranceImpl implements OwnerInsurance<HttpContext> {
  get(ctx: HttpContext, ownerId: bigint): Promise<Insurance | PetStoreError> {
    throw new Error("Method not implemented.");
  }
  update(
    ctx: HttpContext,
    ownerId: bigint,
    properties: InsuranceUpdate
  ): Promise<Insurance | PetStoreError> {
    throw new Error("Method not implemented.");
  }
}
