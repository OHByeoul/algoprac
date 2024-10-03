N = int(input())

g = [list(map(int,input().split())) for _ in range(N)]

g = sorted(g)

for x,y in g:
	print(x,y, sep=' ')