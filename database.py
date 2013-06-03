import sqlite3
con =sqlite3.connect('todo.db')
con.execute("CREATE TABLE todo (id INTEGER PRIMARY KEY,task char(100) NOT NULL,status bool NOT NULL)")

con.execute("INSERT INTO todo (task,status) VALUES ('Read A-byte-of-python to get a good introduction into python',0)")

con.execute("INSERT INTO todo (task,status) VALUES ('visit the python website',1)")

con.execute("INSERT INTO todo (task,status) VALUES ('Test various editors for and check the syntax highlighting',1)")

con.execute("INSERT INTO todo (task,status) VALUES ('choose your favorite WSGI-framwork',0)")

con.commit()
