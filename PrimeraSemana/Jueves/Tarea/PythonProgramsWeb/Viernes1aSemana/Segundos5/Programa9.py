class Contar:
	def calcFactorial(objeto):
		if(objeto.numero == 0):
			return print("1")
		deFacto = 1
		for i in range (1, objeto.numero+1):
			deFacto = deFacto * i
		return print(deFacto)

class Numeros:
	def __init__(self):
		self.nombre = "Arreglo 1"
		self.numero = None

	def anadirNumeros(self):
		print("Inserta un numero")
		try:
			y = int(input())
		except Exception as e:
			return print("No es un numero el que introdujiste")
		self.numero = y

	def imprimirNumeros(self):
		print(self.numero)

class Controladora():
	def main(self):
		uno = Numeros()
		uno.anadirNumeros()
		print('Numero')
		uno.imprimirNumeros()
		print('Factorial')
		Contar.calcFactorial(uno)

obj = Controladora()
obj.main()