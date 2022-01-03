from Alg1 import *

class Alg2:
    def __init__(self):
        self.path=[] #储存找到的路径
        self.sp=[] #储存路径安全概率
        self.fsp=0 #最终安全概率
        self.finalpath=[]

    def alg2(self,topo,source,des,sth):#找到满足安全概率阈值的路径
        #先调用alg1找出普通多路径的数量
        path,pathsp,fsp=Alg1().alg1(topo,source,des,sth)
        #如果alg1能够满足那么确定路径数量
        if fsp>=sth:
            path_num=len(path)
            sumlen=1000000
            #找出最近的可信点
            for i in range(len(topo[0])):
                if topo[1][i]==1 and i!=source and i!=des:#是可信节点
                    path1=Dijkstra().hopdijkstra(topo,source,i)
                    if path1!=[]:
                        len1=len(path1)-1
                    path2=Dijkstra().hopdijkstra(topo,i,des)
                    if path1!=[]:
                        len2=len(path1)-1

                    if len1+len2<sumlen:
                        sumlen=len1+len2
                        relaynode=i
            #判断是否分段
            segpath1,segsp1,segfsp1=Alg1().alg1n(topo,source,i,path_num)
            segpath2,segsp2,segfsp2=Alg1().alg1n(topo,i,des,path_num)
            if len(segpath1)==path_num and len(segpath2)==path_num and segfsp1*segfsp2>fsp:
                self.finalpath.append(segpath1)



        

