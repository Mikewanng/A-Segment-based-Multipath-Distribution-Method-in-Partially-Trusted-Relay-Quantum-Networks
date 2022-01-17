from Topo import *
from Net import *
from Alg1 import *
from RandomRouting import *
from Alg2 import *
import copy,random,time
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
count=1000
g=Net().network
g1=Topo().CreatNodeEdgeSet(g,10,6,0)
g2=Topo().CreatTopo(g1)
source=random.randint(0,len(g2[0])-1)
des=random.randint(0,len(g2[0])-1)
while des==source:
    des=random.randint(0,len(g2[0])-1)
sth=np.arange(0.5,1,0.1)
filename='Sp_vs_sth'+str(count)+'time='+str(time.time())+'.txt'
fp = open(filename, 'w')
fp.write('sth    avesecurityprobability1    ressecurityprobability    respond_rate    avekeyconsume    requestkeyconsume    avesecurityprobability2    ressecurityprobability    respond_rate    avekeyconsume    requestkeyconsume    avesecurityprobabilityr    ressecurityprobability    respond_rate    avekeyconsume    requestkeyconsume\n')
#平均安全概率
sp1=[0]*len(sth)
sp2=[0]*len(sth)
spr=[0]*len(sth)
#响应安全概率
sp1r=[0]*len(sth)
sp2r=[0]*len(sth)
sprr=[0]*len(sth)
#响应统计数
count1=[0]*len(sth)
count2=[0]*len(sth)
countr=[0]*len(sth)
#响应率
respondrate1=[0]*len(sth)
respondrate2=[0]*len(sth)
respondrater=[0]*len(sth)

#平均总消耗
cost1=[0]*len(sth)
cost2=[0]*len(sth)
costr=[0]*len(sth)
#响应平均消耗
cost1r=[0]*len(sth)
cost2r=[0]*len(sth)
costrr=[0]*len(sth)

for i in range(count):
    print('count=',i)
    source=random.randint(0,len(g2[0])-1)
    des=random.randint(0,len(g2[0])-1)
    print('source=',source,'des=',des)
    while des==source:
        des=random.randint(0,len(g2[0])-1)
    for j in range(len(sth)):
        print(sth[j])
        t1=Alg1().alg1(copy.deepcopy(g2),source,des,sth[j])
        print(t1)
        if t1[0][2]>0:
            count1[j]+=1
            sp1[j]+=t1[0][2]
        for z in t1:
            for path in z[0]:
                cost1[j]+=len(path)-1
        t2=Alg2().alg2(copy.deepcopy(g2),source,des,sth[j])
        print(t2)
        for z in t2:
            for path in z[0]:
                cost2[j]+=len(path)-1
        tmp=1
        for p in t2:
            tmp*=p[2]
        if t2[0][2]==0:
            tmp=0
        if tmp>0:
            count2[j]+=1
            sp2[j]+=tmp
        tr=Rr().rr(copy.deepcopy(g2),source,des,sth[j])
        print(tr)
        if tr[0][2]>0:
            countr[j]+=1
            spr[j]+=tr[0][2]
        for z in tr:
            for path in z[0]:
                costr[j]+=len(path)-1
for j in range(len(sp1)):#响应
    sp1r[j]=sp1[j]/count1[j]
    sp2r[j]=sp2[j]/count2[j]
    sprr[j]=spr[j]/countr[j]
    cost1r[j]=cost1[j]/count1[j]
    cost2r[j]=cost2[j]/count2[j]
    costrr[j]=costr[j]/countr[j]

for j in range(len(sp1)):#平均
    sp1[j]/=count
    sp2[j]/=count
    spr[j]/=count
    respondrate1=count1[j]/count
    respondrate2=count2[j]/count
    respondrater=countr[j]/count
    cost1[j]/=count
    cost2[j]/=count
    costr[j]/=count


for j in range(len(sth)):
    fp.write(str(sth[j])+'    '+str(sp1[j])+'    '+str(sp1r[j])+'    '+str(respondrate1[j])+'    '+str(cost1r[j])+'    '+str(cost1[j])+'    '+str(sp2[j])+'    '+str(sp2r[j])+'    '+str(respondrate2[j])+'    '+str(cost2r[j])+'    '+str(cost2[j])+'    '+str(spr[j])+'    '+str(sprr[j])+'    '+str(respondrater[j])+'    '+str(costrr[j])+'    '+str(costr[j])+'\n')

fig = plt.figure()
plt.plot(sth,sp1,color='red')
plt.plot(sth,sp2,color='green')
plt.plot(sth,spr,color='black')
plt.title("average Security probability")
plt.xlabel('sth')
plt.ylabel('Security probability')
plt.show()

fig = plt.figure()
plt.plot(sth,sp1r,color='red')
plt.plot(sth,sp2r,color='green')
plt.plot(sth,sprr,color='black')
plt.title("res Security probability")
plt.xlabel('sth')
plt.ylabel('Security probability')
plt.show()

fig = plt.figure()
plt.plot(sth,count1,color='red')
plt.plot(sth,count2,color='green')
plt.plot(sth,countr,color='black')
plt.title("request Response rate  ")
plt.xlabel('sth')
plt.ylabel('Response rate')
plt.show()

fig = plt.figure()
plt.plot(sth,cost1,color='red')
plt.plot(sth,cost2,color='green')
plt.plot(sth,costr,color='black')
plt.title("ave key consume")
plt.xlabel('sth')
plt.ylabel('consume')
plt.show()


fig = plt.figure()
plt.plot(sth,cost1r,color='red')
plt.plot(sth,cost2r,color='green')
plt.plot(sth,costrr,color='black')
plt.title("res key consume")
plt.xlabel('sth')
plt.ylabel('consume')
plt.show()