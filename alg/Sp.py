#计算安全概率
class Sp:
	def __init__(self):
		pass

	def CalSumSecurityProbability(self,cur_sp,path_sp):
		return 1-(1-cur_sp)*(1-path_sp)

	def pathsp(self,topo,path):#计算路径安全概率
		nodelist=path[1:-1]
		tmp=1
		for i in nodelist:
			tmp*=topo[1][i]

		return tmp
	def checkring(self,path):
		p=0
		q=0
		for i in range(len(path)):
			for j in range(i+1,len(path)):
				if path[i]==path[j]:
					p=i
					q=j
					return [p,q]
		return [p,q]