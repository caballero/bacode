import sqlite3

conn = sqlite3.connect("aguas.db")
c = conn.cursor()

c.execute('''create table recetas(rid int, name text, val real, unit text)''')
c.execute('''create table ingredientes(iid int, name text)''')
c.execute('''create table cantidades(rid int, iid int, val real, unit text)''')
c.execute('''create table proceso(rid int, proceso text)''')

"""
c.execute('''mode tabs''')

c.execute('''import recetas recetas''')
c.execute('''import ingredientes ingrediente''')
c.execute('''import cantidades cantidades''')
c.execute('''import proceso proceso''')
"""

conn.commit()

c.close()