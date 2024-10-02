N = int(input())

arr = [i for i in range(1, N+1)]
ans = []

check = [False] * (N+2)

def perm(level):
	global ans
	if level == N:
		print(*ans, sep=' ')
		return


	for i in range(0,N):
		if check[i] == True:
			continue

		ans.append(arr[i])
		check[i] = True
		perm(level+1)

		check[i] = False
		ans.pop()


perm(0)
