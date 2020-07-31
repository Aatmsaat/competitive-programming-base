import sys
sys.setrecursionlimit(int(1e5)+7)
ip=sys.stdin.readline

for _ in range(int(ip())):
	n=int(ip())
	graph=[[] for _ in range(n+1)]
	
	for _ in range(n):
		x,y=map(int, ip().split())
		x-=1; y-=1
		graph[x].append(y)
		graph[y].append(x)
		
	path=[]#euler tour
		
	def dfs(node, ancestor):
		
		path.append(node+1)
		
		for destination in graph[node]:
			if destination==ancestor: continue
			dfs(destination, node)
		else: path.append(node+1)
		#uncomment when return value
		#ans[0]
		
	dfs(0,-1)
	print(*path)
