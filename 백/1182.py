from itertools import combinations

N, S = map(int,input().split())

infos = list(map(int, input().split()))

ans = 0

for i in range(1, len(infos)+1):
	for comb in combinations(infos,i):
		if sum(comb) == S:
			ans += 1

print(ans)