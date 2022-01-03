from Link import *
from Node import *
import random
import numpy as np
class Topo(object):#定义拓扑
    def __init__(self):
        self.node=[]
        self.edge=[]
        self.topo=[]

    def CreatTopo(self,node_edge_set):#输出邻接矩阵
        self.node=node_edge_set[0][0]
        self.edge=node_edge_set[1]
        #初始化拓扑,拓扑包含邻接表以及节点安全概率
        self.topo=[[],node_edge_set[0][1]]
        for i in range(len(self.node)):#初始化邻接表
            t=[]
            for j in range(len(self.node)):
                t.append(Link())
            self.topo[0].append(t)
        
        #节点与数字映射
        i=0
        dictnode={}
        for node in self.node:
            dictnode[node]=i
            i+=1
        
        
        for edge in self.edge:
            self.topo[0][dictnode.get(edge.fr)][dictnode.get(edge.to)]=Link(dictnode.get(edge.fr),dictnode.get(edge.to),edge.c)
            
        return self.topo
    def CreatNodeEdgeSet(self,basic_node_edge_set,c=1000,TrustednodeNum=4,option=0 ):#option=0默认为单向边
        newedge=[] #存储Link结构的边
        newnode=[] #存储节点以及节点安全概率
        
        #随机生成可信节点
        TrustedNode=[]
        while len(TrustedNode)<TrustednodeNum:
            t=random.randint(0,len(basic_node_edge_set[0])-1)
            if t not in TrustedNode:
                TrustedNode.append(t)

        NodeSecurityProbability=[] #节点安全概率
        for i in range(len(basic_node_edge_set[0])):
            if i not in TrustedNode:
                NodeSecurityProbability.append(0.9)
            else:
                NodeSecurityProbability.append(1)

        newnode=[basic_node_edge_set[0],NodeSecurityProbability]
            
        for edge in basic_node_edge_set[1]:
            if option==1:
                newedge.append(Link(edge[0],edge[1],c))
            else:
                newedge.append(Link(edge[0],edge[1],c))
                newedge.append(Link(edge[1],edge[0],c))
        return [newnode,newedge]

    def TopoUpdate(self,g,path):#删去路径上的不可信节点及路径
        nodelist=path[1:-1]
        for i in range(len(g[0])):
            for j in range(len(g[0][i])):
                if i in  nodelist or j in nodelist:
                    if g[1][j]<1 and g[0][i][j].Is_connected==True:
                        g[0][i][j].dellink()
        
        

    def Toporeduce(self,g):#将邻接矩阵化为邻接表
        tmptopo=[]
        for i in g[0]:
            t=[]
            for j in range(len(i)):
                if i[j].fr != None:
                    t.append([i[j].to,g[1][j]])
            tmptopo.append(t)
        return [tmptopo,g[1]]

    def Toporeducehop(self,g):#将邻接矩阵化为hop邻接表
        tmptopo=[]
        for i in g[0]:
            t=[]
            for j in range(len(i)):
                if i[j].fr != None:
                    t.append([i[j].to,1])
            tmptopo.append(t)
        return [tmptopo,g[1]]



