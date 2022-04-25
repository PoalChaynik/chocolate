# Lietotājs ievada divus veselus skaitļus a un b. Izvadi visus skaitļus šajā intervālā (ieskaitot)!

a = int(input("Ievadi a:"))
b = int(input("Ievadi b:")) 
# Mainīgais, kuram vajadzēja būt nosauktam 'b' saucās 'a' (Izpildlaika kļūda)

for i in range(a, b + 1): 
    #[Nav Kļūda, manuprāt, bet lai paliek] Lai izvadītu pēdējo skaitli ieskaitot jāpievieno vēl klāt skaitlis (Sākotnēji kompilēšanas kļūda)
    print(i) 
    #Līmenis nepareizs (Kompilēšanas kļūda)

    
# Lietotājs ievada veselu pozitīvu skaitli. Izdrukā visus skaitļus sākot no ievadītā līdz 0 (neieskaitot)!

sk = int(input("Ievadi skaitli:"))
while sk > 0:
    print(sk)
    #Līmenis nepareizs (Kompilēšanas kļūda)
    sk -= 1 
    #Šī darbība nekad netiks izpildīta, tā līmenis ir jāpārnes augstāk par vienu lai viss darbotos (Izpildlaika kļūda)

# Lietotājs ievada vairākus skaitļus vienā rindā, atdalot tos ar atstarpi. Izvadi tos skaitļus, kuri ir vienādi un atrodas blakus!

saraksts = [int(sk) for sk in input("Ievadi skaitlus, atdalot tos ar atstarpi:").split()]

for i in range(len(saraksts)):
    if saraksts[i] == saraksts[i + 1] and saraksts[i] != len(saraksts):
        #Līmenis nepareizs (Kompilēšanas kļūda)
        print(saraksts[i], saraksts[i + 1])
        #Līmenis nepareizs (Kompilēšanas Kļūda)
    else:
        break