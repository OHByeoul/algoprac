def beak(lev):
	global ans
	#base 
	if lev == len(S):
		ans +=1
		return


	for char in chars:
		if cnt[char] == 0:
			continue

		print(char,' ', cnt[char])
		if (not choose) or (choose[-1] != char):
			choose.append(char)
			cnt[char] -= 1
			beak(lev+1)
			choose.pop()
			cnt[char] += 1



S = input()
cnt = dict()
chars = set()
choose = []
ans = 0

for each in S:
	chars.add(each)
	if each not in cnt:
		cnt[each] = 0
	cnt[each] += 1

beak(0)
print(ans)
