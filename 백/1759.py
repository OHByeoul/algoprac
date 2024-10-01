from itertools import combinations

def is_condi(each):
	vow = 0
	for each in word:
		vow += (each in vowels)
	ja = L - vow
	return (vow >=1 and ja >= 2)

L,C = map(int,input().split())
arr = input().split()

arr.sort()

vowels = ['a','e','i','o','u']

for word in combinations(arr, L):
	if is_condi(word):
		print(''.join(word))

# def is_condi():
# 	global ans, L

# 	vow = 0
# 	for each in ans:
# 		vow += (each in vows)
# 	ja = len(ans) - vow

# 	return (vow >= 1 and ja >=2)


# def combi(idx, lev):
# 	global arr,L

# 	if lev == L:
# 		if is_condi():
# 			print(''.join(ans))
# 		return

# 	for i in range(idx, C):
# 		ans.append(arr[i])
# 		combi(i+1, lev+1)
# 		ans.pop()

# L, C = map(int, input().split())
# arr = input().split()
# vows = ['a','e','i','o','u']


# arr.sort()

# ans = []

# combi(0,0)