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
runcount=10

g=Net().network
g1=Topo().CreatNodeEdgeSet(g,10,4,0.9,0)
g2=Topo().CreatTopo(g1)

sth=[0.6,0.9]
trnum=np.arange(1,10,1)
for th in sth:
    count=0 #总运行次数
    filename='Sp_vs_trnum'+str(th)+'time='+str(time.time())+'.txt'
    fp = open(filename, 'w')
    fp.write('nodesp    asp1    rsp1    gsp1    rr1    rrg1    acost1    rcost1    keyn1    time1    asp2    rsp2    gsp2    rr2    rrg2   acost2    rcost2    keyn2    time2    aspr    rspr    gspr    rrr    rrgr   acostr   rcostr   keynr    timer\n')
    #平均安全概率
    sp1=[0]*len(trnum)
    sp2=[0]*len(trnum)
    spr=[0]*len(trnum)
    #响应安全概率
    sp1r=[0]*len(trnum)
    sp2r=[0]*len(trnum)
    sprr=[0]*len(trnum)
     #筛选安全概率：alg2满足的次数
    sp1g=[0]*len(trnum)
    sp2g=[0]*len(trnum)
    sprg=[0]*len(trnum)
    #响应统计数
    count1=[0]*len(trnum)
    count2=[0]*len(trnum)
    countr=[0]*len(trnum)
    countk=[0]*len(trnum)
    #响应统计数优势
    count1g=[0]*len(trnum)
    count2g=[0]*len(trnum)
    countrg=[0]*len(trnum)
    #响应率
    rr1=[0]*len(trnum)
    rr2=[0]*len(trnum)
    rrr=[0]*len(trnum)
    #对比响应率除以alg2满足的最大次数
    rr1g=[0]*len(trnum)
    rr2g=[0]*len(trnum)
    rrrg=[0]*len(trnum)


    #平均总消耗
    cost1=[0]*len(trnum)
    cost2=[0]*len(trnum)
    costr=[0]*len(trnum)
    #响应平均消耗
    cost1r=[0]*len(trnum)
    cost2r=[0]*len(trnum)
    costrr=[0]*len(trnum)
    #筛选平均消耗/alg2满足的次数
    cost1g=[0]*len(trnum)
    cost2g=[0]*len(trnum)
    costrg=[0]*len(trnum)
    #密钥数量
    keynum1=[0]*len(trnum)
    keynum2=[0]*len(trnum)
    keynumr=[0]*len(trnum)
    #时间
    time1=[0]*len(trnum)
    time2=[0]*len(trnum)
    timer=[0]*len(trnum)
    #循环次数
    f=0
    while f==0:
        count+=1
        print(count)
        if count>runcount:
            break
        source=random.randint(0,len(g2[0])-1)
        des=random.randint(0,len(g2[0])-1)
        while des==source:
            des=random.randint(0,len(g2[0])-1)
    
        print(source,des)    
        for j in range(len(trnum)):#循环nodesp
            
            g1=Topo().CreatNodeEdgeSet(g,10,trnum[j],0.9,0)
            g2=Topo().CreatTopo(g1)
            print('trnum=',trnum[j])
        
            t1=Alg1().alg1(copy.deepcopy(g2),source,des,th)
            t2=Alg2().alg2(copy.deepcopy(g2),source,des,th)
            #if t1==t2:
                #continue
            tr=Rr().rr(copy.deepcopy(g2),source,des,th)
            
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
            if t1!=t2 or t2[0][2]==0:
                countk[j]+=1
                if t1[0][2]>0:
                    count1g[j]+=1
                if tmp>0:
                    count2g[j]+=1
                if tr[0][2]>0:
                    countrg[j]+=1
                sp1g[j]+=t1[0][2]
                sp2g[j]+=tmp
                sprg[j]+=tr[0][2]


    for j in range(len(trnum)):#响应
        if count1[j]>0:
            sp1r[j]=sp1[j]/count1[j]
            cost1r[j]=cost1[j]/count1[j]
        if count2[j]>0:
            sp2r[j]=sp2[j]/count2[j]
            cost2r[j]=cost2[j]/count2[j]

        if countr[j]>0:
            sprr[j]=spr[j]/countr[j]
            costrr[j]=costr[j]/countr[j]
    #找出count2最大值作为除数
    
    for j in range(len(trnum)):#筛选
        

        
        sp1g[j]=sp1g[j]/countk[j]
        sp2g[j]=sp2g[j]/countk[j]
        sprg[j]=sprg[j]/countk[j]
        rr1g[j]=count1[j]/countk[j]
        rr2g[j]=count2[j]/countk[j]
        rrrg[j]=countr[j]/countk[j]
    for j in range(len(trnum)):#平均
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
        


    for j in range(len(trnum)):
        fp.write(str(trnum[j])+'    '+str(sp1[j])+'    '+str(sp1r[j])+'    '+str(sp1g[j])+'    '+str(rr1[j])+'    '+str(rr1g[j])+'    '+str(cost1[j])+'    '+str(cost1r[j])+'    '+str(keynum1[j])+'    '+str(time1[j])+'    '+str(sp2[j])+'    '+str(sp2r[j])+'    '+str(sp2g[j])+'    '+str(rr2[j])+'    '+str(rr2g[j])+'    '+str(cost2[j])+'    '+str(cost2r[j])+'    '+str(keynum2[j])+'    '+str(time2[j])+'    '+str(spr[j])+'    '+str(sprr[j])+'    '+str(sprg[j])+'    '+str(rrr[j])+'    '+str(rrrg[j])+'    '+str(costr[j])+'    '+str(costrr[j])+'    '+str(keynumr[j])+'    '+str(timer[j])+'\n')
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
    """
    fig = plt.figure()
    plt.plot(trnum,sp1,color='red')
    plt.plot(trnum,sp2,color='green')
    plt.plot(trnum,spr,color='black')
    plt.title("average Security probability")
    plt.xlabel('trnum')
    plt.ylabel('Security probability')
    plt.show()

    fig = plt.figure()
    plt.plot(trnum,sp1r,color='red')
    plt.plot(trnum,sp2r,color='green')
    plt.plot(trnum,sprr,color='black')
    plt.title("res Security probability")
    plt.xlabel('trnum')
    plt.ylabel('Security probability')
    plt.show()

    fig = plt.figure()
    plt.plot(trnum,count1,color='red')
    plt.plot(trnum,count2,color='green')
    plt.plot(trnum,countr,color='black')
    plt.title("request Response rate  ")
    plt.xlabel('trnum')
    plt.ylabel('Response rate')
    plt.show()

    fig = plt.figure()
    plt.plot(trnum,cost1,color='red')
    plt.plot(trnum,cost2,color='green')
    plt.plot(trnum,costr,color='black')
    plt.title("ave key consume")
    plt.xlabel('trnum')
    plt.ylabel('consume')
    plt.show()


    fig = plt.figure()
    plt.plot(trnum,cost1r,color='red')
    plt.plot(trnum,cost2r,color='green')
    plt.plot(trnum,costrr,color='black')
    plt.title("res key consume")
    plt.xlabel('trnum')
    plt.ylabel('consume')
    plt.show()

    fig = plt.figure()
    plt.plot(trnum,keynum1,color='red')
    plt.plot(trnum,keynum2,color='green')
    plt.plot(trnum,keynumr,color='black')
    plt.title("final key number")
    plt.xlabel('trnum')
    plt.ylabel('final key')
    plt.show()
    """