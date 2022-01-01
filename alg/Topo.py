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
        self.node=node_edge_set[0]
        self.edge=node_edge_set[1]
        for i in range(len(self.node)):#初始化邻接矩阵
            self.topo.append([])
        '''
            i=0
            dictnode={}
            for node in self.node:
                dictnode[node]=i
                i+=1
        '''
        
        for edge in self.edge:
            for node in self.node:
                if node.name==edge.fr:
                    self.topo[node.index].append(edge)
                    break
            
        return self.topo
    def CreatNodeEdgeSet(self,basic_node_edge_set,c=1000,TrustednodeNum=4,option=1 ):#option=1默认为单向边
        newedge=[] #存储Link结构的边
        newnode=[] #存储Node结构的节点
        
        #随机生成可信节点位置
        TrustedNode=[]
        while len(TrustedNode)<TrustednodeNum:
            t=random.randint(0,len(basic_node_edge_set)-1)
            if t not in TrustedNode:
                TrustedNode.append(t)
        NodeSecurityProbability=[] #节点安全概率
        for i in range(len(basic_node_edge_set[0])):
            if i not in TrustedNode:
                NodeSecurityProbability.append(0.9)
            else:
                NodeSecurityProbability.append(1)

        for i in range(len(basic_node_edge_set[0])):
            newnode.append(Node(basic_node_edge_set[0][i],i,NodeSecurityProbability[i]))
            
        for edge in basic_node_edge_set[1]:
            if option==1:
                newedge.append(Link(edge[0],edge[1],c))
            else:
                newedge.append(Link(edge[0],edge[1],c))
                newedge.append(Link(edge[1],edge[0],c))
        return [newnode,newedge]






