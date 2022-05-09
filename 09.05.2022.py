# # 1
# # Dota programma, kuras uzdevums ir aprēķināt riņķa laukumu
# # Testēšana: 3 ----> 28.26
# r = float(input("Ieraksti riņķa rādiusu: "))
# pi = 3.14
# laukums = pi*(r**2)
# print(f"Riņķa laukums ir {laukums}")

# # 2
# # Dota programma, kuras uzdevums ir izvadīt lietotāja ievadīto vārdu un uzvārdu apgrieztā secībā (starp vārdu un uzvārdu ir jābūt atstarpei)
# # Testēšana: Anna Bērziņa -----> Bērziņa Anna
# vards = input("Ievadi vārdu: ")
# uzvards = input("Ievadi uzvārdu: ")
# print (uzvards, vards)

# # 3
# #Dota programma, kuras uzdevums ir - lietotāja ievadītos skaitļus (kas atdalīti ar komatiem), izdrukāt kā sarakstu(list) un kortežu(tuples)
# #Testēšana: 1,2,3,4,5,6 -----> Saraksts: ['1','2','3','4','5','6']
# # -----> Kortežs: ('1','2','3','4','5','6')
# vertibas = input("Ievadi skaitļus, atdalot tos ar komatiem: ")
# saraksts = vertibas.split(",")
# kortezs = tuple((saraksts))
# print('Saraksts : ',saraksts)
# print('Kortežs : ',kortezs)

# # 4
# #Dota programma, kuras uzdevums ir izvadīt pirmo un pēdējo krāsu no dotā saraksta
# #Testēšana: ------> Sarkans, melns
# krasu_saraksts = ["Sarkans","Zaļš","Balts","Melns"]
# print("%s, %s"%(krasu_saraksts[0],krasu_saraksts[-1]))

# # 5
# #Dota programma, kuras uzdevums ir veikt sekojošo matemātisko darbību ar ievades skaitli (n): n+nn+nnn
# #Testēšana: 5 ----> 615
# a = int(input("Ievadi veselu skaitli: "))
# n1 = int( "%s" % (a) )
# n2 = int( "%s%s" % (a,a) )
# n3 = int( "%s%s%s" % (a,a,a) )
# print (n1+n2+n3)

# # 6
# #Dota programma, kuras uzdevums ir izvadīt lietotāja ievadītā mēneša kalendāru
# #Testēšana: 2015 ---------> May 2015
# # 4 ---------> Mo Tu We Th Fr Sa Su
# # 1 2 3
# # 4 5 6 7 8 9 10
# # 11 12 13 14 15 16 17
# # 18 19 20 21 22 23 24
# # 25 26 27 28 29 30 31
# import calendar
# y = int(input("Ievadi gadu : "))
# m = int(input("Ievadi mēnesi : "))
# print(calendar.month(y, m))

# # 7
# #Dota programma, kuras uzdevums ir salīdzināt doto ciparu (n) ar 17, ja n ir lielāks par 17, tad nepieciešams atgriezt šo skaitļu starpību dubultā, bet, ja n ir mazāks vai vienāds ar 17, nepieciešams atgriezt šo skaitļu starpību
# #Testēšana: starpiba(22) -----> 10
# # starpiba(14) -----> 3
# def starpiba(n):
#     if n <= 17:
#         return 17 - n
#     elif n > 17:
#         return (n - 17) * 2

# print(starpiba(22))
# print(starpiba(14))

# # 8
# #Dota programma, kuras uzdevums ir atgriezt doto skaitļu (x,y,z) summu, bet, ja skaitļi x,y un z ir vienādi, jāatgriež šo skaitļu summa reizināta ar 3
# #Testēšana: summa(1,2,3) -----> 6
# # summa(3,3,3) -----> 27
# def summa(x, y, z):
#     if x == y == z:
#         sum = (x+y+z)*3
#     else:
#         sum = x + y + z
#     return sum

# print(summa(1,2,3))
# print(summa(3,3,3))

# # 9
# # Dota programma, kuras uzdevums ir noteikt, vai ievadītais skaitlis ir pāra vai nepāra
# # Testēšana: 5 -----> Nepāra skaitlis.
# # 6 -----> Pāra skaitlis.
# num = int(input("Ievadi veselu skaitli: "))
# mod = num % 2
# if mod == 0:
#     print("Pāra skaitlis.")
# else:
#     print("Nepāra skaitlis.")

# # 10
# # Dota programma, kuras uzdevums ir saskaitīt 4 dotajā sarakstā
# # Testēšana: list_count_4([1, 4, 6, 7, 4]) -----> 2
# # list_count_4([1, 4, 6, 4, 7, 4]) ------> 3
# def list_count_4(nums):
#     count = 0
#     for num in nums:
#         if num == 4:
#             count += 1    
#     return count

# print(list_count_4([1,4,6,7,4]))
# print(list_count_4([1,4,6,4,7,4]))

# # 11
# # Dota programma, kuras uzdevums ir pārbaudīt vai dotajā sarakstā ir konkrēta vērtība (n)
# # Testēšana: is_group_member([1, 5, 8, 3], 3) -------> True
# # is_group_member([5, 8, 3], -1) --------> False
# def is_group_member(group_data, n):
#     print(group_data,n)
#     for value in group_data:
#         if n == value:
#             return True
#     if n != value:
#         return False

# print(is_group_member([1,5,7,3],3))
# print(is_group_member([5,8,3],-1))

# # 12
# # Dota programma, kuras uzdevums ir izvadīt doto sarakstu kā tekstu
# # Testēšana: concatenate_list_data([1, 5, 12, 2]) -------> 15122
# def concatenate_list_data(list):
#     result= ''
#     for element in list:
#         result += str(element)
#     return result

# print(concatenate_list_data([1,5,12,2]))

# # 13
# # Dota programma, kuras uzdevums ir izvadīt doto sarakstu atšķirīgos elemenentus
# # Testēšana: -----> Oriģinālie saraksti:

# # {'Sarkans', 'Balts', 'Melns'}
# # {'Zaļš', 'Sarkans'}
# # Atšķirība starp krasu_saraksts_1 un krasu_saraksts_2:
# # {'Balts', 'Melns'}
# # Atšķirība starp krasu_saraksts_2 un krasu_saraksts_1:
# # {'Zaļš'}

# krasu_saraksts_1 = set(["Balts", "Melns", "Sarkans"])
# krasu_saraksts_2 = set(["Sarkans", "Zaļš"])
# print("Oriģinālie saraksti:")
# print(krasu_saraksts_1)
# print(krasu_saraksts_2)
# print("\nAtšķirība starp krasu_saraksts_1 un krasu_saraksts_2:")
# print(krasu_saraksts_1.difference(krasu_saraksts_2))
# print("\nAtšķirība starp krasu_saraksts_2 un krasu_saraksts_1:")
# print(krasu_saraksts_2.difference((krasu_saraksts_1)))