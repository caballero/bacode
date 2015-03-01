#!/usr/bin/python

import sys

rec = sys.argv[1]
cant = sys.argv[2]

recetas = { }
volumen = { }
ingredientes = { }
proceso = { }
cantidades = { }
unidades = { }

rh = open("recetas", "r")
ih = open("ingredientes", "r")
ph = open("proceso", "r")
ch = open("cantidades", "r")

for line in rh:
	line = line.replace("\n", "")
	(id, nombre, cantidad, unidad) = line.split("\t")
	recetas[id] = nombre
	volumen[id] = cantidad

for line in ih:
	line = line.replace("\n", "")
	(id, nombre) = line.split("\t")
	ingredientes[id] = nombre

for line in ph:
	line = line.replace("\n", "")
	(id, nombre) = line.split("\t")
	proceso[id] = nombre

for line in ch:
	line = line.replace("\n", "")
	(rid, iid, cantidad, unidad) = line.split("\t")
	cantidades[rid + ':' + iid] = cantidad
	unidades[rid + ':' + iid] = unidad
	
escala = float(cant) / float(volumen[rec]) # L

print "RECETA SELECCIONADA:"
print recetas[rec] + " (" + volumen[rec] + "L)" 
print
print "INGREDIENTES PARA {} L".format(cant)
for key in cantidades.keys():
	(rid, iid) = key.split(":")
	if rid != rec:
		continue
	nombre = ingredientes[iid]
	cantidad = cantidades[key]
	unidad = unidades[key]
	cantidad_ajustada = float(cantidad) * float(escala)
	print "{} {} {}".format(cantidad_ajustada, unidad, nombre)

print
print "PREPARACION:"
print proceso[rec]