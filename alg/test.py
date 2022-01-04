from Topo import *
from Net import *
from Alg1 import *
from RandomRouting import *
from Alg2 import *
import copy
g=Net().network
g1=Topo().CreatNodeEdgeSet(g,10,4,0)
g2=Topo().CreatTopo(g1)

path,pathsp,fsp=Alg1().alg1(copy.deepcopy(g2),3,18,0.7)
print(path,pathsp,fsp)
#path1,pathsp1,fsp1=Rr().rr(g2,3,26,0.9)
path2,pathsp2,fsp2=Alg2().alg2(copy.deepcopy(g2),3,18,0.7)


print(path2,pathsp2,fsp2)