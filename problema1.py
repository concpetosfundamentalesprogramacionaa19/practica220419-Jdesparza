""" 
	Problema 1
	Problemas de lenguaje de Python
"""

# Ingreso de valores por teclado
horas = input("Por favor ingrese la cantidad de horas de trabajo: ")
costohora = input("Por favor ingrese el costo por hora: ")

# Operaciones para calcular el sueldo y el descuento
descuentoseguro = float(horas) * float(costohora) * 0.1
sueldo = (float(horas) * float(costohora)) - descuentoseguro

#Presentacion del sueldo y descuento
print("El descuento del Seguro Social es: %.2f\nEl sueldo del trabajador es: %.2f\n" % (descuentoseguro, sueldo))

