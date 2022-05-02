from unittest import skip


x = 5
print(x)

skaitlis = 7
if(skaitlis > 7):
    print("Labinieks")

skaitlis = 10000
a = skaitlis / 2
print(a)

a = [1, 2, 3]
print ("Otrais elements = %d" %(a[1]))
 
print ("Trešais elements = %d" %(a[2]))

def funkcija(a):
    if a < 4:
        if a-3 != 0:
            b = a/(a-3)
            print("Value of b = ", b)
    
funkcija(3)
funkcija(5)

x = ("four")
print(x)

a = 'viens'
b = 'divi'
print('%s,%s'%(a,b))

for i in [-2, -1, 0, 1, 2]:
    if i == 0:
        i += 1
    print(1 / i)