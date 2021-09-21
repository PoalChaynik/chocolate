#Var saturet tekstu vai skaitlus

list = ['text', 1, 10] # lai veidotos saraksts ir jaizmanto = []
print(list)

print("Elementu skaits:",len(list)) #elementu skaits saraksta

# print = izvade, list = saraksts, [jebkurs elementa numurs] = izvelas to elementu kas ir ar to numuru saistits

print(list[1]) #izvada 1 elementu (skaita no 0)
print(list[0:1])

#elementu maina

list[1] = "sky" #pamaina 1 elementu no cipara 1 uz tekstu "sky"
print(list)

#elementu pievienosana

list = list + ['ccc'] #pievieno pie jau esosa list jaunu mainigo
print(list)

list.append(2021) #veic to pasu ko komanda augstak
print(list)

list.pop(3) # izdzes no saraksta noradito elementu
print(list)