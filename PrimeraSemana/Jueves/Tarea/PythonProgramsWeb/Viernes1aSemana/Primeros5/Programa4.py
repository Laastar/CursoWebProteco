def imprimirIda():
	for i in range(1, 11):
		if i == 1:
			print("*")
		if i == 2:
			for j in range(1,i+1):
				print(">", end='')
			print("")
		if i == 3:
			for j in range(1,i+1):
				print("*", end='')
			print("")
		if i == 8:
			for j in range(1,i+1):
				print(">", end='')
			print("")
		if i == 10:
			for j in range(1,i+1):
				print("*", end='')
			print("")

def imprimirRegreso():
	for i in range(8, 0, -1):
		if i == 1:
			print("*")
		if i == 2:
			for j in range(1,i+1):
				print(">", end='')
			print("")
		if i == 3:
			for j in range(1,i+1):
				print("*", end='')
			print("")
		if i == 8:
			for j in range(1,i+1):
				print(">", end='')
			print("")

imprimirIda()
imprimirRegreso()