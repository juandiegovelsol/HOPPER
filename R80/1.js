class Order {
  constructor(type, isPaid, isVIP) {
    this.type = type; // "onSite" o "pickUp"
    this.isPaid = isPaid;
    this.isVIP = isVIP;
  }
}

class OrderManager {
  constructor() {
    this.ordersQueue = []; // Cola de pedidos
    this.basePreparationTime = 10; // Tiempo base de preparación en minutos
  }

  addOrder(order) {
    this.ordersQueue.push(order);
  }

  calculateWaitTime(order) {
    // Ordenamos la cola de pedidos en base a prioridad
    this.ordersQueue.sort((a, b) => {
      if (a.type === b.type) {
        return b.isVIP - a.isVIP; // Clientes VIP primero
      }
      return a.type === "onSite" ? -1 : 1; // "onSite" tiene prioridad sobre "pickUp"
    });
    //console.log(this.ordersQueue);
    let currentTime = new Date();
    let waitTimeMinutes = 0;

    for (const o of this.ordersQueue) {
      // Si encontramos el pedido en la cola, calculamos el tiempo hasta ese punto
      if (o === order) {
        break;
      }
      waitTimeMinutes += this.basePreparationTime; // Incrementamos el tiempo de espera
    }

    // Calculamos la hora estimada de entrega
    currentTime.setMinutes(currentTime.getMinutes() + waitTimeMinutes);

    const day = String(currentTime.getDate()).padStart(2, "0");
    const month = String(currentTime.getMonth() + 1).padStart(2, "0");
    const year = currentTime.getFullYear();
    const hours = String(currentTime.getHours()).padStart(2, "0");
    const minutes = String(currentTime.getMinutes()).padStart(2, "0");

    return `${day}-${month}-${year}-${hours}-${minutes}`;
  }
}

// Ejemplo de uso:
const manager = new OrderManager();

const order1 = new Order("onSite", false, false);
const order2 = new Order("pickUp", false, true);
const order3 = new Order("onSite", false, true);

manager.addOrder(order1);
manager.addOrder(order2);
manager.addOrder(order3);

console.log(manager.calculateWaitTime(order1));
console.log(manager.calculateWaitTime(order2));
console.log(manager.calculateWaitTime(order3));
