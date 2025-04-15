from datetime import datetime, timedelta
from typing import Set, Dict, List, Tuple

class Hotel:
    def __init__(self, nombre: str, habitaciones: List[int]):
        """Inicializa el hotel con un nombre y una lista de números de habitaciones."""
        self.nombre: str = nombre
        self.habitaciones: Dict[int, Set[str]] = {num: set() for num in habitaciones}

    def _formatear_fecha(self, fecha: datetime) -> str:
        """Formatea una fecha en formato 'dd/mm/aaaa'."""
        return fecha.strftime("%d/%m/%Y")

    def _generar_rango_fechas(self, fecha_inicio: datetime, fecha_fin: datetime) -> Set[str]:
        """Genera un conjunto de fechas entre `fecha_inicio` y `fecha_fin` inclusive."""
        fecha_actual: datetime = fecha_inicio
        fechas: Set[str] = set()
        while fecha_actual <= fecha_fin:
            fechas.add(self._formatear_fecha(fecha_actual))
            fecha_actual += timedelta(days=1)
        return fechas

    def reservar_habitacion(self, numero_habitacion: int, fecha_inicio: datetime, fecha_fin: datetime) -> None:
        """Reserva una habitación en el rango de fechas indicado."""
        if numero_habitacion in self.habitaciones:
            fechas_reserva: Set[str] = self._generar_rango_fechas(fecha_inicio, fecha_fin)
            if not self.habitaciones[numero_habitacion].intersection(fechas_reserva):
                self.habitaciones[numero_habitacion].update(fechas_reserva)
                print(
                    f"Habitación {numero_habitacion} reservada del 
                    {self._formatear_fecha(fecha_inicio)} al 
                    {self._formatear_fecha(fecha_fin)} en {self.nombre}."
                )
            else:
                print(
                    f"Habitación {numero_habitacion} no disponible en {self.nombre} 
                    para el rango {self._formatear_fecha(fecha_inicio)} - 
                    {self._formatear_fecha(fecha_fin)}."
                )
        else:
            print(f"Habitación {numero_habitacion} no existe en {self.nombre}.")

    def cancelar_reserva(self, numero_habitacion: int, fecha_inicio: datetime, fecha_fin: datetime) -> None:
        """Cancela una reserva en el rango de fechas indicado."""
        if numero_habitacion in self.habitaciones:
            fechas_reserva: Set[str] = self._generar_rango_fechas(fecha_inicio, fecha_fin)
            if fechas_reserva.issubset(self.habitaciones[numero_habitacion]):
                self.habitaciones[numero_habitacion].difference_update(fechas_reserva)
                print(
                    f"Reserva de la habitación {numero_habitacion} cancelada del 
                    {self._formatear_fecha(fecha_inicio)} al 
                    {self._formatear_fecha(fecha_fin)} en {self.nombre}."
                )
            else:
                print(
                    f"No se puede cancelar la reserva. No todas las fechas del rango 
                    {self._formatear_fecha(fecha_inicio)} - 
                    {self._formatear_fecha(fecha_fin)} están reservadas."
                )
        else:
            print(f"Habitación {numero_habitacion} no existe en {self.nombre}.")

    def habitaciones_disponibles(self, fecha_inicio: datetime, fecha_fin: datetime) -> List[int]:
        """Devuelve una lista de números de habitaciones disponibles en el rango de fechas indicado."""
        fechas_consulta: Set[str] = self._generar_rango_fechas(fecha_inicio, fecha_fin)
        disponibles: List[int] = [
            num for num, reservas in self.habitaciones.items() if not reservas.intersection(fechas_consulta)
        ]
        print(
            f"Habitaciones disponibles en {self.nombre} del 
            {self._formatear_fecha(fecha_inicio)} al 
            {self._formatear_fecha(fecha_fin)}: {disponibles}"
        )
        return disponibles

def pruebas_hotel() -> None:
    """Función para realizar pruebas de funcionalidad del sistema de reservas del hotel."""
    # Crea un hotel con 3 habitaciones
    hotel = Hotel("Gran Hotel", [101, 102, 103])

    # Crea fechas para las pruebas
    fecha_inicio = datetime(2023, 10, 1)
    fecha_fin = datetime(2023, 10, 5)

    # Intenta reservar habitaciones
    hotel.reservar_habitacion(101, fecha_inicio, fecha_fin)
    hotel.reservar_habitacion(102, fecha_inicio, fecha_fin)
    hotel.reservar_habitacion(103, fecha_inicio, fecha_fin)

    # Intenta reservar una habitación ya reservada
    hotel.reservar_habitacion(101, fecha_inicio, fecha_fin)

    # Verifica disponibilidad de habitaciones en un nuevo rango de fechas
    hotel.habitaciones_disponibles(fecha_inicio, fecha_fin)

    # Cancela reservas para una habitación
    hotel.cancelar_reserva(101, fecha_inicio, fecha_fin)
    hotel.cancelar_reserva(101, fecha_inicio, fecha_fin)

    # Verifica disponibilidad de habitaciones después de la cancelación
    hotel.habitaciones_disponibles(fecha_inicio, fecha_fin)

# Llamada a la función de pruebas
pruebas_hotel()