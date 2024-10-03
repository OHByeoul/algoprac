N = int(input())

a = [tuple(map(int, input().split())) for _ in range(N)]

a = sorted(a, key=lambda x : (x[1]*x[2]*x[3], x[1]+x[2]+x[3], x[0]))

for n,s1,s2,s3 in a[:3]:
	print(n, end=' ')