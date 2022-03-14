from Topo import *
from Net import *
from Alg1 import *
from RandomRouting import *
from Alg2 import *
from Securitylevel import *
import copy,random,time
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

count=200

"""
g=Net().network
g1=Topo().CreatNodeEdgeSet(g,10,4,0)
g2=Topo().CreatTopo(g1)
source=random.randint(0,len(g2[0])-1)
des=random.randint(0,len(g2[0])-1)
while des==source:
    des=random.randint(0,len(g2[0])-1)
sth=np.arange(0.5,1,0.05)
filename='Sp_vs_sth'+str(count)+'time='+str(time.time())+'.txt'
fp = open(filename, 'w')
fp.write('sth    avesecurityprobability1    ressecurityprobability    respond_rate    avekeyconsume    reskeyconsume    keynum    time1    avesecurityprobability2    ressecurityprobability    respond_rate    avekeyconsume    requestkeyconsume    keynum2    time2    avesecurityprobabilityr    ressecurityprobability    respond_rate    avekeyconsume    requestkeyconsume    keynumr    timer\n')
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
#密钥数量
keynum1=[0]*len(sth)
keynum2=[0]*len(sth)
keynumr=[0]*len(sth)
#时间
time1=[0]*len(sth)
time2=[0]*len(sth)
timer=[0]*len(sth)
for i in range(count):
    print('count=',i)
    source=random.randint(0,len(g2[0])-1)
    des=random.randint(0,len(g2[0])-1)
    print('source=',source,'des=',des)
    while des==source:
        des=random.randint(0,len(g2[0])-1)
    for j in range(len(sth)):
        print(sth[j])
        ts1=time.time()
        t1=Alg1().alg1(copy.deepcopy(g2),source,des,sth[j])
        time1[j]+=time.time()-ts1
        print(t1)
        if t1[0][2]>0:
            count1[j]+=1
            sp1[j]+=t1[0][2]
            keynum1[j]+=1
        for z in t1:
            for path in z[0]:
                cost1[j]+=len(path)-1
        ts2=time.time()
        t2=Alg2().alg2(copy.deepcopy(g2),source,des,sth[j])
        time2[j]+=time.time()-ts2
        print(t2)
        #if t2!=t1:
            #print('*********************************************************************************************\n')
            #time.sleep(10)
        #去除分段的重复路径
        for z in t2:
            for path in z[0]:
                cost2[j]+=len(path)-1
        tmp=1
        for p in t2:
            tmp*=p[2]
        if t2[0][2]==0:
            tmp=0
        if tmp>0:
            keynum2[j]+=Seclev().segsl(t2,sth[j])
            count2[j]+=1
            sp2[j]+=tmp
        tsr=time.time()
        tr=Rr().rr(copy.deepcopy(g2),source,des,sth[j])
        timer[j]+=time.time()-tsr
        print(tr)
        if tr[0][2]>0:
            countr[j]+=1
            spr[j]+=tr[0][2]
            keynumr[j]+=1
        for z in tr:
            for path in z[0]:
                costr[j]+=len(path)-1
for j in range(len(sp1)):#响应
    if count1[j]>0:
        sp1r[j]=sp1[j]/count1[j]
        cost1r[j]=cost1[j]/count1[j]
    if count2[j]>0:
        sp2r[j]=sp2[j]/count2[j]
        cost2r[j]=cost2[j]/count2[j]

    if countr[j]>0:
        sprr[j]=spr[j]/countr[j]
        costrr[j]=costr[j]/countr[j]
    

for j in range(len(sp1)):#平均
    sp1[j]/=count
    sp2[j]/=count
    spr[j]/=count
    respondrate1[j]=count1[j]/count
    respondrate2[j]=count2[j]/count
    respondrater[j]=countr[j]/count
    cost1[j]/=count
    cost2[j]/=count
    costr[j]/=count
    keynum1[j]/=count
    keynum2[j]/=count
    keynumr[j]/=count
    time1[j]/=count
    time2[j]/=count
    timer[j]/=count


for j in range(len(sth)):
    fp.write(str(sth[j])+'    '+str(sp1[j])+'    '+str(sp1r[j])+'    '+str(respondrate1[j])+'    '+str(cost1[j])+'    '+str(cost1r[j])+'    '+str(keynum1[j])+'    '+str(time1[j])+'    '+str(sp2[j])+'    '+str(sp2r[j])+'    '+str(respondrate2[j])+'    '+str(cost2[j])+'    '+str(cost2r[j])+'    '+str(keynum2[j])+'    '+str(time2[j])+'    '+str(spr[j])+'    '+str(sprr[j])+'    '+str(respondrater[j])+'    '+str(costr[j])+'    '+str(costrr[j])+'    '+str(keynumr[j])+'    '+str(timer[j])+'\n')
fp.close()


g=Net().network
g1=Topo().CreatNodeEdgeSet(g,10,0,0)
g2=Topo().CreatTopo(g1)


trnum=np.arange(1,11,1)
sth=0.9
filename='Sp_vs_trnum'+str(count)+'time='+str(time.time())+'.txt'
fp = open(filename, 'w')
fp.write('trnum    avesecurityprobability1    ressecurityprobability    respond_rate    avekeyconsume    reskeyconsume    keynum    time1    avesecurityprobability2    ressecurityprobability    respond_rate    avekeyconsume    requestkeyconsume    keynum2    time2    avesecurityprobabilityr    ressecurityprobability    respond_rate    avekeyconsume    requestkeyconsume    keynumr    timer\n')
#平均安全概率
sp1=[0]*len(trnum)
sp2=[0]*len(trnum)
spr=[0]*len(trnum)
#响应安全概率
sp1r=[0]*len(trnum)
sp2r=[0]*len(trnum)
sprr=[0]*len(trnum)
#响应统计数
count1=[0]*len(trnum)
count2=[0]*len(trnum)
countr=[0]*len(trnum)
#响应率
respondrate1=[0]*len(trnum)
respondrate2=[0]*len(trnum)
respondrater=[0]*len(trnum)

#平均总消耗
cost1=[0]*len(trnum)
cost2=[0]*len(trnum)
costr=[0]*len(trnum)
#响应平均消耗
cost1r=[0]*len(trnum)
cost2r=[0]*len(trnum)
costrr=[0]*len(trnum)
#密钥数量
keynum1=[0]*len(trnum)
keynum2=[0]*len(trnum)
keynumr=[0]*len(trnum)
#时间
time1=[0]*len(trnum)
time2=[0]*len(trnum)
timer=[0]*len(trnum)
for i in range(count):
    print('count=',i)
    source=random.randint(0,len(g2[0])-1)
    des=random.randint(0,len(g2[0])-1)
    while des==source:
        des=random.randint(0,len(g2[0])-1)
    
    for j in range(len(trnum)):
        g=Net().network
        g1=Topo().CreatNodeEdgeSet(g,10,trnum[j],0)
        g2=Topo().CreatTopo(g1)
        print(trnum[j])
        ts1=time.time()
        t1=Alg1().alg1(copy.deepcopy(g2),source,des,sth)
        time1[j]+=time.time()-ts1
        print(t1)
        if t1[0][2]>0:
            count1[j]+=1
            sp1[j]+=t1[0][2]
            keynum1[j]+=1
        for z in t1:
            for path in z[0]:
                cost1[j]+=len(path)-1
        ts2=time.time()
        t2=Alg2().alg2(copy.deepcopy(g2),source,des,sth)
        time2[j]+=time.time()-ts2
        print(t2)
        #if t2!=t1:
            #print('*********************************************************************************************\n')
            #time.sleep(10)
        #去除分段的重复路径
        for z in t2:
            for path in z[0]:
                cost2[j]+=len(path)-1
        tmp=1
        for p in t2:
            tmp*=p[2]
        if t2[0][2]==0:
            tmp=0
        if tmp>0:
            keynum2[j]+=Seclev().segsl(t2,sth)
            count2[j]+=1
            sp2[j]+=tmp
        tsr=time.time()
        tr=Rr().rr(copy.deepcopy(g2),source,des,sth)
        timer[j]+=time.time()-tsr
        print(tr)
        if tr[0][2]>0:
            countr[j]+=1
            spr[j]+=tr[0][2]
            keynumr[j]+=1
        for z in tr:
            for path in z[0]:
                costr[j]+=len(path)-1

for j in range(len(sp1)):#响应
    if count1[j]>0:
        sp1r[j]=sp1[j]/count1[j]
        cost1r[j]=cost1[j]/count1[j]
    if count2[j]>0:
        sp2r[j]=sp2[j]/count2[j]
        cost2r[j]=cost2[j]/count2[j]

    if countr[j]>0:
        sprr[j]=spr[j]/countr[j]
        costrr[j]=costr[j]/countr[j]

for j in range(len(sp1)):#平均
    sp1[j]/=count
    sp2[j]/=count
    spr[j]/=count
    respondrate1[j]=count1[j]/count
    respondrate2[j]=count2[j]/count
    respondrater[j]=countr[j]/count
    cost1[j]/=count
    cost2[j]/=count
    costr[j]/=count
    keynum1[j]/=count
    keynum2[j]/=count
    keynumr[j]/=count
    time1[j]/=count
    time2[j]/=count
    timer[j]/=count


for j in range(len(trnum)):
    fp.write(str(trnum[j])+'    '+str(sp1[j])+'    '+str(sp1r[j])+'    '+str(respondrate1[j])+'    '+str(cost1[j])+'    '+str(cost1r[j])+'    '+str(keynum1[j])+'    '+str(time1[j])+'    '+str(sp2[j])+'    '+str(sp2r[j])+'    '+str(respondrate2[j])+'    '+str(cost2[j])+'    '+str(cost2r[j])+'    '+str(keynum2[j])+'    '+str(time2[j])+'    '+str(spr[j])+'    '+str(sprr[j])+'    '+str(respondrater[j])+'    '+str(costr[j])+'    '+str(costrr[j])+'    '+str(keynumr[j])+'    '+str(timer[j])+'\n')
fp.close()



sth=np.arange(0.5,1,0.05)
filename='randtopoSp_vs_sth'+str(count)+'time='+str(time.time())+'.txt'
fp = open(filename, 'w')
fp.write('sth    avesecurityprobability1    ressecurityprobability    respond_rate    avekeyconsume    reskeyconsume    keynum    time1    avesecurityprobability2    ressecurityprobability    respond_rate    avekeyconsume    requestkeyconsume    keynum2    time2    avesecurityprobabilityr    ressecurityprobability    respond_rate    avekeyconsume    requestkeyconsume    keynumr    timer\n')
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
#密钥数量
keynum1=[0]*len(sth)
keynum2=[0]*len(sth)
keynumr=[0]*len(sth)
#时间
time1=[0]*len(sth)
time2=[0]*len(sth)
timer=[0]*len(sth)
for i in range(count):
    print('count=',i)
    g=Topo().create_random_topology(60,0.06,1)
    g1=Topo().CreatNodeEdgeSet(g,10,6,0)
    g2=Topo().CreatTopo(g1)
    source=random.randint(0,len(g2[0])-1)
    des=random.randint(0,len(g2[0])-1)
    print('source=',source,'des=',des)
    while des==source:
        des=random.randint(0,len(g2[0])-1)
    for j in range(len(sth)):
        print(sth[j])
        ts1=time.time()
        t1=Alg1().alg1(copy.deepcopy(g2),source,des,sth[j])
        time1[j]+=time.time()-ts1
        print(t1)
        if t1[0][2]>0:
            count1[j]+=1
            sp1[j]+=t1[0][2]
            keynum1[j]+=1
        for z in t1:
            for path in z[0]:
                cost1[j]+=len(path)-1
        ts2=time.time()
        t2=Alg2().alg2(copy.deepcopy(g2),source,des,sth[j])
        time2[j]+=time.time()-ts2
        print(t2)
        #if t2!=t1:
            #print('*********************************************************************************************\n')
            #time.sleep(10)
        #去除分段的重复路径
        for z in t2:
            for path in z[0]:
                cost2[j]+=len(path)-1
        tmp=1
        for p in t2:
            tmp*=p[2]
        if t2[0][2]==0:
            tmp=0
        if tmp>0:
            keynum2[j]+=Seclev().segsl(t2,sth[j])
            count2[j]+=1
            sp2[j]+=tmp
        tsr=time.time()
        tr=Rr().rr(copy.deepcopy(g2),source,des,sth[j])
        timer[j]+=time.time()-tsr
        print(tr)
        if tr[0][2]>0:
            countr[j]+=1
            spr[j]+=tr[0][2]
            keynumr[j]+=1
        for z in tr:
            for path in z[0]:
                costr[j]+=len(path)-1
for j in range(len(sp1)):#响应
    if count1[j]>0:
        sp1r[j]=sp1[j]/count1[j]
        cost1r[j]=cost1[j]/count1[j]
    if count2[j]>0:
        sp2r[j]=sp2[j]/count2[j]
        cost2r[j]=cost2[j]/count2[j]

    if countr[j]>0:
        sprr[j]=spr[j]/countr[j]
        costrr[j]=costr[j]/countr[j]

for j in range(len(sp1)):#平均
    sp1[j]/=count
    sp2[j]/=count
    spr[j]/=count
    respondrate1[j]=count1[j]/count
    respondrate2[j]=count2[j]/count
    respondrater[j]=countr[j]/count
    cost1[j]/=count
    cost2[j]/=count
    costr[j]/=count
    keynum1[j]/=count
    keynum2[j]/=count
    keynumr[j]/=count
    time1[j]/=count
    time2[j]/=count
    timer[j]/=count


for j in range(len(sth)):
    fp.write(str(sth[j])+'    '+str(sp1[j])+'    '+str(sp1r[j])+'    '+str(respondrate1[j])+'    '+str(cost1[j])+'    '+str(cost1r[j])+'    '+str(keynum1[j])+'    '+str(time1[j])+'    '+str(sp2[j])+'    '+str(sp2r[j])+'    '+str(respondrate2[j])+'    '+str(cost2[j])+'    '+str(cost2r[j])+'    '+str(keynum2[j])+'    '+str(time2[j])+'    '+str(spr[j])+'    '+str(sprr[j])+'    '+str(respondrater[j])+'    '+str(costr[j])+'    '+str(costrr[j])+'    '+str(keynumr[j])+'    '+str(timer[j])+'\n')
fp.close()


g=Topo().create_random_topology(60,0.06,1)
g1=Topo().CreatNodeEdgeSet(g,10,0,0)
g2=Topo().CreatTopo(g1)


trnum=np.arange(1,11,1)
sth=0.9
filename='randtopoSp_vs_trnum'+str(count)+'time='+str(time.time())+'.txt'
fp = open(filename, 'w')
fp.write('trnum     avesecurityprobability1    ressecurityprobability    respond_rate    avekeyconsume    reskeyconsume    keynum    time1    avesecurityprobability2    ressecurityprobability    respond_rate    avekeyconsume    requestkeyconsume    keynum2    time2    avesecurityprobabilityr    ressecurityprobability    respond_rate    avekeyconsume    requestkeyconsume    keynumr    timer\n')
#平均安全概率
sp1=[0]*len(trnum)
sp2=[0]*len(trnum)
spr=[0]*len(trnum)
#响应安全概率
sp1r=[0]*len(trnum)
sp2r=[0]*len(trnum)
sprr=[0]*len(trnum)
#响应统计数
count1=[0]*len(trnum)
count2=[0]*len(trnum)
countr=[0]*len(trnum)
#响应率
respondrate1=[0]*len(trnum)
respondrate2=[0]*len(trnum)
respondrater=[0]*len(trnum)

#平均总消耗
cost1=[0]*len(trnum)
cost2=[0]*len(trnum)
costr=[0]*len(trnum)
#响应平均消耗
cost1r=[0]*len(trnum)
cost2r=[0]*len(trnum)
costrr=[0]*len(trnum)
#密钥数量
keynum1=[0]*len(trnum)
keynum2=[0]*len(trnum)
keynumr=[0]*len(trnum)
#时间
time1=[0]*len(trnum)
time2=[0]*len(trnum)
timer=[0]*len(trnum)
for i in range(count):
    print('count=',i)
    source=random.randint(0,len(g2[0])-1)
    des=random.randint(0,len(g2[0])-1)
    while des==source:
        des=random.randint(0,len(g2[0])-1)
    g=Topo().create_random_topology(60,0.06,1)
    for j in range(len(trnum)):
        #g=Net().network
        g1=Topo().CreatNodeEdgeSet(g,10,trnum[j],0)
        g2=Topo().CreatTopo(g1)
        print(trnum[j])
        ts1=time.time()
        t1=Alg1().alg1(copy.deepcopy(g2),source,des,sth)
        time1[j]+=time.time()-ts1
        print(t1)
        if t1[0][2]>0:
            count1[j]+=1
            sp1[j]+=t1[0][2]
            keynum1[j]+=1
        for z in t1:
            for path in z[0]:
                cost1[j]+=len(path)-1
        ts2=time.time()
        t2=Alg2().alg2(copy.deepcopy(g2),source,des,sth)
        time2[j]+=time.time()-ts2
        print(t2)
        #if t2!=t1:
            #print('*********************************************************************************************\n')
            #time.sleep(10)
        #去除分段的重复路径
        for z in t2:
            for path in z[0]:
                cost2[j]+=len(path)-1
        tmp=1
        for p in t2:
            tmp*=p[2]
        if t2[0][2]==0:
            tmp=0
        if tmp>0:
            keynum2[j]+=Seclev().segsl(t2,sth)
            count2[j]+=1
            sp2[j]+=tmp
        tsr=time.time()
        tr=Rr().rr(copy.deepcopy(g2),source,des,sth)
        timer[j]+=time.time()-tsr
        print(tr)
        if tr[0][2]>0:
            countr[j]+=1
            spr[j]+=tr[0][2]
            keynumr[j]+=1
        for z in tr:
            for path in z[0]:
                costr[j]+=len(path)-1

for j in range(len(sp1)):#响应
    if count1[j]>0:
        sp1r[j]=sp1[j]/count1[j]
        cost1r[j]=cost1[j]/count1[j]
    if count2[j]>0:
        sp2r[j]=sp2[j]/count2[j]
        cost2r[j]=cost2[j]/count2[j]

    if countr[j]>0:
        sprr[j]=spr[j]/countr[j]
        costrr[j]=costr[j]/countr[j]

for j in range(len(sp1)):#平均
    sp1[j]/=count
    sp2[j]/=count
    spr[j]/=count
    respondrate1[j]=count1[j]/count
    respondrate2[j]=count2[j]/count
    respondrater[j]=countr[j]/count
    cost1[j]/=count
    cost2[j]/=count
    costr[j]/=count
    keynum1[j]/=count
    keynum2[j]/=count
    keynumr[j]/=count
    time1[j]/=count
    time2[j]/=count
    timer[j]/=count


for j in range(len(trnum)):
    fp.write(str(trnum[j])+'    '+str(sp1[j])+'    '+str(sp1r[j])+'    '+str(respondrate1[j])+'    '+str(cost1[j])+'    '+str(cost1r[j])+'    '+str(keynum1[j])+'    '+str(time1[j])+'    '+str(sp2[j])+'    '+str(sp2r[j])+'    '+str(respondrate2[j])+'    '+str(cost2[j])+'    '+str(cost2r[j])+'    '+str(keynum2[j])+'    '+str(time2[j])+'    '+str(spr[j])+'    '+str(sprr[j])+'    '+str(respondrater[j])+'    '+str(costr[j])+'    '+str(costrr[j])+'    '+str(keynumr[j])+'    '+str(timer[j])+'\n')
fp.close()

"""
#算法时间规模


