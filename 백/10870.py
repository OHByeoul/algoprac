n = int(input())



def fibo(n):
	global arr
	
	if arr[n] != -1:
		return arr[n]

	arr[n] = fibo(n-1)+fibo(n-2)
	return arr[n]

arr = [-1] * (n+2)
arr[0] = 0
arr[1] = 1

print(fibo(n))





# def fibo(n):
# 	arr = [-1] * (n+2)
# 	arr[0] = 0
# 	arr[1] = 1

# 	for i in range(2, n+1):
# 		arr[i] = arr[i-1] + arr[i-2]
# 	return arr[n]

# print(fibo(0))



# def fibo(n):
# 	ret = 0
# 	if n <= 1:
# 		ret = n
# 	for i in range(2, n+1):
# 		ret = fibo(i-1)+fibo(i-2)
# 	return ret

# print(fibo(n))