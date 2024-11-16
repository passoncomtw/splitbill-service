import Express from "express";
import { lineLoginRoute } from "./authRouter";

const router = Express.Router();

router.post("/auth/line", lineLoginRoute);

export default router;