count=100
sth=0.9
tnum=np.arange(50,500,50)
filename='randtopotime_vs_tnum'+str(count)+'time='+str(time.time())+'.txt'
fp = open(filename, 'w')
fp.write('tnum    avesecurityprobability1    ressecurityprobability    respond_rate    avekeyconsume    reskeyconsume    keynum    time1    avesecurityprobability2    ressecurityprobability    respond_rate    avekeyconsume    requestkeyconsume    keynum2    time2    avesecurityprobabilityr    ressecurityprobability    respond_rate    avekeyconsume    requestkeyconsume    keynumr    timer\n')

#平均安全概率
sp1=[0]*len(tnum)
sp2=[0]*len(tnum)
spr=[0]*len(tnum)
#响应安全概率
sp1r=[0]*len(tnum)
sp2r=[0]*len(tnum)
sprr=[0]*len(tnum)
#响应统计数
count1=[0]*len(tnum)
count2=[0]*len(tnum)
countr=[0]*len(tnum)
#响应率
respondrate1=[0]*len(tnum)
respondrate2=[0]*len(tnum)
respondrater=[0]*len(tnum)

#平均总消耗
cost1=[0]*len(tnum)
cost2=[0]*len(tnum)
costr=[0]*len(tnum)
#响应平均消耗
cost1r=[0]*len(tnum)
cost2r=[0]*len(tnum)
costrr=[0]*len(tnum)
#密钥数量
keynum1=[0]*len(tnum)
keynum2=[0]*len(tnum)
keynumr=[0]*len(tnum)
#时间
time1=[0]*len(tnum)
time2=[0]*len(tnum)
timer=[0]*len(tnum)
for i in range(count):
    print('count=',i)
    
    for j in range(len(tnum)):
        g=Topo().create_random_topology(tnum[j],0.05,1)
        g1=Topo().CreatNodeEdgeSet(g,10,5,0)
        g2=Topo().CreatTopo(g1)
        source=random.randint(0,len(g2[0])-1)
        des=random.randint(0,len(g2[0])-1)
        print('source=',source,'des=',des)
        while des==source:
            des=random.randint(0,len(g2[0])-1)
        print(tnum[j])
        ts1=time.time()
        t1=Alg1().alg1(copy.deepcopy(g2),source,des,sth)
        time1[j]+=time.time()-ts1
        print(t1)
        if t1[0][2]>0:
            count1[j]+=1
            sp1[j]+=t1[0][2]
            keynum1[j]+=1
        for z in t1:
            for path in z[0]:
                cost1[j]+=len(path)-1
        ts2=time.time()
        t2=Alg2().alg2(copy.deepcopy(g2),source,des,sth)
        time2[j]+=time.time()-ts2
        print(t2)
        #if t2!=t1:
            #print('*********************************************************************************************\n')
            #time.sleep(10)
        #去除分段的重复路径
        for z in t2:
            for path in z[0]:
                cost2[j]+=len(path)-1
        tmp=1
        for p in t2:
            tmp*=p[2]
        if t2[0][2]==0:
            tmp=0
        if tmp>0:
            keynum2[j]+=Seclev().segsl(t2,sth)
            count2[j]+=1
            sp2[j]+=tmp
        tsr=time.time()
        tr=Rr().rr(copy.deepcopy(g2),source,des,sth)
        timer[j]+=time.time()-tsr
        print(tr)
        if tr[0][2]>0:
            countr[j]+=1
            spr[j]+=tr[0][2]
            keynumr[j]+=1
        for z in tr:
            for path in z[0]:
                costr[j]+=len(path)-1

