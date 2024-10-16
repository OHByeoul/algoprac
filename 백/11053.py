N = int(input())

arr = [0]+list(map(int, input().split()))

dp = [-1 for _ in range(N+1)]


dp[1] = 1

for i in range(2, N+1):
	best = 0
	for j in range(1, i):
		if arr[i] > arr[j]:
			best = max(best, dp[j])
	dp[i] = best + 1


print(max(dp[1:]))

