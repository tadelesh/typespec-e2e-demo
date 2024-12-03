import express from "express";

import morgan from "morgan";

const app = express();
app.use(morgan("dev"));

import { createDemoServiceRouter } from "../tsp-output/@typespec/http-server-javascript/http/router.js";
import { WidgetServiceImpl } from "./WidgetService.js";

const router = createDemoServiceRouter(new WidgetServiceImpl());

app.use(router.expressMiddleware);

const port = process.env["PORT"] ?? 8080;

app.listen(port, () => {
  console.log(`Demo Service: Listening on port ${port}`);
});
