class Contar:
	def pares(objeto):
		contador = 0
		for i in objeto.numeros:
			if(i % 2 == 0):
				contador += 1
		return print(contador)

	def impares(objeto):
		contador = 0
		for i in objeto.numeros:
			if(i % 2 != 0):
				contador += 1
		return print(contador)

class Numeros:
	def __init__(self):
		self.nombre = "Arreglo 1"
		self.numeros = list()

	def anadirNumeros(self):
		for i in range (1, 10):
			self.numeros.append(i)

	def imprimirNumeros(self):
		print(self.numeros)

class Controladora():
	def main(self):
		uno = Numeros()
		uno.anadirNumeros()
		print('Numeros')
		uno.imprimirNumeros()
		print('Cantidad numeros pares')
		Contar.pares(uno)
		print('Cantidad numeros impares')
		Contar.impares(uno)

obj = Controladora()
obj.main()