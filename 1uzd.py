#pirmais punktu bloks
text1 = "a " + "b"
print(text1)
text2 = 'a','b'
print(text2)

#otrais punktu bloks
a = int(1) #vesels skaitlis
b = float(3.9) #decimalskaitlis
print(a,b)

#tresais punktu bloks
c = a / b
print(c)
print(a,"dalit ar",b,"ir vienads ar",c)

#ceturtais punktu bloks
print('{0} dalit ar {1} ir vienads ar {2}' .format(a,b,c))

#piektais punktu bloks
list = [text1,text2,a,b,c]
print(list)

#sestais punktu bloks
print(len(list))

#septitais punktu bloks
list.append('banana')
print(list)

#astotais punktu bloks
list[2] = "amogus"
print(list)