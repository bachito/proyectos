#!/usr/bin/python
# -*- coding: utf_8 -*-
# mundial.py: ejemplo de uso de estructuras de datos

def mostrar_tabla(tabla):
	'''Muestra una tabla de posiciones.

	@param tabla: diccionario donde la clave es el cuadro y el valor
	son los puntos
	'''

	print "\nTabla de posiciones"
	for c, p in tabla.iteritems():
		print c + ': ' + str(p)
	print
#funcion que recibe los resultados y llama a actualizar o no la tabla de posiciones
def ingresar_resultado(tabla1):
	cuadro_a = raw_input("Ingrese el primer cuadro de la fecha")
	goles_a = raw_input("Ahora ingrese cuántos goles hizo")
	cuadro_b = raw_input("Ingrese el segundo cuadro de la fecha")
	goles_b = raw_input("Ahora ingrese cuántos goles hizo")
	condicion = raw_input("Desea actualizar la tabla de posiciones? Y/N")
	if condicion == "Y" or condicion == "y":
		actualizar_tabla(tabla1,cuadro_a,goles_a,cuadro_b,goles_b)

#funcion que actualiza la tabla de posiciones
def actualizar_tabla(tabla,cuadro1,goles1,cuadro2,goles2):
	if goles1 > goles2:
		tabla[cuadro1] += 3
	elif goles2 > goles1:
		tabla[cuadro2] += 3
	else:
		tabla[cuadro1] += 1
		tabla[cuadro2] += 1

# inicializar la tabla de posiciones
cuadros = ['Uruguay', 'Mexico', 'Francia', 'Sudafrica']
tabla = dict([(c, 0) for c in cuadros])
mostrar_tabla(tabla)

# primera fecha
print "Se juega la primera fecha"
fecha1 = [{'Uruguay': 2, 'Francia': 1},
	{'Mexico': 1, 'Sudafrica': 1}]
for partido in fecha1:
	c = partido.keys()
	print c[0] + " vs. " + c[1] + ": ",
	if partido[c[0]] > partido[c[1]]:
		print "ganó " + c[0]
		tabla[c[0]] = tabla[c[0]] + 3
	elif partido[c[0]] < partido[c[1]]:
		print "ganó " + c[1]
		tabla[c[1]] = tabla[c[1]] + 3
	else:
		print "empate"
		tabla[c[0]] = tabla[c[0]] + 1
		tabla[c[1]] = tabla[c[1]] + 1
print "Fin de la primera fecha"
mostrar_tabla(tabla)
