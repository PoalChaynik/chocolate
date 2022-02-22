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
    "Uzvārds":uzvardss,
    "Vecums":vecumss,
    "Telefona numurs":tell
}

with open("ievaktieDati.json","r", encoding="utf-8") as fails:
    json_data = json.load(fails)

    ir_saraksta =False
    for key in json_data.keys():
        if key == vardss:
            break
        if key != vardss:
            ir_saraksta = True

    if ir_saraksta == False:
        print("Vārds ir sarakstā")
    else:
        json_data[vardss]=vardnica


with open("ievaktieDati.json","w", encoding="utf-8") as fails:
    json.dump(json_data,fails, indent = 4, ensure_ascii=False)
