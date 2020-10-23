import sqlite3

conn = sqlite3.connect('smarket.db')

c = conn.cursor()
c.execute("SELECT * FROM smarket")
data = c.fetchall()
for datum in data:
    print(datum[0] + "\t" + datum[1] + "\t" + datum[2] + "\t" + datum[3] + "\t" + datum[4] + "\t" + datum[5] + "\t" + datum[6] + "\t" + datum[7] + "\t" + datum[8] + "\t" + datum[9])

conn.close()
