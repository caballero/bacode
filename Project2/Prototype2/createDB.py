import sqlite3
con = sqlite3.connect('socialjob.db') # Warning: This file is created in the current directory
con.execute("CREATE TABLE teachers (id INTEGER PRIMARY KEY,   \
                                    name CHAR(100) NOT NULL,  \
                                    email CHAR(100) NOT NULL, \
                                    affiliation CHAR(100),    \
                                    phone CHAR(20),           \
                                    interest TEXT)")
con.execute("CREATE TABLE students (id INTEGER PRIMARY KEY,   \
                                    name CHAR(100) NOT NULL,  \
                                    email CHAR(100) NOT NULL, \
                                    affiliation CHAR(100),    \
                                    phone CHAR(20),           \
                                    interest TEXT,            \
                                    skills TEXT)")

con.execute("CREATE TABLE jobs     (id INTEGER PRIMARY KEY,    \
                                    name CHAR(100) NOT NULL,   \
                                    description TEXT NOT NULL, \
                                    teacher INT,               \
                                    skills TEXT,               \
                                    status BOOLEAN)")
                                    
con.commit()
