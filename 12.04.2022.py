import sqlite3

db = sqlite3.connect('titanicDB.db')

tabulu_nosaukumi = db.execute("""SELECT name FROM sqlite_schema WHERE type = 'table'""")

rezultati = tabulu_nosaukumi.fetchall()
print(rezultati)

kolonna = db.execute("""SELECT name FROM pragma_table_info('titanic')""")
rezultati = kolonna.fetchall()
print(rezultati)

dati1 = db.execute("SELECT PassengerId, Name FROM titanic")
rezultati = dati1.fetchall()
print(rezultati)

dati2 = db.execute("SELECT PassengerId, Name FROM titanic")
rezultati = dati2.fetchall()
for i in rezultati:
    print(i[0],i[1])

dati4 = db.execute("SELECT * FROM titanic ORDER BY Age ASC")
print(dati4.fetchall())

dati5 = db.execute("SELECT SUM(Survived) FROM titanic WHERE Survived > 0")
print(dati5.fetchall())


dati6 = db.execute("SELECT UPPER(Name) FROM titanic2 ")
print(dati6.fetchall())