from itertools import permutations

N = int(input())

infos = [input().split() for _ in range(N)]

ans = 0
for perm in permutations(range(1,9+1),3):
	ok = True
	for num,st,ball in infos:
		real_st = real_ball = 0
		for i in range(3):
			if num[i] == str(perm[i]):
				real_st += 1
			elif str(perm[i]) in num:
				real_ball += 1

		if real_st != int(st) or real_ball != int(ball):
			ok = False

	if ok:
		ans += 1

print(ans)