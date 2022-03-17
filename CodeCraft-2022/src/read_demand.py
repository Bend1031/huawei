import csv
import numpy as np

with open('data\demand.csv', 'r', encoding="utf-8") as f:
    # reader = csv.DictReader(f)
    reader = csv.reader(f, delimiter=",")
    # demand=np.array([[]])
    demands = []
    for row in reader:
        if reader.line_num == 1:
            mtime = row.pop(0)
            M = row
            i=len(M)
            # print(M)
        else:

            demands.append(row)
        # print(row[1])
    T = []
    D = []
    for demand in demands:
        T.append(demand[0])
        d = demand[1:]
        d = list(map(int, d))
        D.append(d)
    # D = map(int, D)
    t=len(T)
    D=np.array(D)
    print()

