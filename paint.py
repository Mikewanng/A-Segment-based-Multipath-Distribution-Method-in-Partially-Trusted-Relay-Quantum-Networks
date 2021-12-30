import numpy as np

def CalMP(n,l,p):
    return 1-(1-p**l)**n

p=np.arange(0,1.01,0.01)
l=np.arange(1,21,1)
n=np.arange(1,6,1)

"""
filename='probability vs p.txt'
fp=open(filename,'w')
fp.write('p    pro    n    pro    n    pro    n    pro    n    pro    n\n')
for i in p:
    fp.write(str(i)+'    ')
    for j in n:
        fp.write(str(CalMP(j,10,i))+'    '+str(j)+'    ')
    fp.write('\n')

fp.close
"""
filename='probability vs l.txt'
fp=open(filename,'w')
fp.write('l    pro    n\n')
for i in l:
    fp.write(str(i)+'    ')
    for j in n:
        fp.write(str(CalMP(j,i,0.9))+'    '+str(j)+'    ')
    fp.write('\n')

fp.close
