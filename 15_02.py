#Dati, kurus ievadis:
#Vards
#Uzvards
#Vecums
#Tel. Nr.

#Dati jasaglaba vardnica ({})

#Savaktie dati jasaglaba faila 'ievaktieDati.json'

import json
vardss = input('ievadiet vardu: ')
uzvardss = input('ievadiet uzvardu: ')
vecumss = int(input('ievadiet vecumu: '))
tell = int(input('ievadiet telefona numuru: '))

vardnica = {
    'Vards':vardss,
    'Uzvards':uzvardss,
    'Vecums':vecumss,
    'Telefona Numurs':tell
}

jauni_dati = []

def dati(vards,uzvards,vecums,tel):
    with open('ievaktieDati.json','r',encoding='utf-8') as file:
        a = json.load(file)
        jauni_dati.append(vardnica)
        jauni_dati.append(a)
        print(jauni_dati)
    with open('ievaktieDati.json','w',encoding='utf-8') as file:
        json.dump(jauni_dati,file,indent=4,ensure_ascii=False)


    


dati(vardss,uzvardss,vecumss,tell)