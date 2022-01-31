#Teksta datņu atvēršana, nolasīšana, aizvēršana

#1. veids
file = open('pirmais.txt','r', encoding='utf-8')
print(file.read())
file.close()
print() #atstarpe

#2. veids
with open('pirmais.txt','r', encoding='utf-8') as file:
    print(file.read())
    file.close()
print() 

#Linijas izvade
file = open('pirmais.txt','r', encoding='utf-8')
print(file.readline())
file.close()

#Simbolu izvade
file = open('pirmais.txt','r', encoding='utf-8')
print(file.read(5))
file.close()