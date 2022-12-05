#
# AUTORES: Albert Diaz, Nathalia Silvera.
# ULTIMA FECHA DE MODIFICACION: 07/06/2016.
# NOMBRE DEL ARCHIVO: Proteina.py
# DESCRIPCION: Clase para el objeto Proteina.
#

from ARNtb import ARNt
from ADNDoble import ADNDoble
from ADNSimple import ADNSimple

class Proteina:

    # Descripcion: Constructor de la clase Proteina.
    # Parametros: proteina: Arreglo que contiene una cadena de codones.
    # Pre: True
    # Post: self.proteina = proteina and 
    #       self.longitud = len(self.proteina)

	def __init__(self, proteina):
		self.proteina = proteina
		self.longitud = len(self.proteina)

    # Descripcion: Funcion que quita los arreglos vacios de la proteina.
    # Pre: self.loongitud != []
    # Post: El arrreglo D no contiene arreglos vacios.
    # retorna: Un arreglo de proteinas donde no esta presente el arreglo
    #          vacio ([]).

	def acomodar(self):
		C = []
		D = []
		for i in self.proteina:
			if(i != []):
				for j in range(0,len(i)):
					C.append(i[j])
				D.append(C)
				C = []
		return D

    # Descripcion: Traduce los codones de ARN en proteinas.
    # Pre: self.proteina != []
    # Post: Cada codon de ARN se traduce a su equivalente en proteina.
    # retorna: Un arreglo de proteinas.
		
	def transcribir(self):

		T = [['AUG','Met'], ['GCU','Ala'], ['GCC','Ala'], ['GCA','Ala'],
	         ['GCG','Ala'], ['CGU','Arg'], ['CGC','Arg'], ['CGA','Arg'], 
	         ['CGG','Arg'], ['AGA','Arg'], ['AGG','Arg'], ['AAU','Asn'], 
	         ['AAC','Asn'], ['GAU','Asp'], ['GAC','Asp'], ['UGU','Cys'], 
	         ['UGC','Cys'], ['CAA','Gln'], ['CAG','Gln'], ['GAA','Glu'], 
	         ['GAG','Glu'], ['GGU','Gly'], ['GGC','Gly'], ['GGA','Gly'], 
	         ['GGG','Gly'], ['CAU','His'], ['CAC','His'], ['AUU','Ile'], 
	         ['AUC','Ile'], ['AUA','Ile'], ['UUA','Leu'], ['UUG','Leu'], 
	         ['CUU','Leu'], ['CUC','Leu'], ['CUA','Leu'], ['CUG','Leu'], 
     	     ['AAA','Lys'], ['AAG','Lys'], ['UUU','Phe'], ['UUC','Phe'], 
             ['CCU','Pro'], ['CCC','Pro'], ['CCA','Pro'], ['CCG','Pro'], 
             ['UCU','Ser'], ['UCC','Ser'], ['UCA','Ser'], ['UCG','Ser'],
             ['AGU','Ser'], ['AGC','Ser'], ['ACU','Thr'], ['ACC','Thr'],
             ['ACA','Thr'], ['ACG','Thr'], ['UGG','Trp'], ['UAU','Tyr'],
             ['UAC','Tyr'], ['GUU','Val'], ['GUC','Val'], ['GUA','Val'],
             ['GUG','Val']]

		for k in self.proteina:
			for i in range(len(k)):
				for j in range(0, len(T)):
					if(k[i] == T[j][0]):
						k[i] = T[j][1]

		return self.proteina

    # Descripcion: Calcula la longitud de self.proteina.
    # Pre: True
    # Post: len(self.proteina)
    # retorna: La longitud del arreglo self.proteina

	def __len__(self):
		return len(self.proteina)

    # Descripcion: Ordena un arreglo en forma decreciente.
    # Parametros: A: Arreglo de proteinas con su frecuencia.
    # Pre: A != []
    # Post: para todo i en A se tiene que A[i] > A[i+1]

	def sort(self,A):
		self.buildHeap(A)
		for i in range(len(A)-1, 0, -1):
			A[0], A[i] = A[i], A[0]
			self.heapify(A, 0, i)
		print('Codones: ', A)
		for i in range(0, self.longitud):
			print('El codon ',self.proteina[i][0],
			      ' se repite ',self.proteina[i][1],' veces.')
		print('\n')

    # Descripcion: Crea un heap con el arreglo A.
    # Parametros: A: Arreglo de proteinas con su frecuencia.
    # Pre: A != []
    # Post: El arreglo A forma un max heap binario.

	def buildHeap(self,A):
		for i in range(len(A)//2-1, -1, -1):
			self.heapify(A,i,len(A))

    # Descripcion: Verifica la propiedad del heap.
    # Parametros:   A: Arreglo de proteinas con su frecuencia.
    #             idx: posicion del nodo padre en el heap.
    #               m: longitud del arreglo A.
    # Pre: A != [] and m == len(A)
    # Post: Se cumple que lon nodos hijos son menores que el nodo padre.

	def heapify(self, A, idx, m):
		largest = idx
		left = 2*idx+1
		right = 2*idx+2
		if(left < m and A[left][1] < A[idx][1]):
			largest = left
		if(right < m and A[right][1] < A[largest][1]):
			largest = right
		if(largest != idx):
			A[idx], A[largest] = A[largest], A[idx]
			self.heapify(A, largest, m)




