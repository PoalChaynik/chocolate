import datetime
import sqlite3
import xlsxwriter
from tracemalloc import start
start = datetime.datetime.now()
db = sqlite3.connect('titanicDB.db')

print(datetime.datetime.today())

tabulu_nosaukumi = db.execute("""SELECT name FROM sqlite_schema WHERE type = 'table'

""")

rezultati = tabulu_nosaukumi.fetchall()
print(rezultati)


kolonnu_nosaukumi = db.execute("""SELECT name FROM pragma_table_info('titanic')""")
rezultati = kolonnu_nosaukumi.fetchall()
print(rezultati)
# isaks for cilka pieraksts
[print(rinda[0]) for rinda in rezultati]

dati = db.execute("""SELECT Name, Age FROM titanic WHERE Survived > 0
ORDER BY Name
""")
rezultati = dati.fetchall()
[print(rinda[0],rinda[1], end=" ") for rinda in rezultati]
print('\n')
print(len(rezultati),'Cilveki izdzivoja')

file = xlsxwriter.Workbook('titanika_cilveki.xlsx')
lapa = file.add_worksheet()


for a in range(151):
    for rinda in rezultati:
        lapa.write(f'A{a}','aa')

end = datetime.datetime.now()
laiks = end-start
print('\n')
print(laiks)