import random
import json
import sqlite3
vecumss = ''
nick = ''
varianti = ['a','s','p']

def registracija():
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

def LocalGame():
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

    if p1 == a:
        if p2 == s:
            print('akmens x skeres = WIN!')
        elif p2 == p:
            print('akmens x papirits = LOSE...')

    if p1 == s:
        if p2 == a:
            print('skeres x akmens = LOSE...')
        elif p2 == p:
            print('skeres x papirits = WIN!')

    if p1 == p:
        if p2 == a:
            print('papirits x akmens = WIN!')
        if p2 == s:
            print('papirits x skeres = LOSE...')


def CPU():
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

    if p1 == a:
        if p2 == s:
            print('akmens x skeres = WIN!')
        elif p2 == p:
            print('akmens x papirits = LOSE...')

    if p1 == s:
        if p2 == a:
            print('skeres x akmens = LOSE...')
        elif p2 == p:
            print('skeres x papirits = WIN!')

    if p1 == p:
        if p2 == a:
            print('papirits x akmens = WIN!')
        if p2 == s:
            print('papirits x skeres = LOSE...')


while True:
    start = input("Izvelieties Speles Rezimu: '1' - Pret Datoru, '2' - Lokala Spele, '3' - Registracija, '4' - Iziet\n")
    if start == '1':
        CPU()
    elif start == '2':
        LocalGame()
    elif start == '3':
        registracija()
    elif start == '4':
        exit()
