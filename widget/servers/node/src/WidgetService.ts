import { HttpContext } from "../tsp-output/@typespec/http-server-javascript/helpers/router.js";
import {
  Error as WidgetServiceError,
  Widget,
  WidgetService,
} from "../tsp-output/@typespec/http-server-javascript/models/all/demo-service.js";
import {
  ResourceDeletedResponse,
  WidgetCollectionWithNextLink,
  WidgetCreate,
  WidgetResourceCreatedResponse,
  WidgetUpdate,
} from "../tsp-output/@typespec/http-server-javascript/models/all/typespec/rest/resource.js";

export class WidgetServiceImpl implements WidgetService<HttpContext> {
  #next_id = 1;
  #store = new Map<string, Widget>();

  async create(_ctx: HttpContext, resource: WidgetCreate) {
    const widget = {
      id: String(this.#next_id++),
      ...resource,
    };

    this.#store.set(widget.id, widget);

    return {
      statusCode: 201,
      body: widget,
    } as WidgetResourceCreatedResponse;
  }

  async delete(_ctx: HttpContext, id: string) {
    if (!this.#store.has(id)) {
      return {
        code: 404,
        message: `Widget with id ${id} not found`,
      } as WidgetServiceError;
    }

    this.#store.delete(id);

    // TODO: this is very weird because the ResourceDeletedResponse is empty
    // on account of having its status code property named `_`, and that is
    // the _only_ property of the response.
    return {} as ResourceDeletedResponse;
  }

  async list(_ctx: HttpContext) {
    return {
      value: Array.from(this.#store.values()),
    } as WidgetCollectionWithNextLink;
  }

  async get(_ctx: HttpContext, id: string) {
    const widget = this.#store.get(id);

    if (widget) return widget;

    return {
      code: 404,
      message: `Widget with id ${id} not found`,
    } as WidgetServiceError;
  }

  async update(_ctx: HttpContext, id: string, properties: WidgetUpdate) {
    const widget = this.#store.get(id);

    if (!widget) {
      return {
        code: 404,
        message: `Widget with id ${id} not found`,
      } as WidgetServiceError;
    }

    Object.assign(widget, properties);

    return widget;
  }
}
