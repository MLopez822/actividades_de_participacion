from collections import Counter
from typing import Tuple

class DatosMeteorologicos():
    DIRECCIONES_VIENTO = {
       "N": 0,
       "NNE": 22.5,
       "NE": 45,
       "ENE": 67.5,
       "E": 90,
       "ESE": 112.5,
       "SE": 135,
       "SSE": 157.5,
       "S": 180,
       "SSW": 202.5,
       "SW": 225,
       "WSW": 247.5,
       "W": 270,
       "WNW": 292.5,
       "NW": 315,
       "NNW": 337.5
    }
    def __init__(self,nombre_archivo:str) -> None:
        self.nombre_archivo = nombre_archivo

    def ProcesarDatos(self)-> Tuple[float, float, float, float, str]:
        suma_temperatura = 0
        suma_humedad = 0
        suma_presion = 0
        suma_velocidad_viento = 0
        direcciones_viento = []
        count_registros = 0

        with open(self.nombre_archivo, "r") as archivo:
            for linea in archivo:
                if "Temperatura" in linea:
                    count_registros +=1
                    temperatura = float(linea.split("temperatura:")[1].strip())
                    humedad = float(linea.split("humedad:")[1].strip())
                    presion = float(linea.split("presion:")[1].strip())
                    viento = linea.split("viento:")[1].strip().split(',')
                    
                    velocidad_viento = float(viento[0])
                    direccion_viento = viento[1].strip()

                    #suma de datos
                    suma_temperatura += temperatura
                    suma_humedad += humedad
                    suma_presion += presion
                    suma_velocidad_viento += velocidad_viento
                    direcciones_viento.append(direccion_viento)
                    

        # Calcular promedios
        temperatura_promedio = suma_temperatura / count_registros if count_registros > 0 else 0
        humedad_promedio = suma_humedad / count_registros if count_registros > 0 else 0
        presion_promedio = suma_presion / count_registros if count_registros > 0 else 0
        velocidad_promedio_viento = suma_velocidad_viento / count_registros if count_registros > 0 else 0

        # Calcular dirección predominante del viento
        if direcciones_viento:
            direccion_predominante = Counter(direcciones_viento).most_common(1)[0][0]
        else:
            direccion_predominante = ""

        return(temperatura_promedio,humedad_promedio,presion_promedio,velocidad_promedio_viento,direccion_predominante)