"""
	archivo: demo2.py
	Ejemplo de lenguaje de Python
	autor:@reroes
"""

import sys

# Las variables en donde se guardaran los valores
variable = sys.argv[0]
valor1 = sys.argv[1]
valor2 = sys.argv[2]

# Operaciones de suma y multiplicacion de las variables
suma = int(valor1) + int(valor2) # aquí realizo la suma de variables
multiplicacion = int(valor1) * int(valor2) # aquí realizo la multiplicacion de variables

# Se impreme los valores guardados en cada variable
print("la suma es: %s" % suma)
print("la multiplicacion es. %s" % multiplicacion)