﻿#随机可信中继，固定拓扑，随机请求

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
runcount=100

g=Net().network
g1=Topo().CreatNodeEdgeSet(g,10,6,0.9,0)
g2=Topo().CreatTopo(g1)

sth=[0.6,0.9]
nodespset=[0.6,0.65,0.7,0.75,0.8,0.85,0.9]
for th in sth:
    count=0
    filename='Sp_vs_nodesp'+str(th)+'time='+str(time.time())+'.txt'
    fp = open(filename, 'w')
    fp.write('nodesp    asp1    rsp1    gsp1    rr1    rrg1    acost1    rcost1    keyn1    time1    asp2    rsp2    gsp2    rr2    rrg2   acost2    rcost2    keyn2    time2    aspr    rspr    gspr    rrr    rrgr   acostr   rcostr   keynr    timer\n')
    #平均安全概率总运行次数
    sp1=[0]*len(nodespset)
    sp2=[0]*len(nodespset)
    spr=[0]*len(nodespset)
    #临时
    tsp1=[0]*len(nodespset)
    tsp2=[0]*len(nodespset)
    tspr=[0]*len(nodespset)
    #响应安全概率满足请求的运行次数
    sp1r=[0]*len(nodespset)
    sp2r=[0]*len(nodespset)
    sprr=[0]*len(nodespset)
    #筛选安全概率：alg2满足的次数
    sp1g=[0]*len(nodespset)
    sp2g=[0]*len(nodespset)
    sprg=[0]*len(nodespset)
    #响应统计数
    count1=[0]*len(nodespset)
    count2=[0]*len(nodespset)
    countr=[0]*len(nodespset)
    countk=[0]*len(nodespset)
    #临时
    tcount1=[0]*len(nodespset)
    tcount2=[0]*len(nodespset)
    tcountr=[0]*len(nodespset)
    #响应统计数优势
    count1g=[0]*len(nodespset)
    count2g=[0]*len(nodespset)
    countrg=[0]*len(nodespset)
    #响应率
    rr1=[0]*len(nodespset)
    rr2=[0]*len(nodespset)
    rrr=[0]*len(nodespset)
    #对比响应率除以alg2满足的最大次数
    rr1g=[0]*len(nodespset)
    rr2g=[0]*len(nodespset)
    rrrg=[0]*len(nodespset)


    #平均总消耗
    cost1=[0]*len(nodespset)
    cost2=[0]*len(nodespset)
    costr=[0]*len(nodespset)
    #响应平均消耗
    cost1r=[0]*len(nodespset)
    cost2r=[0]*len(nodespset)
    costrr=[0]*len(nodespset)
    #筛选平均消耗/alg2满足的次数
    cost1g=[0]*len(nodespset)
    cost2g=[0]*len(nodespset)
    costrg=[0]*len(nodespset)
    #密钥数量
    keynum1=[0]*len(nodespset)
    keynum2=[0]*len(nodespset)
    keynumr=[0]*len(nodespset)
    
    #时间
    time1=[0]*len(nodespset)
    time2=[0]*len(nodespset)
    timer=[0]*len(nodespset)
    #循环次数
    count=0
    while count<runcount:
        
        g1=Topo().CreatNodeEdgeSet(g,10,4,0.9,0)
        g2=Topo().CreatTopo(g1)
        source=random.randint(0,len(g2[0])-1)
        while g2[1][source]==1:
            source=random.randint(0,len(g2[0])-1)
        des=random.randint(0,len(g2[0])-1)
        while des==source or g2[1][des]==1:
            des=random.randint(0,len(g2[0])-1)
    
        print(source,des)
        f=0
        for j in range(len(nodespset)):#循环nodesp

            print('nodesp=',nodespset[j])
            Topo().Changenodesp(g2,nodespset[j])
            t1=Alg1().alg1(copy.deepcopy(g2),source,des,th)
            t2=Alg2().alg2(copy.deepcopy(g2),source,des,th)
            tr=Rr().rr(copy.deepcopy(g2),source,des,th)
            print(t1)
            if t1[0][2]>0:
                count1[j]+=1
                sp1[j]+=t1[0][2]
                tsp1[j]+=t1[0][2]
                tcount1[j]+=1
                keynum1[j]+=1
            for z in t1:
                for path in z[0]:
                    cost1[j]+=len(path)-1
            #alg2
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
                keynum2[j]+=Seclev().segsl(t2,th)
                count2[j]+=1
                tcount2[j]+=1
                sp2[j]+=tmp
                tsp2[j]+=tmp
            #rr
            print(tr)
            if tr[0][2]>0:
                countr[j]+=1
                spr[j]+=tr[0][2]
                tcountr[j]+=1
                tspr[j]+=tr[0][2]
                keynumr[j]+=1
            for z in tr:
                for path in z[0]:
                    costr[j]+=len(path)-1

            if t2!=t1:
                f=1

        if f==1:
            count+=1
            for j in range(len(nodespset)):
                sp1g[j]+=tsp1[j]
                
                sp2g[j]+=tsp2[j]
                
                sprg[j]+=tspr[j]
                
                count1g[j]+=tcount1[j]
                
                count2g[j]+=tcount2[j]
                
                countrg[j]+=tcountr[j]
                
        for j in range(len(nodespset)):
            tsp1[j]=0
            tsp2[j]=0
            tspr[j]=0
            tcount1[j]=0
            tcount2[j]=0
            tcountr[j]=0

    for j in range(len(nodespset)):#响应
        if count1[j]>0:
            sp1r[j]=sp1g[j]/count1g[j]
            #cost1r[j]=cost1[j]/count1[j]
        if count2[j]>0:
            sp2r[j]=sp2g[j]/count2g[j]
            #cost2r[j]=cost2[j]/count2[j]

        if countr[j]>0:
            sprr[j]=sprg[j]/countrg[j]
            #costrr[j]=costr[j]/countr[j]
    #找出count2最大值作为除数
  
    for j in range(len(nodespset)):#筛选
        

        
        sp1g[j]=sp1g[j]/countk[j]
        sp2g[j]=sp2g[j]/countk[j]
        sprg[j]=sprg[j]/countk[j]
        rr1g[j]=count1g[j]/countk[j]
        rr2g[j]=count2g[j]/countk[j]
        rrrg[j]=countrg[j]/countk[j]

    for j in range(len(nodespset)):#绝对平均
        sp1[j]/=runcount
        sp2[j]/=runcount
        spr[j]/=runcount
        rr1[j]=count1[j]/runcount
        rr2[j]=count2[j]/runcount
        rrr[j]=countr[j]/runcount
        cost1[j]/=runcount
        cost2[j]/=runcount
        costr[j]/=runcount
        keynum1[j]/=runcount
        keynum2[j]/=runcount
        keynumr[j]/=runcount
        time1[j]/=runcount
        time2[j]/=runcount
        timer[j]/=runcount


    for j in range(len(nodespset)):
        fp.write(str(nodespset[j])+'    '+str(sp1[j])+'    '+str(sp1r[j])+'    '+str(sp1g[j])+'    '+str(rr1[j])+'    '+str(rr1g[j])+'    '+str(cost1[j])+'    '+str(cost1r[j])+'    '+str(keynum1[j])+'    '+str(time1[j])+'    '+str(sp2[j])+'    '+str(sp2r[j])+'    '+str(sp2g[j])+'    '+str(rr2[j])+'    '+str(rr2g[j])+'    '+str(cost2[j])+'    '+str(cost2r[j])+'    '+str(keynum2[j])+'    '+str(time2[j])+'    '+str(spr[j])+'    '+str(sprr[j])+'    '+str(sprg[j])+'    '+str(rrr[j])+'    '+str(rrrg[j])+'    '+str(costr[j])+'    '+str(costrr[j])+'    '+str(keynumr[j])+'    '+str(timer[j])+'\n')
    fp.write('countk')
    for j in countk:
        fp.write(str(j)+'    ')
    fp.write('\n')
    fp.write('count1g')
    for j in count1g:
        fp.write(str(j)+'    ')
    fp.write('\n')
    fp.write('count2g')
    for j in count2g:
        fp.write(str(j)+'    ')
    fp.write('\n')
    fp.write('countrg')
    for j in countrg:
        fp.write(str(j)+'    ')
    fp.write('\n')
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