import sqlite3

conn = sqlite3.connect('smarket.db')

c = conn.cursor()
c.execute("""DROP TABLE smarket""")
conn.close()
