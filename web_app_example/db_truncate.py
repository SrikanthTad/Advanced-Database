import sqlite3
conn = sqlite3.connect('todo.db') # Warning: This file is created in the current directory
conn.execute("DELETE FROM todo")

conn.commit()
