#Dati, kurus ievadis:
#Vards
#Uzvards
#Vecums
#Tel. Nr.

#Dati jasaglaba vardnica ({})

#Savaktie dati jasaglaba faila 'ievaktieDati.json'

import json
#varda parbaude
while True:
    vardss = input('ievadiet vardu: ')
    if vardss.isdigit() == False:
        if vardss.strip() == '':
            print('ievadiet vardu atkartoti')
            continue
        else:
            break
    else:
        print('ievadiet vardu atkartoti')
        continue

        
#uzvarda parbaude
while True:
    uzvardss = input('ievadiet uzvardu: ')
    if uzvardss.isdigit() == False:
        if uzvardss.strip() == '':
            print('ievadiet uzvardu atkartoti')
            continue
        else:
            break
    else:
        print('ievadiet uzvardu atkartoti')
        continue

#vecuma parbaude
while True:
    vecumss = input('ievadiet vecumu: ')
    if vecumss.isdigit():
        break
    else:
        print('ievadiet vecumu atkartoti')
        continue
#telefona numura parbaude
while True:
    tell = input('ievadiet telefona numuru: ')
    if tell.isdigit():
        if len(tell) == 8:
            break
    else:
        print('ievadiet telefona numuru atkartoti')
        continue

vardnica = {
    "Uzvārds":uzvardss,
    "Vecums":vecumss,
    "Telefona numurs":tell
}

with open("ievaktieDati.json","r", encoding="utf-8") as fails:
    json_data = json.load(fails)

    ir_saraksta = True
    for key in json_data.keys():
        if key == vardss:
            if not isinstance(json_data[vardss],list):
                json_data[vardss] = [json_data[vardss]]
            json_data[vardss].append(vardnica)
            if_saraksta = True
            print('key==vards')
            break
        else:
            ir_saraksta = False

    if not ir_saraksta:
        print('navSaraksta')
        json_data[vardss]=vardnica


with open("ievaktieDati.json","w", encoding="utf-8") as fails:
    json.dump(json_data,fails, indent = 4, ensure_ascii=False)
