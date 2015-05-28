#!/usr/bin/python

import sqlite3
from bottle import route, run, debug, template, request, static_file, error

# only needed when you run Bottle on mod_wsgi
from bottle import default_app

@route('/aguas')
def getRec:
    conn = sqlite3.connect("aguas.db")
    c = conn.cursor()
    c.execute('select name, val, unit from recetas')
    res = c.fetchall()
    c.close()
    output = template('make_table', rows=result)
    return output
    
@error(403)
def mistake403(code):
    return 'There is a mistake in your url!'

@error(404)
def mistake404(code):
    return 'Sorry, this page does not exist!'


debug(True)
run(reloader=True)
