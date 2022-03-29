import xlwt

wb = xlwt.Workbook()

lapa1 = wb.add_sheet('Lapa1')

#lapa1.write(rinda,kolonna,dati,stils)

lapa1.write(0,0,'Sveiki')
lapa1.write(1,0,'Labdien')
lapa1.write(2,0,'Labrit')
lapa1.write(3,0,'Labvakar')

# wb.save('meginajums.xls')

import xlsxwriter

fails = xlsxwriter.Workbook('meginajums2.xlsx')
lapa = fails.add_worksheet()

lapa.write('A1','Riga')
lapa.write('C2','London')

fails.close()



