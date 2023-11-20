import csv
with open("csv3.csv",newline='')as csvfile:
    d=csv.reader(csvfile)
    for i in d:
        print(','.join(i))
