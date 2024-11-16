import cookieParser from "cookie-parser";
import cors from "cors";
import express from "express";
import seaggerUI from "express-swagger-generator";
import morgan from "morgan";
import * as path from "path";
import appRouter from "./controllers";
import "./helpers/passportManager.js";

const packageJson = require("../../../package.json");

const { NODE_ENV = "development", APP_DOMAIN } = process.env;

const swaggerOptions = {
  swaggerDefinition: {
    info: {
      title: "Splitbill API Service",
      description: "分帳系統 api",
      version: `${packageJson.version} - ${NODE_ENV}`,
    },
    host: APP_DOMAIN,
    produces: ["application/json"],
    schemes: ["http", "https"],
    securityDefinitions: {
      JWT: {
        type: "apiKey",
        in: "header",
        name: "Authorization",
        description: "JWT token",
      },
    },
  },
  route: {
    url: "/api-docs",
    docs: "/api-docs.json",
  },
  basedir: __dirname,
  files: ["./controllers/**/*.js"],
};

const app = express();

if (NODE_ENV === "development") {
  // Log every HTTP request. See https://github.com/expressjs/morgan for other
  // available formats.
  app.use(morgan("dev"));
}

app.use(cors());
app.use(express.json());
app.use(express.urlencoded({ extended: false }));
app.use(cookieParser());

app.use("/assets", express.static(path.join(__dirname, "assets")));

app.use("/", appRouter);

seaggerUI(app)(swaggerOptions);

const port = process.env.PORT || 3333;
const server = app.listen(port, () => {
  console.log(`Listening at http://127.0.0.1:${port}/api`);
});
server.on("error", console.error);

module.exports = server;
