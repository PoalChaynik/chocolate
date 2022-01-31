#1
file = open('otrais.txt','r', encoding='utf-8')
print(file.read())
file.close()

#2
file2 = open('otrais.txt','r', encoding='utf-8')
print('simbolu skaits:',len(file2.read()))
file2.close()

#3
file3 = open('otrais.txt','r', encoding='utf-8')
print('pirmie 10 simboli:',file3.read(10))
file3.close()

#4
file4 = open('otrais.txt','r', encoding='utf-8')
lines = file4.read()
print(lines[0])
print(lines[-1])
file4.close()

#5
file5 = open('otrais.txt','r', encoding='utf-8')
lines = file5.readlines()
print(lines[3])
file5.close()