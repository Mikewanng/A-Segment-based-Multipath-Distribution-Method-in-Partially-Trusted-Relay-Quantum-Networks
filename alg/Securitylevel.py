from Sp import *
import math,sys
from queue import PriorityQueue

class Seclev:#计算安全等级表，得到最终密钥量
    def __init__(self):
        pass

    def sl(self,pathsecurityset,sth):#计算满足sth的最大密钥量
        slt=[[],[]] #初始化表
        q=PriorityQueue()
        #将路径安全概率放入队列
        for i in pathsecurityset[1]:
            q.put(i)
        #计算安全登记表
        for i in range(len(pathsecurityset[1])):
            tsp=q.get()
            slt[0].append(tsp)
            slt[1].append(len(pathsecurityset[1])-i)
            if not q.empty():
                tsp2=q.get()
                nsp=Sp().CalSumSecurityProbability(tsp,tsp2)
                q.put(nsp)
        
        #查表
        t=0
        for i in range(len(slt[0])):
            if slt[0][i]>=sth:
                t=slt[1][i]
                break
        return t

    def segsl(self,pathsecuritysetset,sth):#计算不同分段中的满足sth的最大密钥量
        tmpnum=[]
        min=sys.maxsize
        for i in pathsecuritysetset:
            tmpn=self.sl(i,sth**(1/len(pathsecuritysetset)))
            tmpnum.append(tmpn)
            if tmpn<min:
                min=tmpn
        return min