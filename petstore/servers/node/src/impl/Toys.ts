import { HttpContext } from "../../tsp-output/@typespec/http-server-javascript/helpers/router.js";
import {
  PetStoreError,
  Toy,
  Toys,
} from "../../tsp-output/@typespec/http-server-javascript/models/all/pet-store.js";
import { ToyCollectionWithNextLink } from "../../tsp-output/@typespec/http-server-javascript/models/all/typespec/rest/resource.js";

export class ToysImpl implements Toys<HttpContext> {
  get(
    ctx: HttpContext,
    petId: number,
    toyId: bigint
  ): Promise<Toy | PetStoreError> {
    throw new Error("Method not implemented.");
  }
  list(
    ctx: HttpContext,
    petId: number,
    nameFilter: string
  ): Promise<ToyCollectionWithNextLink | PetStoreError> {
    throw new Error("Method not implemented.");
  }
}
