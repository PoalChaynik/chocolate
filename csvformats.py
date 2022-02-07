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

#satura nolasisana

saturs = []
for rinda in csv_lasit:
    saturs.append(rinda)

print(saturs)
print(type(saturs))

file.close()

#jauna faila izveide

kolonnuNosaukumi = ['Vards','1.atzime','2.atzime']
dati = [['Gregorijs',9,2], ['Patriks',10,5], ['Eriks',8,6]]

fails2 = open('vardi.csv','w',encoding='utf-8',newline='')
csvwrite = csv.writer(fails2)
csvwrite.writerow(kolonnuNosaukumi)
csvwrite.writerows(dati)
fails2.close()

#Ielasi datnes saturu, parveido to par masivu

with open('vardi.csv','r',encoding='utf-8') as fails:
    lasit = csv.reader(fails)
    saturss = []
    for rinda in lasit:
        saturss.append(rinda)

    print(saturss)
    #Masiva garums
    print(len(saturss),'rindas')

    #Pirma elementa saturs
    print(saturss[0])

    #izvadi pirmo 3 elementu saturu
    for s in range(3):
        print(saturss[s])


#define funkciju, kas ka argumentus izmanto datnes nosaukumu un elementa kartas numuru
#Izvadi attiecigo elementu

def funkcija(nosaukums,kartasNr):
    with open(nosaukums,'r',encoding='utf-8') as fails:
        lasit = csv.reader(fails)
        saturss = []
        for rinda in lasit:
            saturss.append(rinda)
        print(saturss[kartasNr])

funkcija('vardi.csv',0)