import csv
import numpy as np
from read_config import *


with open('data\demand.csv', 'r', encoding="utf-8") as f:

    # reader = csv.DictReader(f)
    reader = csv.reader(f, delimiter=",")
    # demand=np.array([[]])
    demands = []
    for row in reader:
        if reader.line_num == 1:
            mtime = row.pop(0)
            M = row
            i = len(M)
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
    t = len(T)
    D = np.array(D)
    print()

with open('data\site_bandwidth.csv', 'r', encoding="utf-8") as f:
    reader = csv.reader(f, delimiter=",")
    C = {}
    for item in reader:

        if reader.line_num == 1:
            pass

        else:
            C[item[0]] = item[1]

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
    N = []  # 边缘节点
    Y = []  # qos值矩阵
    for item in qos:
        N.append(item[0])
        y = item[1:]
        y = list(map(int, y))
        Y.append(y)
    # D = map(int, D)
    j = len(N)
    Y = np.array(Y)



##根据 qos 值确定客户节点能够连接的边缘节点与连接数
num_of_connects = []
N_avi_connect=[]#可供连接的节点
connect={} #每个客户节点能够连接的边缘节点
for i in range(Y.shape[1]):
    a = Y[..., i]
    index = np.argwhere(a < Q).tolist()
    index=sum(index,[])
    N_avi_connect=[N[j] for j in index]
    num_of_connects.append(len(index))
    connect[M_qos[i]] = N_avi_connect


sort_index = np.argsort(num_of_connects)  # 从小到大的索引
M_sort = [M[i] for i in sort_index]  # 分配顺序


class Edge_node:
    """边缘节点
    """

    def __init__(self, name, cap):
        self.name = name
        self.cap = cap
        self._need = 0
        self.record = []

    @property
    def need(self):
        return self._need

    @need.setter
    def need(self, value):
        self._need = value
        self.cap -= value
        self.record.append(value)

# 初始化边缘节点
edge_dict={}
for name,band_width in C.items():
    Edge = Edge_node(name, int(band_width)) 
    edge_dict[name]=Edge

print()
for t_i in range(t):
    num_of_connects = []
    link_index=[]
    demand_t_i = D[t_i, ...]
    for i in range(Y.shape[1]):
        a = Y[..., i]
        index = np.argwhere(a < Q)
        link_index.append(index)
        num_of_connects.append(len(index))
        print()
    sort_index = np.argsort(num_of_connects) # 从小到大的索引
    M_sort=[M[i] for i in sort_index] # 分配顺序

    print()
