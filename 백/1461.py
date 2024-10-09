N,M = map(int,input().split())

book = list(map(int,input().split()))

pos = []
neg = []

for each in book:
	if each > 0:
		pos.append(each)
	else:
		neg.append(-1*each)

pos = sorted(pos)[::-1]
neg = sorted(neg)[::-1]

dist = []

for i in neg[::M]:
	dist.append(i)

for i in pos[::M]:
	dist.append(i)

ans = sum(dist)*2-max(dist)

print(ans)

