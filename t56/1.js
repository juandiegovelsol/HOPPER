const fs = require("fs");

function loadOrders(file) {
  const data = fs.readFileSync(file);
  return JSON.parse(data);
}

function validateOrder(order) {
  return (
    order &&
    typeof order.total === "number" &&
    order.total > 0 &&
    Array.isArray(order.dishes) &&
    order.dishes.every(
      (dish) =>
        typeof dish.name === "string" &&
        dish.name.trim() !== "" &&
        typeof dish.quantity === "number" &&
        dish.quantity > 0
    )
  );
}

function analyzeSales(orders) {
  const salesCategories = {
    low: {},
    medium: {},
    high: {},
  };

  for (const key in orders) {
    const order = orders[key];
    if (validateOrder(order)) {
      const { total, dishes } = order;
      let category = "";
      if (total <= 50) category = "low";
      else if (total <= 100) category = "medium";
      else category = "high";

      for (const dish of dishes) {
        salesCategories[category][dish.name] =
          (salesCategories[category][dish.name] || 0) + dish.quantity;
      }
    }
  }

  for (const category in salesCategories) {
    const mostOrderedDish = Object.entries(salesCategories[category]).reduce(
      (a, b) => (b[1] > a[1] ? b : a),
      ["", 0]
    );
    console.log(
      `Plato más pedido en ${category}: ${mostOrderedDish[0]} (Cantidad: ${mostOrderedDish[1]})`
    );
  }
}

const orders = loadOrders("orders.json");
analyzeSales(orders);
