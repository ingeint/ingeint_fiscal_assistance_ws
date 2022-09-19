from dbfread import DBF

table = DBF('C:\PRINTSPOOL\DATOS3.DBF', load=True)
records = table.records
loop = len(records) - 1
while loop > 0:
    if records[loop]['REFINT'] == '1449':
        print(records[loop]['NUMDOC'])
        break
    loop -= 1
    print(loop)
