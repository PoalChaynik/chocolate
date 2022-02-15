#Definet funkciju, kuras argumenti ir divi csv failu nosaukumi
#Parveidot failus masivos
#Jasalidzina masivu garumi

#Ja masivi ir vienadi
#Tos apvieno un rezultatu saglaba jauna datne
import csv

def salidzinasana(nosaukums1,nosaukums2):
    file1 = open(nosaukums1,'r',encoding='utf-8')
    lasit1 = csv.reader(file1)
    saturs1 = []
    for rinda in lasit1:
        saturs1.append(rinda)
    file2 = open(nosaukums2,'r',encoding='utf-8')
    lasit2 = csv.reader(file2)
    saturs2 = []
    for rinda2 in lasit2:
        saturs2.append(rinda2)
    file1.close()
    file2.close()
    print(len(saturs1),len(saturs2))
    if len(saturs1) == len(saturs2):
        file3 = open('result.csv','w',encoding='utf-8',newline='')
        csvwritee = csv.writer(file3)
        csvwritee.writerows(saturs2)
        csvwritee.writerows(saturs1)
        file3. close
    unikalie = []     

    for unik in saturs1:
        if unik not in saturs2:
            unikalie.append(unik)

    unikalie2 = []

    for unik2 in saturs2:
        if unik2 not in saturs1:
            unikalie2.append(unik2)
    print(unikalie,'\n',unikalie2)

    vienadie = []

    for vienads in saturs1:
        if vienads in saturs2:
            vienadie.append(vienads)

    print(vienadie)

    
    



salidzinasana('pirmais.csv','otrais.csv')


#Define funkciju, kuras argumenti ir divu json failu nosaukumi
#Parveido failus par vardnicam

#Abas vardnicas apvienot un ierakstit rezultatu jauna json faila

#Salidzinat vardnicu atslegas un izvadit tikai tos datus, kuri ir atrodami viena/abas vardnicas
import json
kopa = []
def jason(name1,name2):
    file1 = open(name1,'r',encoding='utf-8')
    file2 = open(name2,'r',encoding='utf-8')
    a = json.load(file1)
    b = json.load(file2)
    kopa.append(a)
    kopa.append(b)
    file2.close()
    file1.close()
    file3 = open('rezultats.json','w',encoding='utf-8')
    json.dump(kopa,file3,indent=4, separators=(',',':'))
    
    for i in b.values():
        if i not in a.values():
            print(i)
            
    for i in a.values():
        if i not in b.values():
            print(i)
        if i in b.values():
            print(i)



    

jason('viens.json','divi.json')