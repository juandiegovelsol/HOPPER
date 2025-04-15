const express = require("express");
const userController = require("./userController");

const router = express.Router();

router.post("/", userController.createUser);
router.get("/:id", userController.getUserById);
router.get("/", userController.getAllUsers);

module.exports = router;
