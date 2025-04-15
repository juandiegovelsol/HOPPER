import math
import select
import time
import random
import sys

# Variables globales
presion_acumulada = 0
muestras = 0
max_historico = 0
eventos = []
pausado = False
config = None
tendencia = []
inicio_coccion = time.time()
valvula_activa = False
receta_actual = None
tiempo_inicio_receta = None

def cargar_configuracion():
    return {
        "max_seguro": 85,
        "critico": 95,
        "intervalo_muestreo": 0.2,
        "umbral_pico": 15,
        "longitud_tendencia": 30,
        "tiempo_descarga": 2,
        "rango_estabilidad": 5
    }

def controlar_valvula(presion_actual):
    global valvula_activa
    if presion_actual >= config['critico'] and not valvula_activa:
        valvula_activa = True
        time.sleep(config['tiempo_descarga'])
        return presion_actual * 0.6
    valvula_activa = False
    return presion_actual

def actualizar_estadisticas(presion):
    global presion_acumulada, muestras, max_historico
    presion_acumulada += presion
    muestras += 1
    if presion > max_historico:
        max_historico = presion

def detectar_pico(presion_actual, presion_anterior):
    if presion_actual - presion_anterior > config['umbral_pico']:
        return f"¡AUMENTO BRUSCO! Δ{presion_actual - presion_anterior}%"
    return ""

def mostrar_alarma(mensaje):
    print(f"\n*** ALARMA: {mensaje} ***")

def guardar_log(presion, estado):
    with open("presion.log", "a") as f:
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
        f.write(f"{timestamp} - {presion}% - {estado}\n")

def configurar_umbrales_interactivo():
    nuevo_max = int(input("Nuevo máximo seguro (%): "))
    nuevo_critico = int(input("Nuevo nivel crítico (%): "))
    if nuevo_max >= nuevo_critico:
        raise ValueError("El máximo seguro debe ser menor al crítico")
    config.update({
        "max_seguro": nuevo_max,
        "critico": nuevo_critico
    })

config = cargar_configuracion()


