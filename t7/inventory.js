const express = require("express");
const inventoryController = require("./inventoryController");

const router = express.Router();

router.post("/", inventoryController.createToy);
router.put("/:id", inventoryController.updateToyQuantity);
router.post("/orders", inventoryController.createOrder);

module.exports = router;
