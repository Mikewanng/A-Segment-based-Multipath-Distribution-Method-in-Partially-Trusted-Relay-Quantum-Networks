from Sp import *
import math,sys
class Seclev:#计算安全等级表，得到最终密钥量
    def __init__(self):
        pass

    def sl(self,pathsecurityset,sth):#计算满足sth的最大密钥量
        slt=[[],[]] #初始化表
        #按照最低的安全概率计算
        tmpsp=0
        for i in range(len(pathsecurityset)):
            tmpsp=Sp().CalSumSecurityProbability(tmpsp,pathsecurityset[-i-1])
            slt[0].append(tmpsp)
            slt[1].append(len(pathsecurityset)//(i+1))
        #查表
        for i in range(len(slt[0])):
            if slt[0][i]>=sth:
                return slt[1][i]
        return 1

    def segsl(self,pathsecuritysetset,sth):#计算不同分段中的满足sth的最大密钥量
        tmpnum=[]
        min=sys.maxsize
        for i in pathsecuritysetset:
            tmpn=self.sl(i[1],sth**(1/len(pathsecuritysetset)))
            tmpnum.append(tmpn)
            if tmpn<min:
                min=tmpn
        return min