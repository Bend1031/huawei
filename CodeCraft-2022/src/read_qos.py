import csv
import numpy as np

with open('data\qos.csv', 'r', encoding="utf-8") as f:
    # reader = csv.DictReader(f)
    reader = csv.reader(f, delimiter=",")
    # item=np.array([[]])
    qos = []
    for row in reader:
        if reader.line_num == 1:
            mtime = row.pop(0)
            M_qos = row
            i = len(M_qos)
            # print(M_qos)
        else:

            qos.append(row)
        # print(row[1])
    N = [] #边缘节点
    Y = [] #qos值矩阵
    for item in qos:
        N.append(item[0])
        y = item[1:]
        y = list(map(int, y))
        Y.append(y)
    # D = map(int, D)
    j = len(N)
    Y = np.array(Y)
    print()
