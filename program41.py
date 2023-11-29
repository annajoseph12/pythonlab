import csv
with open("csv4.csv",newline='')as csvfile:
    d=csv.DictReader(csvfile)
    print("STUDENT NAME ROLL NO MARK")
    print("................")
    for i in d:
        print(i['student name'],i['roll no'],i['mark'])