import sys,heapq
class Dijkstra:
    def __init__(self):
        self._passed=[]
        self._nopass=[]
        self._prev=[]  #记录从源点V0到终点Vi的当前最短路径上终点Vi的直接前驱顶点序号，若V0到Vi之间有边前驱为V0否则为-1 
        self._cost=[]  #记录源点到终点之间最短路径的代价，存在记V0到Vi的边的代价，否则记为MAX
        self._path=[]  #源点到目的点的路径

    def dijkstra(self,g,source,des):
        #初始化起点
        self._passed.append(source)
        self.g=g
        self._visited=[0]*len(g)

        #初始化前驱列表以及代价
        for i in range(len(g)):
            if i==source:
                self._cost.append(1)
            else:
                self._cost.append(0)
        heap=[]
        for i in self.g[source]:
            self._prev[i.index]=source
            self._cost[i.index]=1
            heapq.heappush(heap,(1-i.sp,i))  #要将高安全概率的节点优先级提高，将sp值转化为1-f
        while heap!=[]:
            #弹出最大安全概率节点
            tmpe=heapq.heappop(heap)
            tmp=list(tmpe)
            tmp[0]=1-tmp[0] #重新转化为安全概率p
            tmpe=tuple(tmp)
            if self._visited[tmpe[1].index]==1:#如果该点已到过，就进行下一次循环
                continue
            self._visited[tmpe[1].index]==1
            for i in self.g[tmpe[1].index]:
                if self._cost[tmpe[1].index]*tmpe[1].sp>self._cost[i.index]:
                    self._cost[i.index]=self._cost[tmpe[1].index]*tmpe[1].sp
                    self._prev[i.index]=tmpe[1].index
                    heapq.heappush(heap,(1-self._cost[i.index],i))
        #确定路径
        path=self.getpath(des)
        if path[0]==source and len(path)>=2:
            return path
        else:
            return []
    def getpath(self,u):   #获取到当前点u的路径
        tmp=u
        li=[]
        while u!=-1:
            li.append(u)
            u=self._prev[u]

        li.reverse()
        return li
