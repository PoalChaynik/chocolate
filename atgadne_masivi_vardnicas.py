#Masivs jeb list

#Pirmais indekss ir 0
#Lai pieklutu vertiba, ir nepieciesams zinat indksu
#Masiva garums NAV pedejais indekss
#Masiva pedejais indekss: masiva garums - 1

"""
Vertiba |A|B|C|D|E|F|
Indekss |0|1|2|3|4|5|
"""

masivs = ["A",'B','C','D','E','F']
print(masivs)
print(type(masivs))
print(masivs[3])

for x in masivs:
    print(x)

#Vardnica jeb Dictionary

#Katrai vertibai ir sava atslega

"""
Atslega |Vards|Izglitiba|Vecums|
Vertiba |Janis| Videja  |  20  |
"""

vardnica = {'Vards':'Janis','Izglitiba':'Videja','Vecums':20}
print(vardnica)
print(type(vardnica))
print(vardnica['Vards'])

#Kombinacija - vardnica masiva

kombinacija = [
    {'Vards':'Janis','Izglitiba':'Videja','Vecums':20},
    {'Vards':'Edgars','Izglitiba':'Augstaka','Vecums':33}
]

print(kombinacija,type(kombinacija))

for x in kombinacija:
    print(x['Vards'])