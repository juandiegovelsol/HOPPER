class Room {
  constructor(roomNumber, capacity, price) {
    this.roomNumber = roomNumber;
    this.capacity = capacity;
    this.price = price;
    this.reservations = [];
  }

  isAvailableForDates(startDate, endDate) {
    return this.reservations.every((res) => {
      return endDate <= res.startDate || startDate >= res.endDate;
    });
  }

  needsCleaning(today) {
    return this.reservations.some((res) => {
      const daysPassed = Math.floor(
        (today - res.startDate) / (1000 * 60 * 60 * 24)
      );
      console.log(daysPassed);
      return daysPassed > 0 && daysPassed % 2 === 0;
    });
  }
}

class Hostel {
  constructor() {
    this.rooms = [];
  }

  addRoom(capacity, price) {
    const roomNumber = this.rooms.length + 1;
    this.rooms.push(new Room(roomNumber, capacity, price));
  }

  makeReservation(numPeople, startDate, endDate) {
    const options = this.checkAvailability(numPeople, startDate, endDate);
    if (options.length === 0) return null;

    const selectedRooms = options[0].rooms;
    selectedRooms.forEach((room) => {
      room.reservations.push({ startDate, endDate });
    });

    return selectedRooms.map((room) => room.roomNumber);
  }

  deleteReservation(roomNumber, startDate, endDate) {
    const room = this.rooms.find((r) => r.roomNumber === roomNumber);
    if (room) {
      room.reservations = room.reservations.filter((res) => {
        return !(
          res.startDate.getTime() === startDate.getTime() &&
          res.endDate.getTime() === endDate.getTime()
        );
      });
    }
  }

  checkAvailability(numPeople, startDate, endDate) {
    const availableRooms = this.rooms.filter((room) =>
      room.isAvailableForDates(startDate, endDate)
    );

    const options = [];
    const combinations = this.getCombinations(availableRooms);

    combinations.forEach((combo) => {
      const totalCapacity = combo.reduce((sum, room) => sum + room.capacity, 0);
      if (totalCapacity >= numPeople) {
        const totalPrice = combo.reduce((sum, room) => sum + room.price, 0);
        options.push({ rooms: combo, totalPrice, totalCapacity });
      }
    });

    options.sort(
      (a, b) => a.totalPrice - b.totalPrice || a.totalCapacity - b.totalCapacity
    );
    return options;
  }

  getCombinations(array) {
    const result = [];
    const f = (prefix, arr) => {
      for (let i = 0; i < arr.length; i++) {
        const newPrefix = [...prefix, arr[i]];
        result.push(newPrefix);
        f(newPrefix, arr.slice(i + 1));
      }
    };
    f([], array);
    return result;
  }

  getEmptyAndFullRooms() {
    let empty = 0;
    let full = 0;
    this.rooms.forEach((room) => {
      if (room.reservations.length === 0) {
        empty++;
      } else {
        full++;
      }
    });
    return { empty, full };
  }

  getRoomsNeedingCleaning(today) {
    return this.rooms
      .filter((room) => room.needsCleaning(today))
      .map((room) => room.roomNumber);
  }
}

// Suponemos que la clase Room ya está definida e importada
// Caso 1: Debe limpiar (hay una reserva que hace 2 días)
const room1 = new Room(101, 2, 50);
room1.reservations.push({
  startDate: new Date("2025-04-20"), // hace 4 días
  endDate: new Date("2025-04-22"),
});
/* room1.reservations.push({
  startDate: new Date("2025-04-23"), // hace 1 día
  endDate: new Date("2025-04-24"),
}); */
console.log(
  "Necesita limpieza (esperado true):",
  room1.needsCleaning(new Date("2025-04-24"))
);
// daysPassed para la primera reserva = 4 → 4 % 2 === 0 → cleaning

// Caso 2: No debe limpiar (ninguna reserva cumple días pares > 0)
const room2 = new Room(102, 3, 75);
room2.reservations.push({
  startDate: new Date("2025-04-22"), // hace 2 días → cleaning,
  endDate: new Date("2025-04-23"),
});
room2.reservations.push({
  startDate: new Date("2025-04-23"), // hace 1 día
  endDate: new Date("2025-04-24"),
});
// Pero hoy es justo la misma fecha de final de la primera y la segunda reserva
// daysPassed = 2 % 2 === 0 para la primera reserva, sin embargo si queremos que NO limpie:
// cambiamos la fecha de hoy para que no caiga en par:
console.log(
  "Necesita limpieza (esperado false):",
  room2.needsCleaning(new Date("2025-04-23"))
);
// daysPassed: reserva1 → 1 día (no par), reserva2 → 0 días (no >0)
