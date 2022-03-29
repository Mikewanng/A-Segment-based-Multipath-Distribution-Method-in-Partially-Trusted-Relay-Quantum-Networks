#随机可信中继，固定拓扑，随机请求

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
valuecount=1000

g=Net().network
g1=Topo().CreatNodeEdgeSet(g,10,4,0.9,0)
g2=Topo().CreatTopo(g1)

sth=[0.6,0.9]
nodespset=np.arange(0.65,0.95,0.05)
for th in sth:
    count=0
    filename='Sp_vs_nodesp'+str(th)+'time='+str(time.time())+'.txt'
    fp = open(filename, 'w')
    fp.write('nodesp    avesecurityprobability1    ressecurityprobability    respond_rate    avekeyconsume    reskeyconsume    keynum    time1    avesecurityprobability2    ressecurityprobability    respond_rate    avekeyconsume    requestkeyconsume    keynum2    time2    avesecurityprobabilityr    ressecurityprobability    respond_rate    avekeyconsume    requestkeyconsume    keynumr    timer\n')
    #平均安全概率
    sp1=[0]*len(nodespset)
    sp2=[0]*len(nodespset)
    spr=[0]*len(nodespset)
    #响应安全概率
    sp1r=[0]*len(nodespset)
    sp2r=[0]*len(nodespset)
    sprr=[0]*len(nodespset)
    #响应统计数
    count1=[0]*len(nodespset)
    count2=[0]*len(nodespset)
    countr=[0]*len(nodespset)
    countk=[0]*len(nodespset)
    #响应率
    respondrate1=[0]*len(nodespset)
    respondrate2=[0]*len(nodespset)
    respondrater=[0]*len(nodespset)

    #平均总消耗
    cost1=[0]*len(nodespset)
    cost2=[0]*len(nodespset)
    costr=[0]*len(nodespset)
    #响应平均消耗
    cost1r=[0]*len(nodespset)
    cost2r=[0]*len(nodespset)
    costrr=[0]*len(nodespset)
    #密钥数量
    keynum1=[0]*len(nodespset)
    keynum2=[0]*len(nodespset)
    keynumr=[0]*len(nodespset)
    #时间
    time1=[0]*len(nodespset)
    time2=[0]*len(nodespset)
    timer=[0]*len(nodespset)
    #循环次数
    f=0
    while f==0:
        count+=1
        g1=Topo().CreatNodeEdgeSet(g,10,4,0.9,0)
        g2=Topo().CreatTopo(g1)
        source=random.randint(0,len(g2[0])-1)
        des=random.randint(0,len(g2[0])-1)
        while des==source:
            des=random.randint(0,len(g2[0])-1)
    
        print(source,des)    
        for j in range(len(nodespset)):#循环nodesp

            print('nodesp=',nodespset[j])
            Topo().Changenodesp(g2,nodespset[j])
            t1=Alg1().alg1(copy.deepcopy(g2),source,des,th)
            t2=Alg2().alg2(copy.deepcopy(g2),source,des,th)
            #if t1==t2:
                #continue
            tr=Rr().rr(copy.deepcopy(g2),source,des,th)
            countk[j]+=1
            #alg1
            
            print(t1)
            if t1[0][2]>0:
                count1[j]+=1
                sp1[j]+=t1[0][2]
                keynum1[j]+=1
            for z in t1:
                for path in z[0]:
                    cost1[j]+=len(path)-1
            #alg2
            print(t2)
            
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
                keynum2[j]+=Seclev().segsl(t2,th)
                count2[j]+=1
                sp2[j]+=tmp
            #rr
        
            print(tr)
            if tr[0][2]>0:
                countr[j]+=1
                spr[j]+=tr[0][2]
                keynumr[j]+=1
            for z in tr:
                for path in z[0]:
                    costr[j]+=len(path)-1
            f=0
            for i in countk:
                if i>valuecount:
                    f=1


    for j in range(len(nodespset)):#响应
        if count1[j]>0:
            sp1r[j]=sp1[j]/count1[j]
            cost1r[j]=cost1[j]/count1[j]
        if count2[j]>0:
            sp2r[j]=sp2[j]/count2[j]
            cost2r[j]=cost2[j]/count2[j]

        if countr[j]>0:
            sprr[j]=spr[j]/countr[j]
            costrr[j]=costr[j]/countr[j]

    for j in range(len(nodespset)):#平均
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


    for j in range(len(nodespset)):
        fp.write(str(nodespset[j])+'    '+str(sp1[j])+'    '+str(sp1r[j])+'    '+str(respondrate1[j])+'    '+str(cost1[j])+'    '+str(cost1r[j])+'    '+str(keynum1[j])+'    '+str(time1[j])+'    '+str(sp2[j])+'    '+str(sp2r[j])+'    '+str(respondrate2[j])+'    '+str(cost2[j])+'    '+str(cost2r[j])+'    '+str(keynum2[j])+'    '+str(time2[j])+'    '+str(spr[j])+'    '+str(sprr[j])+'    '+str(respondrater[j])+'    '+str(costr[j])+'    '+str(costrr[j])+'    '+str(keynumr[j])+'    '+str(timer[j])+'\n')
    fp.close()
    '''
    fig = plt.figure()
    plt.plot(nodespset,sp1,color='red')
    plt.plot(nodespset,sp2,color='green')
    plt.plot(nodespset,spr,color='black')
    plt.title("average Security probability")
    plt.xlabel('nodespset')
    plt.ylabel('Security probability')
    plt.show()

    fig = plt.figure()
    plt.plot(nodespset,sp1r,color='red')
    plt.plot(nodespset,sp2r,color='green')
    plt.plot(nodespset,sprr,color='black')
    plt.title("res Security probability")
    plt.xlabel('nodespset')
    plt.ylabel('Security probability')
    plt.show()

    fig = plt.figure()
    plt.plot(nodespset,count1,color='red')
    plt.plot(nodespset,count2,color='green')
    plt.plot(nodespset,countr,color='black')
    plt.title("request Response rate  ")
    plt.xlabel('nodespset')
    plt.ylabel('Response rate')
    plt.show()

    fig = plt.figure()
    plt.plot(nodespset,cost1,color='red')
    plt.plot(nodespset,cost2,color='green')
    plt.plot(nodespset,costr,color='black')
    plt.title("ave key consume")
    plt.xlabel('nodespset')
    plt.ylabel('consume')
    plt.show()


    fig = plt.figure()
    plt.plot(nodespset,cost1r,color='red')
    plt.plot(nodespset,cost2r,color='green')
    plt.plot(nodespset,costrr,color='black')
    plt.title("res key consume")
    plt.xlabel('nodespset')
    plt.ylabel('consume')
    plt.show()

    fig = plt.figure()
    plt.plot(nodespset,keynum1,color='red')
    plt.plot(nodespset,keynum2,color='green')
    plt.plot(nodespset,keynumr,color='black')
    plt.title("final key number")
    plt.xlabel('nodespset')
    plt.ylabel('final key')
    plt.show()
    '''