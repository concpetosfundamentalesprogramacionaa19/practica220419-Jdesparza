""" 
	Problema 1
	Problemas de lenguaje de Python
"""
# Ingreso de valores por teclado
x = input("Por favor ingrese el valor de x: ")
y = input("Por favor ingrese el valor de y: ")
z = input("Por favor ingrese el valor de z: ")

# Operacion para calcular m
m = (float(x) + (float(y) / float(z))) / (float(x) - (float(y) / float(z)))

# Respuesta de m
print("el valor de m, en base a las variables : \nx = %.1f\n\ty = %.1f\n\t\tz = %.1f\nDa como resultado: \n\t m = %.2f" % (float(x), float(y), float(z), m))