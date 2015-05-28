#!/usr/bin/python

import sqlite3
from bottle import route, run, debug, template, request, static_file, error

# only needed when you run Bottle on mod_wsgi
from bottle import default_app

@route('/aguas')
def getRec():
    conn = sqlite3.connect("aguas.db")
    c = conn.cursor()
    c.execute('select rid, name, val, unit from recetas')
    res = c.fetchall()
    c.close()
    output = template('make_table', rows=res)
    return output

@route('/receta<no:int>/<cant:float>')
def scaleRec(no, cant):
    conn = sqlite3.connect("aguas.db")
    c = conn.cursor()
    c.execute('select name,val from recetas where rid = ?', (no,))
    res = c.fetchone()
    receta  = res[0]
    volorig = res[1]
    
    c.execute('select name,val,unit from ingredientes natural join cantidades where rid = ?', (no,))
    res = c.fetchall()
    output = '<h2>{}</h2><table border=1><th>Ingrediente</th><th>Cantidad</th><th>Unidad</th>'.format(receta)
    for ing in res:
        name = ing[0]
        val  = ing[1]
        unit = ing[2]
        val  = float(val) * float(cant) / float(volorig)
        output = output + '<tr><td>{}</td><td>{}</td><td>{}</td>'.format(name,val,unit)
                
    output = output + '</table>'
    
    c.execute('select proceso from proceso where rid = ?', (no,))
    res = c.fetchone()
    proceso = res[0]
    output = output + '<pre>{}</pre>'.format(proceso)
    
    
    c.close()
    
    return output

@error(403)
def mistake403(code):
    return 'There is a mistake in your url!'

@error(404)
def mistake404(code):
    return 'Sorry, this page does not exist!'


debug(True)
run(reloader=True)
