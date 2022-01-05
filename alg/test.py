from Topo import *
from Net import *
from Alg1 import *
from RandomRouting import *
from Alg2 import *
import copy,random,time
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
count=100
g=Net().network
g1=Topo().CreatNodeEdgeSet(g,10,4,0)
g2=Topo().CreatTopo(g1)
source=random.randint(0,len(g2[0])-1)
des=random.randint(0,len(g2[0])-1)
while des==source:
    des=random.randint(0,len(g2[0])-1)
sth=np.arange(0.5,1,0.1)
sp1=[0]*len(sth)
sp2=[0]*len(sth)
spr=[0]*len(sth)
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
        for p in t1:
            sp1[j]+=p[2]
        t2=Alg2().alg2(copy.deepcopy(g2),source,des,sth[j])
        print(t2)
        for p in t2:
            sp2[j]+=p[2]
        tr=Rr().rr(copy.deepcopy(g2),source,des,sth[j])
        print(tr)
        for p in tr:
            spr[j]+=p[2]
for j in range(len(sp1)):
    sp1[j]/=count
    sp2[j]/=count
    spr[j]/=count
fig = plt.figure()
plt.plot(sth,sp1,color='red')
plt.plot(sth,sp2,color='green')
plt.plot(sth,spr,color='black')
plt.title("")
plt.xlabel('sth')
plt.ylabel('sp')
plt.show()