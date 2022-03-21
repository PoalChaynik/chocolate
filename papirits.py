varianti = ['a','s','p']

while True:
    p1 = input("Izvelieties: 'a' - akmens, 's' - skeres, 'p' - papirits\n")
    for i in varianti:
        if p1 == i:
            break
    if p1 == i:
        break
    else:
        continue

while True:
    p2 = input("Izvelieties: 'a' - akmens, 's' - skeres, 'p' - papirits\n")
    for i in varianti:
        if p2 == i and p2 != p1:
            break
    if p2 == i and p2 != p1:
        break
    else:
        continue


print(p1,p2)
