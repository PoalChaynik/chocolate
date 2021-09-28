'''
Aleksis Počs
28.09.2021
For un While Loop
'''


'''
For Loops
'''

#saraksta list iteracija
list = [1,2,3,4,5,6,7,8,9,10]
for i in list:
    print(list)

#Tikai para skaitlu izvade

for i in list:
    if i % 2 == 0:
        print(i)
        
#Else pievienosana

for i in list:
    if i % 2 == 0:
        print(i)
    else:
        print('nav otrais skaitlis')

#Vardu saraksta specifiska izvade

list2 = ['Iphone','Samsung','Xiaomi']

for list2[0] in list2:
    print('Tas ir',list2[0])

#skaitli konkreta diapazona/intervala

for list[0] in range(1,11,1):
    print(list[0])



'''
While Loops
'''
print('sakas While loops\n')

#while loops ar skaititaju
kakis = 'kakis'
number = 1
while number < 101:
    print(kakis + str(number))
    number += 1

#break apgalvojums
suns = 'suns'
number = 1
while number == number:
    print(suns + str(number))
    number += 1
    if number == 101:
        print("while cikls beidzas")
        break

#continue apgalvojums
number = 1
while number < 100:
    number += 1
    if number == 100:
        continue
    print(number)
#es nezinu ko tas dara

#Else apgalvojums
zebra = 1
while zebra < 50:
    print(zebra)
    zebra += 1
else:
    print(zebra)
    print('zebru skaits beidzas')
    