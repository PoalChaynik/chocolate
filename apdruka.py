
def pasuti_tkreklus(skaits,apdruka,piegade):
    cenas = {'teksts':5,'zime':7,'foto':20}
    piegade_c = 15

    if cenas['teksts']:
        if piegade == True:
            summap = skaits * cenas['teksts'] + piegade_c
        else:
            summa = skaits * cenas['teksts']
            
    if cenas['zime']:
        if piegade == True:
            summap = skaits * cenas['zime'] + piegade_c
        else:
            summa = skaits * cenas['zime']
            
    if cenas['foto']:
        if piegade == True:
            summap = skaits * cenas['foto'] + piegade_c
        else:
            summa = skaits * cenas['foto']

        
    if summap - piegade_c > 50 and summap - piegade_c < 100:
        summap = summap - piegade_c
        print(summap)
    elif summap - piegade_c < 50:
        print(summap)

    if summap - piegade_c > 100:
        print('Atlaide 5%!')
        atlaide = summap * 0.05
        print(summap - atlaide)
    else:
        print(summap)


    






pasuti_tkreklus(6,'teksts',True)
