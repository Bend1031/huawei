import csv
import numpy as np
import os
import configparser

base_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))
# base_path=""
config = configparser.ConfigParser()
config.read(base_path+"/data/config.ini")

Q = config.getint('config', 'qos_constraint')

with open(base_path+'/data/demand_copy.csv', 'r', encoding="utf-8") as f:

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


with open(base_path+'/data/site_bandwidth.csv', 'r', encoding="utf-8") as f:
    reader = csv.reader(f, delimiter=",")
    C = {}
    for item in reader:

        if reader.line_num == 1:
            pass

        else:
            C[item[0]] = item[1]

with open(base_path+'/data/qos.csv', 'r', encoding="utf-8") as f:
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


# 根据 qos 值确定客户节点能够连接的边缘节点与连接数
num_of_connects = []
N_avi_connect = []  # 可供连接的节点
connect = {}  # 每个客户节点能够连接的边缘节点
for i in range(Y.shape[1]):
    a = Y[..., i]
    index = np.argwhere(a < Q).tolist()
    index = sum(index, [])
    N_avi_connect = [N[j] for j in index]
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
        if self.cap < value:
            raise ValueError("带宽用尽！")
        self.cap -= value
        self.record.append(value)


if os.path.exists("./output"):
    pass
else:
    os.makedirs(r"./output")
with open(base_path+"/output/solution.txt", "w") as f:
    for t_i in range(t):

        # 初始化边缘节点
        edge_dict = {}
        for name, band_width in C.items():
            edge_dict[name] = Edge_node(name, int(band_width))

        demand_t_i = D[t_i, ...]
        demand_t_i_sort = [demand_t_i[i] for i in sort_index]

        # 对每个客户节点进行流量分配
        for m in range(len(M_sort)):
            # 该客户连接的边缘节点
            edge_sort = connect[M_sort[m]]
            # 对每个节点计算权重
            cap_sum = 0
            weight_list = []
            for i in edge_sort:
                cap_sum += edge_dict[i].cap
            for i in edge_sort:
                weight_list.append(edge_dict[i].cap/cap_sum)
            need_list = [demand_t_i_sort[m] * i for i in weight_list]

            # 取整数
            need_list_int = list(map(int, need_list))
            need_list_int[-1] = need_list_int[-1] + \
                demand_t_i_sort[m]-sum(need_list_int)

            # 对边缘节点分配流量
            log_list = []
            for i in range(len(edge_sort)):
                edge_dict[edge_sort[i]].need = need_list_int[i]
                log_list.append((edge_sort[i], need_list_int[i]))

        # 当前时刻流量分配完毕
        # 输出流量分配方案 M 行
            print(M_sort[m]+":", end="", file=f)
            for log in log_list:
                end_str = "<"+log[0]+","+str(log[1])+">"
                if log[1] == 0:
                    print(file=f)
                    break
                if log == log_list[-1]:
                    if t_i == t-1 and m == len(M_sort)-1:
                        print(end_str, end="", file=f)
                    else:
                        print(end_str, file=f)
                else:
                    print(end_str, end="", file=f)
