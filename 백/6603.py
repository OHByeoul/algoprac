

def combi(index, level):
	global choice, lst, n
	#base
	if level == 6:
		for i in choice:
			print(i, end=' ')
		print()
		return


	for i in range(index, n):
		choice.append(lst[i])
		combi(i+1, level+1)
		choice.pop()



while True:
	lst = list(map(int,input().split()))
	n = lst[0]
	lst = lst[1:]
	choice = []

	if n == 0:
		break

	combi(0,0)
	print()