#Tuples

# ()

'''
Aleksis Pocs
Tuples and Sets
'''


newTuple = ('skola','majas','pagrabs')
print(newTuple)
print(len(newTuple)) #elementu daudzums

print(newTuple[1]) #piekluve elementam

print(newTuple.index('majas')) #elementa numuru var dabut

newTuple = (1,1,0,0,1,0,1,1,0,1,0,0,1,1,0,1,0,0,1)
print(newTuple.count(0)) #saskaita cik 0 ir tupele

#Set

# {}
# Sets izvadas randoma seciba

newSet = {'a'} #pie tuksa seta nedrikst lietot komandu .add()
print(newSet)
newSet.add('e') #pievieno jaunu elementu setam
print(newSet)
newSet.add('e') #ja pievieno setam elementu kas jau eksiste tad izvadis tikai vienu reizi (neatkartojas)
print(newSet)
newSet.add(1) #ciparus ari var pievienot
print(newSet)
list = ['arbuzs','piens'] #veido sarakstu
print(list)
newSet = set(list) #ievieto setam elementus no saraksta
print(newSet)