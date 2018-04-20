def divisibleSiete(x):
	if x % 7 == 0:
		return True

def multipleCinco(x):
	if x % 5 == 0:
		return True

for i in range (1500, 2700):
	if divisibleSiete(i) and multipleCinco(i):
		print(i)
	elif divisibleSiete(i):
		print(i)
	elif multipleCinco(i):
		print(i)