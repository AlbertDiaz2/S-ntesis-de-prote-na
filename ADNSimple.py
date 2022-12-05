#
# AUTORES: Albert Diaz, Nathalia Silvera.
# ULTIMA FECHA DE MODIFICACION: 06/06/2016.
# NOMBRE DEL ARCHIVO: ADNSimple.py
# DESCRIPCION: Clase para el objeto ADN simple.
#

class ADNSimple:

    # Descripcion: Constructor de la clase ADNSimple.
    # Parametros: cadenasimple: Arreglo que contiene una cadena de adn
    #             simple.
    # Pre: True
    # Post: self.cadenasimple = cadenasimple and 
    #       self.longitud = len(cadenasimple)

	def __init__(self, cadenasimple):
		self.cadenasimple = cadenasimple
		self.longitud = len(cadenasimple)

    # Descripcion: Calcula la longitud de self.cadenasimple.
    # Pre: True
    # Post: len(self.cadenasimple)
    # retorna: La longitud del arreglo self.cadenasimple

	def __len__(self):
		return len(self.cadenasimple)

    # Descripcion: Funcion que determina el adn complemento de cadena
    #              simple.
    # Pre: cadenasimple != []
    # Post: Para todo i en A se tiene que
    #       A[i] == ('A' or 'T' or 'C' or 'G')
    # retorna: cadena complemento del arreglo cadenasimple.
	
	def complementar(self):
		A = []
		for i in range(0, self.longitud):
			if(self.cadenasimple[i] == 'A'):
				A.append('T')
			elif(self.cadenasimple[i] == 'T'):
				A.append('A')
			elif(self.cadenasimple[i] == 'G'):
				A.append('C')
			elif(self.cadenasimple[i] == 'C'):
				A.append('G')
		return A

    # Descripcion: Funcion que transcribe una secuencia de adn simple en
    #              arn.
    # Pre: cadenasimple != []
    # Post: Para todo i tal que A[i] == T se cambia por A[i] == U.
    # retorna: Un arreglo de arn.
    
	def transcribir(self):
		for i in range(0, self.longitud):
			if(self.cadenasimple[i] == 'T'):
				self.cadenasimple[i] = 'U'
		return self.cadenasimple




