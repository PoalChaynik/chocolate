# bibliotekai lieto {}, katrai vertibai ir sava atslega

lib = {'key1':'Microsoft','key2':'Apple'}
print(lib) #izvada visu lib

print(lib['key1']) #izvada pirmo atslegu no bibliotekas 'lib'

print(len(lib)) # atslegu skaits

lib2 = {'key1':['1','2','3'],'key2':'amogus'} #otra biblioteka kura pirmaja atslega ir vairakas vertibas
print(lib2) # izvada visu lib2
print(lib2['key1'][2]) #izvada lib2 bibliotekas 1 atslegas 1 vertibu (skaitot no 1)
print(lib2['key2']) #izvada otras atslegas vertibu
print(len(lib2))

lib3 = {'key1':{'key2':['Apple','BlackBerry','Microsoft']}} #tresa biblioteka kuras key1 ieksa ir key2 un kura ir jau vertibas
print(len(lib3))

print(lib3['key1']['key2'][0]) #key1 ieksa mekle key2 un izvada 1 vertibu jeb 0
print(lib3['key1']['key2'][1]) #key1 ieksa mekle key2 un izvada 2 vertibu jeb 1
print(lib3['key1']['key2'][2]) #key1 ieksa mekle key2 un izvada 3 vertibu jeb 2


lib4 = {'Pica':{'sastavdalas':['siers','ketchups','desa'],'daudzums':[2,1,10]}} #picas sastavdalas un daudzums
print(lib4['Pica']['sastavdalas'][1]) #izvada 1 jeb 2 vertibu no sastavdalam
print(lib4['Pica']['daudzums']) #izvada daudzumu no picas 