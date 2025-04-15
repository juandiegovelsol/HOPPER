// Ejemplo de datos de menú
const menuItems = [
  { id: 1, name: "Hamburguesa", price: 8.99 },
  { id: 2, name: "Pizza", price: 12.99 },
  { id: 3, name: "Ensalada", price: 7.99 },
];

let currentOrder = []; // Pedido actual del cliente

// Función para mostrar el menú y permitir al cliente hacer su pedido
function showMenuAndTakeOrder() {
  // Verificar si el cliente está logueado
  if (!isLoggedIn()) {
    alert("Por favor, inicia sesión para hacer un pedido.");
    return;
  }

  // Mostrar el menú al cliente
  console.log("Menú:");
  menuItems.forEach((item) => {
    console.log(`${item.id}. ${item.name} - $${item.price.toFixed(2)}`);
  });

  // Simular la selección de elementos del menú
  addItemToOrder(2, "Extra queso, sin cebolla");
  addItemToOrder(1, "");

  // Calcular y mostrar el precio total del pedido
  updateTotalPrice();
}

// Función para agregar un ítem al pedido
function addItemToOrder(itemId, comment = "") {
  const menuItem = menuItems.find((item) => item.id === itemId);
  if (menuItem) {
    currentOrder.push({ ...menuItem, comment });
    console.log(`Añadido al pedido: ${menuItem.name}`);
  } else {
    console.log("Ítem no encontrado.");
  }
}

// Función para calcular el precio total
function updateTotalPrice() {
  const totalPrice = currentOrder.reduce(
    (total, item) => total + item.price,
    0
  );
  console.log(`Precio total: $${totalPrice.toFixed(2)}`);
}

// Simulación de verificación de sesión iniciada
function isLoggedIn() {
  // Aquí deberías implementar la lógica real para verificar la sesión del usuario
  return true;
}

// Ejecución de la función para ver el menú y hacer pedidos
showMenuAndTakeOrder();
