import csv

with open(r'C:\Users\Windows\Desktop\2018Win\Heart Project\code\REFERENCE.csv') as f:
    reader = csv.reader(f)
    print(list(reader))