from datetime import datetime, timedelta
from typing import Set, List, Tuple

class Hotel:
    def __init__(self, nombre: str, habitaciones: List[int]):
        """
        Inicializa un hotel con un nombre y una lista de números de habitaciones.
        
        :param nombre: Nombre del hotel.
        :param habitaciones: Lista de números de habitaciones disponibles.
        """
        self.nombre = nombre
        self.habitaciones = {num: set() for num in habitaciones}

    def _generar_rango_fechas(self, fecha_inicio: datetime, fecha_fin: datetime) -> Set[str]:
        """
        Genera un conjunto de fechas entre fecha_inicio y fecha_fin, inclusivas.
        
        :param fecha_inicio: Fecha de inicio del rango.
        :param fecha_fin: Fecha de fin del rango.
        :return: Conjunto de fechas en formato string "dd/mm/yyyy".
        """
        fecha_actual = fecha_inicio
        fechas = set()
        while fecha_actual <= fecha_fin:
            fechas.add(fecha_actual.strftime("%d/%m/%Y"))
            fecha_actual += timedelta(days=1)
        return fechas

    def reservar_habitacion(self, numero_habitacion: int, fecha_inicio: datetime, fecha_fin: datetime) -> None:
        """
        Reserva una habitación por un rango de fechas.
        
        :param numero_habitacion: Número de la habitación a reservar.
        :param fecha_inicio: Fecha de inicio de la reserva.
        :param fecha_fin: Fecha de fin de la reserva.
        """
        if numero_habitacion in self.habitaciones:
            fechas_reserva = self._generar_rango_fechas(fecha_inicio, fecha_fin)
            if not self.habitaciones[numero_habitacion].intersection(fechas_reserva):
                self.habitaciones[numero_habitacion].update(fechas_reserva)
                print(f"Habitación {numero_habitacion} reservada del {fecha_inicio.strftime('%d/%m/%Y')} al {fecha_fin.strftime('%d/%m/%Y')} en {self.nombre}.")
            else:
                print(f"Habitación {numero_habitacion} no disponible en {self.nombre} para el rango {fecha_inicio.strftime('%d/%m/%Y')} - {fecha_fin.strftime('%d/%m/%Y')}.")
        else:
            print(f"Habitación {numero_habitacion} no existe en {self.nombre}.")

    def cancelar_reserva(self, numero_habitacion: int, fecha_inicio: datetime, fecha_fin: datetime) -> None:
        """
        Cancela una reserva en una habitación por un rango de fechas.
        
        :param numero_habitacion: Número de la habitación de la reserva a cancelar.
        :param fecha_inicio: Fecha de inicio del rango a cancelar.
        :param fecha_fin: Fecha de fin del rango a cancelar.
        """
        if numero_habitacion in self.habitaciones:
            fechas_reserva = self._generar_rango_fechas(fecha_inicio, fecha_fin)
            if fechas_reserva.issubset(self.habitaciones[numero_habitacion]):
                self.habitaciones[numero_habitacion].difference_update(fechas_reserva)
                print(f"Reserva de la habitación {numero_habitacion} cancelada del {fecha_inicio.strftime('%d/%m/%Y')} al {fecha_fin.strftime('%d/%m/%Y')} en {self.nombre}.")
            else:
                print(f"No se puede cancelar la reserva. No todas las fechas del rango {fecha_inicio.strftime('%d/%m/%Y')} - {fecha_fin.strftime('%d/%m/%Y')} están reservadas.")
        else:
            print(f"Habitación {numero_habitacion} no existe en {self.nombre}.")

    def habitaciones_disponibles(self, fecha_inicio: datetime, fecha_fin: datetime) -> List[int]:
        """
        Devuelve una lista de números de habitaciones disponibles en un rango de fechas.
        
        :param fecha_inicio: Fecha de inicio del rango de consulta.
        :param fecha_fin: Fecha de fin del rango de consulta.
        :return: Lista de números de habitaciones disponibles.
        """
        fechas_consulta = self._generar_rango_fechas(fecha_inicio, fecha_fin)
        disponibles = [num for num, reservas in self.habitaciones.items() if not reservas.intersection(fechas_consulta)]
        print(f"Habitaciones disponibles en {self.nombre} del {fecha_inicio.strftime('%d/%m/%Y')} al {fecha_fin.strftime('%d/%m/%Y')}: {disponibles}")
        return disponibles

# Ejemplo de uso:

# 1. Crear una instancia del hotel con algunas habitaciones
hotel = Hotel("Hotel California", [101, 102, 103])

# 2. Realizar una reserva en la habitación 101 del 1 al 5 de septiembre de 2023
fecha_inicio_reserva = datetime(2023, 9, 1)
fecha_fin_reserva = datetime(2023, 9, 5)
hotel.reservar_habitacion(101, fecha_inicio_reserva, fecha_fin_reserva)
# Se espera que se muestre:
# "Habitación 101 reservada del 01/09/2023 al 05/09/2023 en Hotel California."

# 3. Intentar reservar la misma habitación 101 en fechas que se solapan (3 al 6 de septiembre de 2023)
fecha_inicio_solapada = datetime(2023, 9, 3)
fecha_fin_solapada = datetime(2023, 9, 6)
hotel.reservar_habitacion(101, fecha_inicio_solapada, fecha_fin_solapada)
# Se espera que se muestre un mensaje indicando que la habitación no está disponible.

# 4. Reservar la habitación 102 para otra fecha (del 2 al 4 de septiembre de 2023)
hotel.reservar_habitacion(102, datetime(2023, 9, 2), datetime(2023, 9, 4))

# 5. Consultar las habitaciones disponibles en el hotel para el rango del 3 al 4 de septiembre de 2023
hotel.habitaciones_disponibles(datetime(2023, 9, 3), datetime(2023, 9, 4))
# Se espera que la lista incluya las habitaciones que no tienen reservas en esas fechas (por ejemplo, la 103)

# 6. Cancelar la reserva realizada en la habitación 101 del 1 al 5 de septiembre de 2023
hotel.cancelar_reserva(101, fecha_inicio_reserva, fecha_fin_reserva)
# Se espera que se muestre:
# "Reserva de la habitación 101 cancelada del 01/09/2023 al 05/09/2023 en Hotel California."

# 7. Volver a consultar las habitaciones disponibles para el mismo rango (3 al 4 de septiembre de 2023)
hotel.habitaciones_disponibles(datetime(2023, 9, 3), datetime(2023, 9, 4))
# Ahora la habitación 101 debería estar disponible.