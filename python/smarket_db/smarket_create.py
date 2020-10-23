import sqlite3, csv

conn = sqlite3.connect('smarket.db')

c = conn.cursor()
c.execute("""CREATE TABLE smarket (Year, Lag1, Lag2, Lag3, Lag4, Lag5, Volume, Today, Direction, Probability);""")

with open('Smarket_new.csv', 'r') as data:
    dr = csv.DictReader(data)
    db = [(i['Year'], i['Lag1'], i['Lag2'], i['Lag3'], i['Lag4'], i['Lag5'], i['Volume'], i['Today'], i['Direction'], i['Prob']) for i in dr]

c.executemany("""INSERT INTO smarket (Year, Lag1, Lag2, Lag3, Lag4, Lag5, Volume, Today, Direction, Probability) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""", db)
conn.commit()
conn.close()
