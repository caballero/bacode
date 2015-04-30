import sqlite3
import re
from bottle import route, run, debug, template, request, static_file, error

# only needed when you run Bottle on mod_wsgi
from bottle import default_app

@route('/newteacher', method='GET')
def new_teacher():
    if request.GET.get('save','').strip():

        name = request.GET.get('name', '').strip()
        email = request.GET.get('email', '').strip()
        affiliation = request.GET.get('affiliation', '').strip()
        phone = request.GET.get('phone', '').strip()
        interest = request.GET.get('interest', '').strip()
        
        conn = sqlite3.connect('socialjob.db')
        c = conn.cursor()
        c.execute("INSERT INTO teachers (name,email,affiliation,phone,interest) VALUES (?,?,?,?,?)", (name,email,affiliation,phone,interest))
        new_id = c.lastrowid

        conn.commit()
        c.close()

        return '<p>Un nuevo profesor ha sido agregado, su ID es %s</p>' % new_id

    else:
        return template('new_teacher.tpl')

@route('/newstudent', method='GET')
def new_student():
    if request.GET.get('save','').strip():

        name = request.GET.get('name', '').strip()
        email = request.GET.get('email', '').strip()
        affiliation = request.GET.get('affiliation', '').strip()
        phone = request.GET.get('phone', '').strip()
        interest = request.GET.get('interest', '').strip()
        skills = request.GET.get('skills', '').strip()
        
        conn = sqlite3.connect('socialjob.db')
        c = conn.cursor()
        c.execute("INSERT INTO teachers (name,email,affiliation,phone,interest,skills) VALUES (?,?,?,?,?,?)", (name,email,affiliation,phone,interest,skills))
        new_id = c.lastrowid

        conn.commit()
        c.close()

        return '<p>Un nuevo alumno ha sido agregado, su ID es %s</p>' % new_id

    else:
        return template('new_student.tpl')

@route('/newjob', method='GET')
def new_job():
    if request.GET.get('save','').strip():

        name = request.GET.get('name', '').strip()
        description = request.GET.get('description', '').strip()
        teacher = request.GET.get('teacher', '').strip()
        skills = request.GET.get('skills', '').strip()
        
        conn = sqlite3.connect('socialjob.db')
        c = conn.cursor()
        c.execute("INSERT INTO teachers (name,description,teacher,skills,status) VALUES (?,?,?,?,?)", (name,description,teacher,skills,1))
        new_id = c.lastrowid

        conn.commit()
        c.close()

        return '<p>Un nuevo alumno ha sido agregado, su ID es %s</p>' % new_id

    else:
        return template('new_student.tpl')

@route('/edit/<no:int>', method='GET')
def edit_item(no):

    if request.GET.get('save','').strip():
        edit = request.GET.get('task','').strip()
        status = request.GET.get('status','').strip()

        if status == 'open':
            status = 1
        else:
            status = 0

        conn = sqlite3.connect('todo.db')
        c = conn.cursor()
        c.execute("UPDATE todo SET task = ?, status = ? WHERE id LIKE ?", (edit,status,no))
        conn.commit()

        return '<p>The item number %s was successfully updated</p>' %no

    else:
        conn = sqlite3.connect('todo.db')
        c = conn.cursor()
        c.execute("SELECT task FROM todo WHERE id LIKE ?", (str(no)))
        cur_data = c.fetchone()

        return template('edit_task', old = cur_data, no = no)

@route('/item<item:re:[0-9]+>')
def show_item(item):

        conn = sqlite3.connect('todo.db')
        c = conn.cursor()
        c.execute("SELECT task FROM todo WHERE id LIKE ?", (item))
        result = c.fetchall()
        c.close()

        if not result:
            return 'This item number does not exist!'
        else:
            return 'Task: %s' %result[0]

@route('/help')
def help():

    static_file('help.html', root='.')

@route('/json<json:re:[0-9]+>')
def show_json(json):

    conn = sqlite3.connect('todo.db')
    c = conn.cursor()
    c.execute("SELECT task FROM todo WHERE id LIKE ?", (json))
    result = c.fetchall()
    c.close()

    if not result:
        return {'task':'This item number does not exist!'}
    else:
        return {'Task': result[0]}


@error(403)
def mistake403(code):
    return 'There is a mistake in your url!'

@error(404)
def mistake404(code):
    return 'Sorry, this page does not exist!'


debug(True)
run(reloader=True)
#remember to remove reloader=True and debug(True) when you move your application from development to a productive environment
