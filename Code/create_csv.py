import csv
datas = [['A00001', 'N'],
         ['A00002','N'],
         ['A00003', 'N']]

with open('example.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    for row in datas:
        writer.writerow(row)