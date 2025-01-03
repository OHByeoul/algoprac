from collections import deque

N, M, start = map(int, input().split())


g = [[] for _ in range(N+1)]

visit = [False]*(N+1)
visit2 = [False]*(N+1)


for m in range(M):
	v1,v2 = map(int, input().split())
	g[v1].append(v2)
	g[v2].append(v1)


for each in range(1,N+1):
	g[each].sort()

def dfs(start):
	if visit[start]:
		return
	visit[start] = True
	print(start, end=' ')

	for v in g[start]:
		dfs(v)


def bfs(start):
	q = deque()
	q.append(start)
	visit2[start] = True

	while q:
		n = q.popleft()
		print(n, end=' ')

		for each in g[n]:
			if visit2[each]:
				continue
			visit2[each] = True
			q.append(each)
		


dfs(start)
print()
bfs(start)
print()
