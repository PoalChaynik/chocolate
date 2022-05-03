def ievade():
    while True:
        time = (input('Ievadiet Laiku (24H Formātā/BEZ MINŪTĒM): '))
        if time.isdigit() and int(time) <= 24: 
            time = int(time)
            if time >= 0 and time <6:
                print('Ar labu nakti!')
                break
            elif time >=6 and time <12:
                print('Labrīt!')
                break
            elif time >= 12 and time <18:
                print('Labdien!')
                break
            elif time >= 18 and time <=24:
                print('Labvakar!')
                break
        else:
            continue


ievade()