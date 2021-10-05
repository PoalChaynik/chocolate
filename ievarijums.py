'''
Aleksis Pocs
05.10.2021
'''

recepte = {'cukurs':0.6,'kanelis':0.008,'aboli':2.0,'udens':0.2}
cenas = {'cukurs':0.75,'kanelis':0.3,'aboli':0.0,'udens':0.0}

def izmaksa():
    cs = recepte['cukurs'] * cenas['cukurs']
    ck = (recepte['kanelis']) * (cenas['kanelis'])
    print('Summa =',cs+ck)

izmaksa()

