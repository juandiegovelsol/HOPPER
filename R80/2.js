class Order {
  constructor(type, paid, vip) {
    this.type = type; // "onSite" o "pickUp"
    this.paid = paid; // true o false
    this.vip = vip; // true o false
  }
}

class Restaurant {
  constructor() {
    this.orders = []; // Cola de pedidos pendientes
    this.preparationTime = 20; // Tiempo de preparación de cada pedido (en minutos)
  }

  // Función para agregar un nuevo pedido a la cola
  addOrder(order) {
    this.orders.push(order);
  }

  // Función para calcular el tiempo de espera restante para cada pedido
  calculateWaitTime(order) {
    const priorityOrders = this.orders.filter(
      (o) => o.vip || o.type === "onSite"
    );
    const regularOrders = this.orders.filter(
      (o) => !o.vip && o.type === "pickUp"
    );

    let waitTime = 0;

    // Calcular tiempo de espera para órdenes de mayor prioridad (onSite y VIP)
    for (const ord of priorityOrders) {
      waitTime += this.preparationTime;
      if (ord.type === "pickUp" && !ord.paid) {
        waitTime += 5; // Tiempo adicional por pago en pickUp
      }
    }

    // Calcular tiempo de espera para órdenes regulares (pickUp)
    if (order.type === "pickUp" && !order.paid) {
      waitTime += 5; // Tiempo adicional por pago en pickUp
    }

    return waitTime;
  }

  // Función para obtener la hora estimada de entrega de un pedido
  getDeliveryTime(order) {
    const now = new Date();
    const minutesToAdd = this.calculateWaitTime(order);
    now.setMinutes(now.getMinutes() + minutesToAdd);

    // Formatear la fecha y hora de entrega estimada
    const deliveryTime = `${now.getDate()}-${(now.getMonth() + 1)
      .toString()
      .padStart(2, "0")}-${now.getFullYear()}-${now
      .getHours()
      .toString()
      .padStart(2, "0")}-${now.getMinutes().toString().padStart(2, "0")}`;

    return deliveryTime;
  }
}

// Ejemplo de uso:
const santaBrasa = new Restaurant();

const newOrder1 = new Order("onSite", true, false);
const newOrder2 = new Order("pickUp", false, false);
const newOrder3 = new Order("pickUp", true, true);

// Agregar algunos pedidos de prueba
santaBrasa.addOrder(newOrder1);
santaBrasa.addOrder(newOrder2);
santaBrasa.addOrder(newOrder3);

console.log(
  santaBrasa.getDeliveryTime(newOrder1),
  ", ",
  santaBrasa.getDeliveryTime(newOrder2),
  ", ",
  santaBrasa.getDeliveryTime(newOrder3)
);

// Crear un nuevo pedido para obtener su hora de entrega estimada
const newOrder = new Order("pickUp", true, false);
const deliveryTime = santaBrasa.getDeliveryTime(newOrder);

console.log("Hora estimada de entrega:", deliveryTime);
