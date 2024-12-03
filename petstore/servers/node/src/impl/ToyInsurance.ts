import { HttpContext } from "../../tsp-output/@typespec/http-server-javascript/helpers/router.js";
import {
  Insurance,
  PetStoreError,
  ToyInsurance,
} from "../../tsp-output/@typespec/http-server-javascript/models/all/pet-store.js";
import { InsuranceUpdate } from "../../tsp-output/@typespec/http-server-javascript/models/all/typespec/rest/resource.js";

export class ToyInsuranceImpl implements ToyInsurance<HttpContext> {
  get(
    ctx: HttpContext,
    petId: number,
    toyId: bigint
  ): Promise<Insurance | PetStoreError> {
    throw new Error("Method not implemented.");
  }
  update(
    ctx: HttpContext,
    petId: number,
    toyId: bigint,
    properties: InsuranceUpdate
  ): Promise<Insurance | PetStoreError> {
    throw new Error("Method not implemented.");
  }
}
