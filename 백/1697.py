from collections import deque

N, K = map(int, input().split())

dx = [-1,1,2]

visit = [False] * 100001


q = deque()
q.append((0,N))
visit[N] = True

while q:
	t, p= q.popleft()

	if p == K:
		print(t)
		break
 
	for i in range(3):
		if i == 2:
			np = p*dx[i]
		else:
			np = p+dx[i]

		if 0 <= np <= 100000 and not visit[np]:
			visit[np] = True
			q.append((t+1,np))
