# #Teksta datņu atvēršana, nolasīšana, aizvēršana

# #1. veids
# file = open('pirmais.txt','r', encoding='utf-8')
# print(file.read())
# file.close()
# print() #atstarpe

# #2. veids
# with open('pirmais.txt','r', encoding='utf-8') as file:
#     print(file.read())
#     file.close()
# print() 

# #Linijas izvade
# file = open('pirmais.txt','r', encoding='utf-8')
# print(file.readline())
# file.close()

# #Simbolu izvade
# file = open('pirmais.txt','r', encoding='utf-8')
# print(file.read(5))
# file.close()

#Jauna teksta faila izveide

file = open('tresais.txt','w',encoding='utf-8')
file.write('Test 123 abc\n')

teksts = ['Ir 2022.gads \n','Ir 2022.gada 1. februaris\n','Sveiki']
file.writelines(teksts)
file.close
file = open('tresais.txt','r',encoding='utf-8')
print(file.read())
file.seek(0) #"kursora" parvietosana uz faila sakumu
print(file.readline())

file = open('tresais.txt','a',encoding='utf-8')
file.write(' kuku')