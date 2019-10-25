"""
	@naludena1
	Practica04
"""

import codecs
import json

archivo = codecs.open("datos.txt", "r") # Lectura del archivo
lineas = archivo.readlines()

print(len(lineas))

linea_diccionario = [json.loads(l) for l in lineas]


# Encontrar todos los que han hecho mas de 3 goles
goles = lambda x: list(x.items())[1][1] > 3 # Funcion y condicion
salida_goles = filter(goles, linea_diccionario) # Filtrar los resultados de la condicion
print(list(salida_goles)) # Salida de datos


print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")


# Encontrar los que son del país Nigeria
pais = lambda x: list(x.items())[0][1] == "Nigeria" # Funcion y condicio
salida_pais = filter(pais, linea_diccionario) # Filtrar los resultados de la condicion
print(list(salida_pais)) # Salida de datos


print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")


# El valor mínimo y máximo de la caracteristica Height
height = list(map(lambda x: list(x.items())[2][1], linea_diccionario)) 
maximoNum = max(height) # Obtener el numero maximo
minimoNum = min(height) # Obtener el numero minimo

# Salida de datos
print(list(filter(lambda x: list(x.items())[2][1] == maximoNum, linea_diccionario)))
print(list(filter(lambda x: list(x.items())[2][1] == minimoNum, linea_diccionario)))






