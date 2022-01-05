from Topo import *
from Net import *
from Alg1 import *
from RandomRouting import *
from Alg2 import *
import copy,random
g=Net().network
g1=Topo().CreatNodeEdgeSet(g,10,2,0)
g2=Topo().CreatTopo(g1)
source=random.randint(0,len(g2[0])-1)
des=random.randint(0,len(g2[0])-1)
while des==source:
    des=random.randint(0,len(g2[0])-1)
path,pathsp,fsp=Alg1().alg1(copy.deepcopy(g2),source,des,0.7)
print(path,pathsp,fsp)
#path1,pathsp1,fsp1=Rr().rr(g2,3,26,0.9)
t=Alg2().alg2(copy.deepcopy(g2),source,des,0.7)


print(t)