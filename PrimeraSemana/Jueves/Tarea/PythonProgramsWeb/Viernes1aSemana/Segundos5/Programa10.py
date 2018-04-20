class Contar:
	def quitarABC(objeto):
		objeto.cadena = objeto.cadena.replace("a", "")
		objeto.cadena = objeto.cadena.replace("A", "")
		objeto.cadena = objeto.cadena.replace("e", "")
		objeto.cadena = objeto.cadena.replace("E", "")
		objeto.cadena = objeto.cadena.replace("i", "")
		objeto.cadena = objeto.cadena.replace("I", "")
		objeto.cadena = objeto.cadena.replace("o", "")
		objeto.cadena = objeto.cadena.replace("O", "")
		objeto.cadena = objeto.cadena.replace("u", "")
		objeto.cadena = objeto.cadena.replace("U", "")
		return print(objeto.cadena)
		
class Cadena:
	def __init__(self):
		self.nombre = "Arreglo 1"
		self.cadena = None

	def anadirCadena(self):
		print("Inserta una cadena")
		y = input()
		self.cadena = y

	def imprimirCadena(self):
		print(self.cadena)

class Controladora():
	def main(self):
		uno = Cadena()
		uno.anadirCadena()
		print('Cadena')
		uno.imprimirCadena()
		print('Cadena modificada')
		Contar.quitarABC(uno)

obj = Controladora()
obj.main()