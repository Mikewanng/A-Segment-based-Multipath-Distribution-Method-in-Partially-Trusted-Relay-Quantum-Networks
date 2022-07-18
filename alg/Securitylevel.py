from Sp import *
import math,sys
from queue import PriorityQueue

class Seclev:#计算安全等级表，得到最终密钥量
    def __init__(self):
        pass
#  [[[[5, 6], [5, 7, 6], [5, 37, 3, 4, 11, 6]], [1, 0.95, 0.18549375000000012], 1.0], [[[6, 31, 16, 20, 25, 26], [6, 8, 10, 15, 13, 29, 17, 18, 26]], [0.8145062499999999, 0.7350918906249998], 0.950861201386621]]


    def sl(self,pathsecurityset,sth):#输入路径集合及路径安全概率计算满足sth的最大密钥量

        maxpath=100000
        overpath=[]
        #首先找出每一段路径的最小路径数量
        for i in range(len(pathsecurityset)):
            if len(pathsecurityset[i][0])<maxpath:
                maxpath=len(pathsecurityset[i][0])
                overpath.append(i)
        #将大于此路径数量的段进行安全性提升
        for i in overpath:
            for j in range(len(pathsecurityset[i][0])-maxpath):
                up_sec_level(pathsecurityset[i])
        #然后进行段间匹配判断当前最小的安全性能否满足sth，满足则输出，否则继续提升每一段的安全等级


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

    def up_sec_level(self,pathsecurityset):
        pass

    def seclev(self,pathsecurityset):#计算安全等级表
        q=PriorityQueue()
        slt=[] #初始化表,表项为：索引作安全等级，安全等级对应的路径安全概率
        #将路径安全概率放入队列
        pathnum=len(pathsecurityset[0])
        for i in range(pathnum):
            q.put([pathsecurityset[1][i],[pathsecurityset[0][i]]]) #将路径及安全概率放入优先队列，根据安全概率将从低到高。
        tmp1=[]
        tmp2=[]
        for i in q.queue:
            tmp1.append(i[0])
            tmp2.append(i[1])
        slt.append([tmp1,tmp2])
        for i in range(pathnum-1):
            tmp_1=q.get()
            cur_sp=tmp_1[0]
            if not q.empty():
                tmp_2=q.get()
                new_sp=Sp().CalSumSecurityProbability(cur_sp,tmp_2[0])
                q.put([new_sp,tmp_1[1]+tmp_2[1]])
            tmp1=[]
            tmp2=[]
            for i in q.queue:
                tmp1.append(i[0])
                tmp2.append(i[1])
            slt.append([tmp1,tmp2])
        slt.reverse()
        return slt
