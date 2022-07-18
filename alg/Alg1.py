#多路径算法
from Dijkstra import *
from Sp import *
from Topo import *

class Alg1:
    def __init__(self):
        self.path=[] #储存找到的路径
        self.sp=[] #储存路径安全概率
        self.fsp=0 #最终安全概率

    def alg1(self,topo,source,des,sth):#找到满足安全概率阈值的路径
        
        g=topo
        
        cur_sp=0
        while cur_sp<sth:
            #转为邻接表
            topotable=Topo().Toporeduce(g)
            path,path_sp=Dijkstra().dijkstra(topotable,source,des)#返回找到的路径和安全概率
            if path==[]: #意味着没有足够的路径来保证安全概率
                return [[[],[],0]] #拒绝服务返回0
            else:
                self.path.append(path)
                self.sp.append(path_sp)
            cur_sp=Sp().CalSumSecurityProbability(cur_sp,path_sp)
            self.fsp=cur_sp
            #移除拓扑上的边
            Topo().TopoUpdate(g,path)
            if cur_sp==1:
                return [[self.path,self.sp,self.fsp]]
        return [[self.path,self.sp,self.fsp]]

    def alg1n(self,topo,source,des,n):#找出n条路径
        g=topo
        cur_sp=0
        cur_path=0
        while cur_path<n:
            #转为邻接表
            topotable=Topo().Toporeduce(g)
            path,path_sp=Dijkstra().dijkstra(topotable,source,des)#返回找到的路径和安全概率
            if path==[]: #意味着没有足够的路径来保证安全概率
                return [[[],[],0]] #拒绝服务返回0
            else:
                
                self.path.append(path)
                cur_path=len(self.path)
                self.sp.append(path_sp)

            cur_sp=Sp().CalSumSecurityProbability(cur_sp,path_sp)
            self.fsp=cur_sp

            #移除拓扑上的边
            Topo().TopoUpdate(g,path)
            if cur_sp==1:
                return [[self.path,self.sp,self.fsp]]
        return [[self.path,self.sp,self.fsp]]

    def alg1maxs(self,topo,source,des,sth=2):#找到最大安全性的路径
        
        g=topo
        
        cur_sp=0
        while cur_sp<sth:
            #转为邻接表
            topotable=Topo().Toporeduce(g)
            path,path_sp=Dijkstra().dijkstra(topotable,source,des)#返回找到的路径和安全概率
            if path==[]: #意味着没有足够的路径来保证安全概率
                break #找不到多余路径，返回当前找出的路径
            else:
                self.path.append(path)
                self.sp.append(path_sp)
            cur_sp=Sp().CalSumSecurityProbability(cur_sp,path_sp)
            self.fsp=cur_sp
            #移除拓扑上的边
            Topo().TopoUpdate(g,path)
            if cur_sp==1:
                return [[self.path,self.sp,self.fsp]]
        return [[self.path,self.sp,self.fsp]]
    def alg1maxn(self,topo,source,des,n):#找出n条路径
        g=topo
        cur_sp=0
        cur_path=0
        while cur_path<n:
            #转为邻接表
            topotable=Topo().Toporeduce(g)
            path,path_sp=Dijkstra().dijkstra(topotable,source,des)#返回找到的路径和安全概率
            if path==[]: #意味着没有足够的路径来保证安全概率
                return [[self.path,self.sp,self.fsp]] #返回已找到的路径
            else:
                
                self.path.append(path)
                cur_path=len(self.path)
                self.sp.append(path_sp)

            cur_sp=Sp().CalSumSecurityProbability(cur_sp,path_sp)
            self.fsp=cur_sp

            #移除拓扑上的边
            Topo().TopoUpdate(g,path)
            
        return [[self.path,self.sp,self.fsp]]