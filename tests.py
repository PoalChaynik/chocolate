# #1
# num = (input("Ievadi veselu skaitli: "))
# mod = num / 2
# if mod > 0:
#     print("Nepāra skaitlis.")
# else:
#     print("Pāra skaitlis.")

# #2
# r = float(input("Ieraksti riņķa rādiusu: "))
# pi = 3.14
# laukums = pi * r**2
# print(f"Riņķa laukums ir {laukums}")

#3
# num = int((input("Ievadi veselu skaitli: ")))
# mod = num / 0
# if mod > 0:
#     print("Nepāra skaitlis.")
# else:
#     print("Pāra skaitlis.")

# #4
# y = int(input("Ievadi gadu : "))
# m = (input("Ievadi mēnesi : "))
# print(calendar.month(y, m))

# #5
# #Dota programma, kuras uzdevums ir saskaitīt simbolus, kas atrodas teksta mainīgajā
# #Testēšana: string_length('Programmēšana') ------> 13

# def string_length(str1):
#     count = 0
#     for char in str1:
#         count += 1
#     return count

# print(string_length('Programmesana'))

# #6
# # Dota programma, kuras uzdevums ir noteikt, vai ievadītais skaitlis ir pāra vai nepāra
# # Testēšana: 5 -----> Nepāra skaitlis.
# #            6 -----> Pāra skaitlis.
# while True:
#     try:
#         num = int((input("Ievadi veselu skaitli: ")))
#     except ValueError:
#         print("Ievadi skaitli!")
#     else:
#         break
        
# mod = num % 2
# if mod > 0:
#     print("Nepāra skaitlis.")
# else:
#     print("Pāra skaitlis.")

#7
#Dota programma, kuras uzdevums ir izvadīt dotā teksta pirmos divus un pēdējos divus simbolus, ja teksts sastāv no mazāk kā diviem simboliem, jāatgriež tukšs teksta mainīgais
# Testēšana: string_both_ends('Programmēšana') ------> Prna
#            string_both_ends('Pr') --------> PrPr
#            string_both_ends('P') -------> ''

# def string_both_ends(str):
#     if len(str) >= 2:
#         return str[0:2] + str[-2:]
#     else:
#         return



# print(string_both_ends('P'))

#8
# r = float(input("Ieraksti riņķa rādiusu: "))
# pi = 3,14
# laukums = pi * r**2
# print(f"Riņķa laukums ir {laukums}")

#9
# krasu_saraksts = ["Sarkans","Zaļš","Balts""Melns"]
# print( "%s %s"%(krasu_saraksts[5],krasu_saraksts[-1]))

# Dota programma, kuras uzdevums ir izveidot vienu simbolu virkni (string) no dotajām (a,b), samainot to pirmos simbolus vietām
# Testēšana: chars_mix_up('abc', 'xyz') ------> xyc abz
# def chars_mix_up(a, b):
#   new_a = b[:2] + a[2:]
#   new_b = a[:2] + b[2:]

#   return ('%s %s' %(new_a,new_b))


# print(chars_mix_up('abc','xyz'))

#10
# Dota programma, kuras uzdevums ir atgriezt garāko vārdu un tā garumu no dotā saraksta
# Testēšana: find_longest_word(["Python", "Ieskaite", "Programmēšana"]) -------->  ('Programmēšana', 13)
def find_longest_word(words_list):
    word_len = []
    for n in words_list:
        word_len.append((len(n), n))
    word_len.sort()
    length = word_len[-1][0]
    long_word = word_len[-1][1]
    return long_word, length

print(find_longest_word(["Python","Ieskaite","Programmesana"]))