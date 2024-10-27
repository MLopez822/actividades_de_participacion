from modelo.init import DatosMeteorologicos

dt = DatosMeteorologicos("resources/datos.txt")
estadisticas = dt.ProcesarDatos()

print("Temperatura promedio:", estadisticas[0])
print("Humedad promedio:", estadisticas[1])
print("Presión promedio:", estadisticas[2])
print("Velocidad promedio del viento:", estadisticas[3])
print("Dirección predominante del viento:", estadisticas[4])