for j in range(len(sp1)):#响应
    if count1[j]>0:
        sp1r[j]=sp1[j]/count1[j]
        cost1r[j]=cost1[j]/count1[j]
    if count2[j]>0:
        sp2r[j]=sp2[j]/count2[j]
        cost2r[j]=cost2[j]/count2[j]

    if countr[j]>0:
        sprr[j]=spr[j]/countr[j]
        costrr[j]=costr[j]/countr[j]
    time1[j]/=count1[j]
    time2[j]/=count2[j]
    timer[j]/=countr[j]

for j in range(len(sp1)):#平均
    sp1[j]/=count
    sp2[j]/=count
    spr[j]/=count
    respondrate1[j]=count1[j]/count
    respondrate2[j]=count2[j]/count
    respondrater[j]=countr[j]/count
    cost1[j]/=count
    cost2[j]/=count
    costr[j]/=count
    keynum1[j]/=count
    keynum2[j]/=count
    keynumr[j]/=count
    


for j in range(len(tnum)):
    fp.write(str(tnum[j])+'    '+str(sp1[j])+'    '+str(sp1r[j])+'    '+str(respondrate1[j])+'    '+str(cost1[j])+'    '+str(cost1r[j])+'    '+str(keynum1[j])+'    '+str(time1[j])+'    '+str(sp2[j])+'    '+str(sp2r[j])+'    '+str(respondrate2[j])+'    '+str(cost2[j])+'    '+str(cost2r[j])+'    '+str(keynum2[j])+'    '+str(time2[j])+'    '+str(spr[j])+'    '+str(sprr[j])+'    '+str(respondrater[j])+'    '+str(costr[j])+'    '+str(costrr[j])+'    '+str(keynumr[j])+'    '+str(timer[j])+'\n')
fp.close()
