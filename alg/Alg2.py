from Alg1 import *
import copy,sys
class Alg2:
    def __init__(self):
        self.path=[] #储存找到的路径
        self.sp=[] #储存路径安全概率
        self.fsp=0 #最终安全概率
        self.finalpath=[]

    def alg2(self,topo,source,des,sth):#找到满足安全概率阈值的路径
        #先调用alg1找出普通多路径的数量
        tmp=Alg1().alg1(copy.deepcopy(topo),source,des,sth)
        fsp=tmp[0][2]
        #如果alg1能够满足那么确定路径数量
        if fsp>=sth:
            path_num=len(tmp[0][0])
            if path_num==1:#不需要分段
                return tmp
            return self.alg2n(copy.deepcopy(topo),source,des,path_num)
            
        else:#算法1不能满足，那么依次递增路径数量直到满足sth
            for n in range(1,100):
                t=self.alg2n(copy.deepcopy(topo),source,des,n)
                #判断返回路径是否为空
                for i in t:
                    if i[0]==[]:#无法找到足够路径数量
                        return [[[],[],0]]
                #判断能否满足安全性需求
                sp=Sp().segsp(t)
                if sp>=sth:
                    """
                    #重组格式
                    t0=[]
                    t1=[]
                    t2=[]
                    for i in t:
                        t0.append(i[0])
                        t1.append(i[1])
                        t2.append(i[2])"""
                    return t
                    
    def alg2n(self,topo,source,des,n):#找出n条路径并返回
        sumlen=1000000
        #找出最近的可信点且距离起点更近
        relaynode=sys.maxsize
        topotable=Topo().Toporeducehop(topo)
        for i in range(len(topo[0])):
            if topo[1][i]==1 and i!=source and i!=des:#是可信节点
                path1=Dijkstra().hopdijkstra(topotable,source,i)
                if path1!=[]:
                    len1=len(path1)-1
                else:
                    continue
                path2=Dijkstra().hopdijkstra(topotable,i,des)
                if path1!=[]:
                    len2=len(path2)-1
                else:
                    continue

                if len1+len2<sumlen:
                    sumlen=len1+len2
                    relaynode=i

        #判断是否分段
        if relaynode==sys.maxsize:
            return Alg1().alg1n(copy.deepcopy(topo),source,des,n)
        t=Alg1().alg1n(copy.deepcopy(topo),source,des,n)
        t1=Alg1().alg1n(topo,source,relaynode,n)
        tmptopo=copy.deepcopy(topo)
        t2=Alg1().alg1n(topo,relaynode,des,n)

        if len(t1[0][0])==n and len(t2[0][0])==n and t1[0][2]*t2[0][2]>t[0][2]:
                return t1+self.alg2n(tmptopo,relaynode,des,n)
        
        else:
            return t
        

