#Var izmantot iebuveto moduli csv
import csv

file = open('csv_meg.csv','r',encoding='utf-8')
print(type(file))

csv_lasit = csv.reader(file)
print(csv_lasit)

#Kolonnu nosaukumi

header = []
header = next(csv_lasit)
print(header)