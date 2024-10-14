import sys
sys.setrecursionlimit(1000000)

def rec(x,y):
	global arr, dp

	if dp[x][y] != -1:
		return dp[x][y]

	dp[x][y] = max(rec(x-1,y),rec(x,y-1),rec(x-1,y-1))+arr[x][y]
	return dp[x][y]



N, M = map(int,input().split())
arr = [[0]+list(map(int, input().split())) for _ in range(N)]
arr = [[0]*(M+1)]+arr

dp = [[-1 for _ in range(M+1)] for _ in range(N+1)]


for j in range(0, M+1):
	dp[0][j] = 0

for i in range(0,N+1):
	dp[i][0]= 0

print(i,j)
print(rec(i,j))