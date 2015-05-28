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

@route('/rec<no:int>/<cant:float>')
def scaleRec(no, cant):
    conn = sqlite3.connect("aguas.db")
    c = conn.cursor()
    c.execute('select val from recetas where rid = ?', (no,))
    res = c.fetchone()
    volorig = res[0]
    c.execute('select name,val,unit from ingredientes natural join cantidades where rid = ?', (no,))
    res = c.fetchall()
    c.close()
    output = '<table border=1><th>Ingrediente</th><th>Cantidad</th><th>Unidad</th>'
    for ing in res:
        name = ing[0]
        val  = ing[1]
        unit = ing[2]
        val  = float(val) * float(cant) / float(volorig)
        output = output + '<tr><td>{}</td><td>{}</td><td>{}</td>'.format(name,val,unit)
                
    output = output + '</table>'
    return output

@error(403)
def mistake403(code):
    return 'There is a mistake in your url!'

@error(404)
def mistake404(code):
    return 'Sorry, this page does not exist!'


debug(True)
run(reloader=True)
