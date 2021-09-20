from sys import stdin, setrecursionlimit as srl
from threading import stack_size, Thread

srl(int(1e9)+7)
stack_size(int(1e8))
ip=stdin.readline

def main():
	n, m=map(int, input('Enter No. of nodes and edges: ').split())
	print('Enter edges for Directed Acyclic Graph')
	adj=[[] for _ in range(n+1)]
	while m:
		m-=1
		x,y=map(int, ip().split())
		adj[x].append(y)
	
	visited=[0]*(n+1)
	stk=[]
	for x in range(1, n+1):
		def topsort(v):
			if visited[v]: return
			visited[v]=1
			for i in adj[v]:
				topsort(i)
			stk.append(v)
		if not visited[x]: topsort(x)
		
	print(*stk[::-1])
	
Thread(target=main).start()
