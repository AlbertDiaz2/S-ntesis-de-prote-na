#
# AUTORES: Albert Diaz, Nathalia Silvera.
# ULTIMA FECHA DE MODIFICACION: 06/06/2016.
# NOMBRE DEL ARCHIVO: ADNDoble.py
# DESCRIPCION: Clase para el objeto ADN doble.
#

from ADNSimple import ADNSimple
import sys

class ADNDoble:

    # Descripcion: Constructor de la clase ADNDoble.
    # Pre: True
    # Post: self.cadenadoble = []
    #       self.longitud = len(self.cadenadoble)

	def __init__(self, cadenasimple):
		self.cadenadoble = cadenasimple
		self.longitud = len(self.cadenadoble)

    # Descripcion: Funcion que convierte una cadena de adn simple en una
    #            cadena de adn doble.
    # Pre: cadenasimple != []
    # Post: Para todo i en self.cadenadoble se tiene que
    #       self.cadenadoble[i] == (['A','T'] or ['T','A'] or
    #                               ['C','G'] or ['G','C'])
    # retorna: cadena de adn doble.

	def zip(self):
		for i in range(0, self.longitud):
			if(self.cadenadoble[i] == 'A'):
				self.cadenadoble[i] = ['A','T']
			elif(self.cadenadoble[i] == 'T'):
				self.cadenadoble[i] = ['T','A']
			elif(self.cadenadoble[i] == 'C'):
				self.cadenadoble[i] = ['C','G']
			elif(self.cadenadoble[i] == 'G'):
				self.cadenadoble[i] = ['G','C']
		return self.cadenadoble

    # Descripcion: Funcion que separa una cadena de adn doble en dos 
    #              cadenas de adn simple.
    # Pre: cadenadoble != [] 
    # Post: para todo i en self.cadenadoble se tiene que 
    #       A contiene todos los self.cadenadoble[i][0] 
    #       B contiene todos los self.cadenadoble[i][1] 
    # retorna: dos cadenas de adn simple.

	def unzip(self):
		A = []
		B = []
		for i in range(0, self.longitud):
			A.append(self.cadenadoble[i][0])
			B.append(self.cadenadoble[i][1])
		return A,B

    # Descripcion: Calcula la longitud de self.cadenadoble.
    # Pre: True
    # Post: len(self.cadenadoble)
    # retorna: La longitud del arreglo self.cadenadoble

	def __len__(self):
		return len(self.cadenadoble)

    # Descripcion: Funcion que realiza la mitosis en una cadena de adn.
    # Pre: cadenadoble != []
    # Post: Se tiene una copia de la cadena original.
    # retorna: cadena de adn doble duplicada.

	def mitosis(self):
		UZ = self.unzip()
		C = UZ[0]
		D = UZ[1]
		C1 = self.zip(C)
		D1 = self.zip(D)
		return C1, D1

    # Descripcion: Busca en un ADN doble, si existe un trozo de su cadena
    #              que coincida con un ADN simple dado.
    # Parametros: subcadena: Arreglo que contiene ADN simple.
    # Pre: cadenadoble != [] and subcadena != []
    # Post: esta == True or esta == False
    # retorna: True o False.

	def buscar(self, subcadena):
		esta = False
		contador = 0
		for i in range(0, len(subcadena)):
			for j in range(0, self.longitud):
				print('i: ', i,'j: ', j)
				if(subcadena[i] == self.cadenadoble[j][0] or
				   subcadena[i] == self.cadenadoble[j][1]):
					contador += 1
					print('subcadena: ', subcadena[i], 'ADN: ',self.cadenadoble[j][0], self.cadenadoble[j][1])
					print(contador)
					break
		if(contador == len(subcadena)):
			print('si esta')
			print(contador)
			esta = True
			return esta
		print('no esta')
		return esta

    # Descripcion: Funcion que muestra en pantalla los elementos de la
    #              cadena de adn doble.
    # Pre: True
    # Post: Se muestran todos los elementos de la cadena de adn doble.

	def imprimir(self):
		A = []
		for i in range(0, self.longitud):
			A.append(''.join(self.cadenadoble[i]))
		print('Cadena Doble:',A)




