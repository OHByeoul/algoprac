from itertools import combinations


while True:
	I = list(map(int,(input().split())))

	k = I[0]
	arr = I[1:]

	if k == 0:
		break

	for each in combinations(arr, 6):
		for u in each:
			print(u, end= ' ')
		print()
	print()


# def combi(index, level):
# 	global choice, lst, n
# 	#base
# 	if level == 6:
# 		for i in choice:
# 			print(i, end=' ')
# 		print()
# 		return


# 	for i in range(index, n):
# 		choice.append(lst[i])
# 		combi(i+1, level+1)
# 		choice.pop()



# while True:
# 	lst = list(map(int,input().split()))
# 	n = lst[0]
# 	lst = lst[1:]
# 	choice = []

# 	if n == 0:
# 		break

# 	combi(0,0)
# 	print()