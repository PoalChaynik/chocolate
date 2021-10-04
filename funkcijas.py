'''
Aleksis Pocs
04.10.2021
'''

#Funkcijas definesana

def count():
    for i in range(5):
        print(i)

count()

#Funkcija ar vienu parametru

def one(ball):
    print('diamond',ball)

one(ball='horse')


#Funkcija ar diviem parametriem

def money(one,two):
    print('i have',one,two)

money(one='three hundred',two='bucks')

#Funkcija ar diviem parametriem izmantojot return

def player(p1,p2):
    return p1 + p2
    
plrone = 'player one'
plrtwo = 'player two'

print(player(plrone,plrtwo))

#Trenins ieskaitei
s = int(input('ievadi skaitli: '))

def counting(one,two,three):
    for one in range(one,two,three):
        print(one)

if s == 1:
    counting(one=s,two=s+10,three=1)
else:
    counting(one=s,two=s+11,three=1)

