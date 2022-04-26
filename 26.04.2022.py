# #Bez kludas
# try:
#     f = open('testfile','w')
#     f.write('Test write this')
# except IOError:
#     print('Error: Could not find file or read data')
# else:
#     print('Success!')
#     f.close()

# #Ieviesta Kluda
# try:
#     f = open('testfile1','r') #testfile1 jo testfile fails jau eksiste
#     f.write('Write')
# except IOError:
#     print('Error: Could not find file or read data')
# else:
#     print('Success: No Errors')
#     f.close()
# finally:
#     print('Un vini dzivoja ilgi un laimigi')


def askint():
    step = 0
    while True:
        try:
            step +=1 
            val = int(input('Ievadi Skaitli: '))
        except:
            print('Ievadiet SKAITLI!')
            continue
        else:
            if step >= 2:
                print('BEIDZOT!',f'Jums Vajadzeja {step} Meginajumus Lai Ierakstit Skaitli!')
            print(val)
            break
        finally:
            print('Execution')


askint()