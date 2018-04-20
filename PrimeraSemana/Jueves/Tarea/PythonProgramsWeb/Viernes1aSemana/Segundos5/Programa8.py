class Contar:
	def excepciones(objeto):
		print("[", end='')
		for i in objeto.numeros:
			if(i == 3):
				continue
			elif(i == 6):
				continue
			else:
				print(i, end=', ')
		print("]", end='')
		print("")

class Numeros:
	def __init__(self):
		self.nombre = "Arreglo 1"
		self.numeros = list()

	def anadirNumeros(self):
		for i in range (1, 9):
			self.numeros.append(i)

	def imprimirNumeros(self):
		print(self.numeros)

class Controladora():
	def main(self):
		uno = Numeros()
		uno.anadirNumeros()
		print('Numeros')
		uno.imprimirNumeros()
		print('Numeros sin excepciones')
		Contar.excepciones(uno)

obj = Controladora()
obj.main()