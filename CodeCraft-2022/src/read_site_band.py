import csv

with open('data\site_bandwidth.csv', 'r', encoding="utf-8") as f:
    reader = csv.reader(f, delimiter=",")
    C = {}
    for item in reader:

        if reader.line_num == 1:
            pass

        else:
            C[item[0]] = item[1]
