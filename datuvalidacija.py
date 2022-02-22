
while True:
    vards = input('ievadi savu vardu: ')
    if vards.strip() == '':
        print('ievadi vardu atkartoti')
        continue
    else:
        break

print(vards)

while True:
    vecums = input('ievadi savu vecumu: ')
    if vecums.isdigit():
        print(vecums)
        break
    else:
        print('ievadiet vecumu atkartoti: ')
        continue

while True:
    tel = input('ievadi savu tel.nr: ')
    if tel.isdigit():
        if len(tel) == 8:
            print(tel)
            break
        else:
           print('ievadiet tel.nr atkartoti')
           continue
    else:
        print('ievadiet tel.nr atkartoti')
        continue