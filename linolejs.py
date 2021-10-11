def gridas_izmaksas(cenas,telpas_garums,telpas_platums):
    kvmetri = round(telpas_garums) * round(telpas_platums)
    cenakv = cenas * kvmetri
    print(cenakv)
gridas_izmaksas(6,5,5)


def gridas_izmaksas2(cena,linoleja_platums,telpas_garums,telpas_platums):

    if telpas_platums%linoleja_platums != 0:
        trukst = telpas_platums%linoleja_platums
        if trukst<=linoleja_platums:
            papildus = round(linoleja_platums * telpas_garums)
            izmaksas = (round(telpas_garums*telpas_platums) + papildus)*cena
        elif trukst > linoleja_platums:
            lin_gab = round(trukst/linoleja_platums)
            papildus = lin_gab * linoleja_platums * telpas_garums
            izmaksas = (round(telpas_garums*telpas_platums) + papildus)*cena
    else:
        izmaksas = round(telpas_platums*telpas_garums)*cena
    
    return izmaksas

print(gridas_izmaksas2(6,1,5,5))

a = 6%5
print(a)