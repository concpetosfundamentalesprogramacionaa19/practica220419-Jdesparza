"""
	archivo: demo3.py
	Ejemplo de lenguaje de Python
	autor:@reroes
"""

import sys

# Se asigna valores por teclado para cada variable
valor1 = input("Por favor ingrese el primer valor:")
valor2 = input("Por favor ingrese el segundo valor: ")

# Operaciones de suma y multiplicacion de las variables
suma = int(valor1) + int(valor2) # aquí realizo la suma de variables
multiplicacion = int(valor1) * int(valor2) # aquí realizo la multiplicacion de variables

# Se impreme los valores guardados en cada variable
print("La suma es: %d\n\tLa multiplicacion es: %d" % (suma, multiplicacion))
#print("la multiplicacion es %d" % multiplicacion)