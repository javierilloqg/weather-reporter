#******************************************************************************
#* Copyright (C) 2020 by Javier Quesada Galban
#*
#* Python script to show weather forecast for desired cities
#*
#******************************************************************************
#
#* @file tarea_final.py
#* @author Javier Quesada Galban
#* @date 13 April 2021
#* @brief This script gets data from openweathermap via API and returns the 
#  weather for desired city.  
#*
#

import swowpy
from modulo_presion import comprobarpresion
from modulo_direccion_viento import direccion

api_key = "" #Personal API key here

ciudades = input("Introduce diez ciudades, separadas por coma: ")
tabla_ciudades = ciudades.split(",")
print("Has introducido:", len(tabla_ciudades), "ciudades")
kelvin = -273 #This workaround fixes snowpy bug


if len(tabla_ciudades) > 10: #max 10 cities. Could be more
    print("No soporto más de 10 ciudades!!! (aún)")
else:
    for ciudad in tabla_ciudades:
        tiempo = swowpy.Swowpy(api_key, ciudad)
        temperatura = int(tiempo.temperature()) + kelvin
        humedad = tiempo.humidity()
        presion = tiempo.pressure()
        viento = tiempo.wind()
        print("\n") #no se si lo quitaré en la revisión final
        print("Ciudad: ", ciudad)
        print("Descripción:", tiempo.current_weather("Description"))
        print("Temperatura:", temperatura,"°C")
        print("Humedad relativa:", humedad,"%")
        print("Presión atmosférica:", presion,"hPa")
        print("Velocidad del viento:", viento[0],"m/s",",", viento[1],"°", \
        direccion(viento[1])) #velocidad, m/s, dirección, grados
        print(comprobarpresion(presion))
        print("---------------------------------")
        print("\n")

print("Script realizado por Javier Quesada Galbán")
        
    