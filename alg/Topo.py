from alg.Link import *
class Topo(object):#定义拓扑
    def __init__(self):
        self.node=[]
        self.edge=[]
        self.topo=[]

    def CreatTopo(self,node_edge_set):#输出邻接矩阵
        self.node=node_edge_set[0]
        self.edge=node_edge_set[1]
        for i in range(len(self.node)):#初始化邻接矩阵
            self.topo.append([])
        i=0
        dictnode={}
        for node in self.node:
            dictnode[node]=i
            i+=1
        for edge in self.edge:
            self.topo[dictnode.get(edge.fr)].append(edge)
        return self.topo
    def CreatNodeEdgeSet(self,basic_node_edge_set,c=1000,TrustednodeNum=4,option=1"""默认为单向边"""):
        newedge=[] #里面存Link结构的边
        i=0
        dictnode={}
        for node in self.node:
            dictnode[node]=i
            i+=1
        for edge in basic_node_edge_set[1]:
            if option=1:
                newedge.append(Link(edge[0],edge[1],c))






