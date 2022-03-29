import random
import json
import sqlite3
import datetime
vecumss = ''
nick = ''
varianti = ['a','s','p']
registracija_notika = False
timerEnd = ''

db = sqlite3.connect('dati.db')
db3 = db.cursor()

db3.execute("""CREATE TABLE IF NOT EXISTS dati
    (id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    nickname TEXT NOT NULL,
    vecums INT NOT NULL,
    win INT NOT NULL,
    lose INT NOT NULL
    )""")

def registracija():
    global registracija_notika
    registracija_notika = True
    print('Registrejieties lai saglabatu datus\n')

    while True:
        nickname = input('ievadiet nickname: ')
        if nickname.isdigit() == False:
            if nickname.strip() == '':
                print('ievadiet nickname atkartoti')
                continue
            else:
                nick = nickname
                break
        else:
            print('ievadiet nickname atkartoti')
            continue

    while True:
        vecums = input('ievadiet vecumu: ')
        if vecums.isdigit():
            vecumss = vecums
            break
        else:
            print('ievadiet vecumu atkartoti')
            continue

    db3.execute("""INSERT INTO dati
        (nickname, vecums, win, lose)
        VALUES (:nickname,:vecums,0,0)
    """,{'nickname':nick,'vecums':vecumss})

    db.commit()
        

def winning():
    print("Uzvara|Zaudejums:",win,lose)
    global timerEnd
    if registracija_notika == False:
        timerEnd = datetime.datetime.now() - TimerStart
        print(timerEnd)
    if win == True and registracija_notika == True:
        db.execute("""UPDATE dati SET win = win + 1 WHERE id = (SELECT MAX(id) FROM dati)""")
        db.commit()
        saving()
    elif lose == True and registracija_notika == True:
        db.execute("""UPDATE dati SET lose = lose + 1 WHERE id = (SELECT MAX(id) FROM dati)""")
        db.commit()
        saving()

def saving():
    dats = db3.execute("SELECT * FROM dati")
    rezultats = dats.fetchall()
    
    with open("speletaju_dati.json","w", encoding="utf-8") as fails:
        json.dump(rezultats,fails, indent = 4, ensure_ascii=False)
    global timerEnd
    timerEnd = datetime.datetime.now() - TimerStart
    print(timerEnd)

db.commit()

def LocalGame():
    global win
    global lose
    win = False
    lose = False
    while True:
        p1 = input("[Player1] Izvelieties: 'a' - akmens, 's' - skeres, 'p' - papirits\n")
        for i in varianti:
            if p1 == i:
                break
        if p1 == i:
            break
        else:
            continue

    while True:
        p2 = input("[Player2] Izvelieties: 'a' - akmens, 's' - skeres, 'p' - papirits\n")
        for i in varianti:
            if p2 == i and p2 != p1:
                break
        if p2 == i and p2 != p1:
            break
        else:
            continue

    a = varianti[0]
    s = varianti[1]
    p = varianti[2]
    global TimerStart
    TimerStart = datetime.datetime.now()
    if p1 == a:
        if p2 == s:
            print('akmens x skeres = WIN!')
            win = True
            
        elif p2 == p:
            print('akmens x papirits = LOSE...')
            lose = True
            

    if p1 == s:
        if p2 == a:
            print('skeres x akmens = LOSE...')
            lose = True
        elif p2 == p:
            print('skeres x papirits = WIN!')
            win = True

    if p1 == p:
        if p2 == a:
            print('papirits x akmens = WIN!')
            win = True
        if p2 == s:
            print('papirits x skeres = LOSE...')
            lose = True
    
    winning()

def CPU():
    global win
    global lose
    win = False
    lose = False
    while True:
        p1 = input("[Player1] Izvelieties: 'a' - akmens, 's' - skeres, 'p' - papirits\n")
        for i in varianti:
            if p1 == i:
                break
        if p1 == i:
            break
        else:
            continue

    while True:
        p2 = random.choice(varianti)
        for i in varianti:
            if p2 == i and p2 != p1:
                break
        if p2 == i and p2 != p1:
            break
        else:
            continue

    a = varianti[0]
    s = varianti[1]
    p = varianti[2]
    global TimerStart
    TimerStart = datetime.datetime.now()
    if p1 == a:
        if p2 == s:
            print('akmens x skeres = WIN!')
            win = True
        elif p2 == p:
            print('akmens x papirits = LOSE...')
            lose = True

    if p1 == s:
        if p2 == a:
            print('skeres x akmens = LOSE...')
            lose = True
        elif p2 == p:
            print('skeres x papirits = WIN!')
            win = True

    if p1 == p:
        if p2 == a:
            print('papirits x akmens = WIN!')
            win = True
        if p2 == s:
            print('papirits x skeres = LOSE...')
            lose = True
    
    winning()


while True:
    start = input("Izvelieties Speles Rezimu: '1' - Pret Datoru, '2' - Lokala Spele, '3' - Registracija, '4' - Iziet\n")
    if start == '1':
        CPU()
    elif start == '2':
        LocalGame()
    elif start == '3':
        registracija()
    elif start == '4':
        db.close()
        exit()
