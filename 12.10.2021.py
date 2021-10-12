def atgriez_skaitli(skaitlis1,skaitlis2):
    skaitli = [skaitlis1,skaitlis2]
    length = len(skaitli)
    for sk in range(length):
        if skaitli[0] and skaitli[1] %2==0:
            return min(skaitli)
        if skaitli[0] or skaitli[1]%2!=0:
                return max(skaitli)

print(atgriez_skaitli(6,2))

def sakas_vienadi(vards):
    vards = vards.lower().split()
    if vards[0][0] == vards[1][0]:
        return True
    else: 
        return False

print(sakas_vienadi('Maza Lama'))
print(sakas_vienadi('Liela Lama'))