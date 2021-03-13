class Humano ():
	Piernas = True
	def __init__ (self, nombre):
		self.nombre = nombre
	def hablar(self):
		print ("HOLA SOY", self.nombre)

class Autos ():
	Ruedas = True
	def __init__(self, marca):
		self.marca = marca
	def tipo(self):
		print("Carro marca: ", self.marca)

Julio = Humano("Julio")
Julio.hablar()
print(Julio.Piernas)

Toyota = Autos("Mercedes")
print(Toyota.Ruedas)
Toyota.tipo()