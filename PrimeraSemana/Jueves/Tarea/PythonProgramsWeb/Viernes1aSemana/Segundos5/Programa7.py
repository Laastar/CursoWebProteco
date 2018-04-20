class Buscar:
  
  def __init__(self,list1):
    self.lista = list1

  def voltear(self):
      for i in self.lista:
        print(i,"   ",type(i))

lista= [1452, 11.23, 1 + 2j, True, 'w3resource', (0, -1), [5, 12], {"clase": 'V', 'section': 'A'}]
a=Buscar(lista)
a.voltear()
