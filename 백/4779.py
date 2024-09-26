def kan(n):
	#base
	if n ==0:
		print('-', end='')
		return

	#recursive
	kan(n-1)
	print(' '*(3**(n-1)), end='')
	kan(n-1)


while True:
	try:
		n = int(input())
		kan(n)
		print()
	except:
		break

