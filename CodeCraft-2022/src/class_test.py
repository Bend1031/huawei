class Edge_node:
    """边缘节点
    """

    def __init__(self, name, cap):
        self.name = name
        self.cap = cap
        self._need=0
        self.record=[]

    @property
    def need(self):
        return self._need

    @need.setter
    def need(self, value):
        self._need = value
        self.cap -= value
        self.record.append(value)


A = Edge_node("A", 2000)
A.need=200
A.need=300

