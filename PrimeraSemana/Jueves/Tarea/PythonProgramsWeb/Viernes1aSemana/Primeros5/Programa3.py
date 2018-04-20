from random import randint

def mayor(num):
	print("Que numero?")
	
	try:
		y = int(input())
	except Exception as e:
		return print("No es un numero el que introdujiste")
	if(num > y):
		return print("Si")
	else:
		return print("No")
	
	
def menor(num):
	print("Que numero?")
	try:
		y = int(input())
	except Exception as e:
		return print("No es un numero el que introdujiste")
	if(num < y):
		return print("Si")
	else:
		return print("No")


def adivino(num):
	print("Que numero es?")
	try:
		y = int(input())
	except Exception as e:
		print("No es un numero el que introdujiste")
	if(y == num):
		print("Correcto")
		exit(0)
	else:
		print("Fallaste")

x = randint(1, 9)
print(x)

print("Conjeturas aceptadas Mayor o Menor")

while True:
	print("Inserte su conjetura")
	conjetura = input()
	if conjetura == "Mayor":
		mayor(x);
	elif conjetura == "Menor":
		menor(x);
	else:
		print("Conjetura no valida")
	adivino(x)
