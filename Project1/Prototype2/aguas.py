#!/usr/bin/python

import sys
import sqlite3

rec = sys.argv[1]
cant = sys.argv[2]

conn = sqlite3.connect("aguas.db")
c = conn.cursor()

c.execute('select name, val, unit from recetas where rid == ?', rec)
res = c.fetchone()
receta = res[0]
cantorig = res[1]
unitorig = res[2]

escala = float(cant) / float(cantorig)

print "RECETA SELECCIONADA:"
print "{} ({} {})".format(receta, cantorig, unitorig) 
print

print "INGREDIENTES PARA {} {}".format(cant, unitorig)
c.execute('select i.name, c.val, c.unit from cantidades as c natural join ingredientes as i where rid == ?', rec)
res = c.fetchall()
for row in res:
	nombre = row[0]
	cantidad = row[1]
	unidad = row[2]
	cantidad_ajustada = float(cantidad) * float(escala)
	print "{} {} {}".format(cantidad_ajustada, unidad, nombre)

print
print "PREPARACION:"
c.execute('select proceso from proceso where rid == ?', rec)
res = c.fetchone()
proceso = res[0]
print proceso

c.close()