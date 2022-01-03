from Topo import *
from Net import *
from Alg1 import *
from RandomRouting import *
g=Net().network
g1=Topo().CreatNodeEdgeSet(g,10,4,0)
g2=Topo().CreatTopo(g1)

#path,pathsp,fsp=Alg1().alg1(g2,3,26,0.99)
path1,pathsp1,fsp1=Rr().rr(g2,3,26,0.9)
#print(path,pathsp,fsp)

print(path1,pathsp1,fsp1)