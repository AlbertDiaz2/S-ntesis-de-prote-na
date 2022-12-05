#
# AUTORES: Albert Diaz, Nathalia Silvera.
# ULTIMA FECHA DE MODIFICACION: 06/06/2016.
# NOMBRE DEL ARCHIVO: ARNtb.py
# DESCRIPCION: Clase para el objeto ARNt.
#

from ADNSimple import ADNSimple

class ARNt:

    # Descripcion: Constructor de la clase ARNt.
    # Parametros: cadenaArnt: Arreglo que contiene una cadena de arn.
    # Pre: True
    # Post: self.cadenaArnt = cadenaArnt and 
    #       self.longitud = len(cadenaArnt)

	def __init__(self, cadenaArnt):
		self.cadenaArnt = cadenaArnt
		self.longitud = len(cadenaArnt)

    # Descripcion: Funcion que toma una cadena de arn y forma
    #              codones.
    # Pre: True
    # Post: ARN contiene un arreglo de codones, o es un arreglo
    #       vacio. cadena_rota contiene la secuencia de ARN rota, o
    #       es un arreglo vacio.
    # retorna: Un arreglo que contiene el ARN basura y los codones.       
	
	def Traducir(self):
	
		ARN = []
		cadena_rota = []
		i_inicios = []
		paradas = 0
		a =0
		if(self.longitud < 3):
			return [ARN, cadena_rota]
		else:
			k = 0
			while(k < self.longitud-3):
				k = self.codon_inicio(k)
				i_inicios.append(k)
				A = self.codones(k,paradas)
				if(A != None):
					k = A[2]
					ARN.append(A[0])
					paradas = A[1]
			
			if(len(i_inicios) > paradas):
				if(ARN != []):
					del ARN[len(ARN)-1]
					for i in range(i_inicios[len(i_inicios)-1], self.longitud):
						cadena_rota.append(self.cadenaArnt[i])
				else:
					for i in range(i_inicios[len(i_inicios)-2], self.longitud):
						cadena_rota.append(self.cadenaArnt[i])

			return [ARN, cadena_rota]
	
    # Descripcion: Funcion que busca la primera aparicion de AUG.
    # Parametros: i: representa una posicion de la cadena de ARN.        
    # Pre: self.cadenaArnt != []
    # Post: variable que contiene la posicion siguiente de la G del
    #       codon AUG.
    # retorna: La posicion siguiente a donde se encuentre el codon
    #          AUG, o un valor mayor a la lonitud de la cadena de
    #          codones.  
	
	def codon_inicio(self,i):
		for j in range(i, self.longitud-2):
			if(self.cadenaArnt[j] == 'A' and 
			   self.cadenaArnt[j+1] == 'U' and 
			   self.cadenaArnt[j+2] == 'G'):
				return (j + 3)
		return(j + 3)
		
    # Descripcion: Funcion que va formando las cadenas de codones.
    # Parametros: i: representa una posicion de la cadena de ARN.
    #             p: reresenta el numero de veces que ha aparecido uno
    #                de los codones de paradas (UAA, UGA, UAG).
    # Pre: self.cadenaArnt != []
    # Post: sub contiene los codones formados luego del codon de inicio,
    #       o es un arreglo vacio. p guarda la cantidad de codones de 
    #       parada que se han encontrado en la cadena de arn. i+3 es la
    #       posicion que se encuentra luego del codon de parada.
    # retorna: Un arreglo que contiene: la cantidad de codones de parada
    #          encontrados, un arreglo con los codones formados o un
    #          arreglo vacio, y la posicion del elemento que se encuetra
    #          despues del codon de parada.

	def codones(self, i, p):
		sub = []
		m = p
		for i in range(i, self.longitud-2,3):
			
			if((self.cadenaArnt[i]=='U' and self.cadenaArnt[i+1]=='A'
			      and self.cadenaArnt[i+2]=='G') or 
		         (self.cadenaArnt[i]=='U' and self.cadenaArnt[i+1]=='G'
			      and self.cadenaArnt[i+2]=='A') or 
		         (self.cadenaArnt[i]=='U' and self.cadenaArnt[i+1]=='A'
			      and self.cadenaArnt[i+2]=='A')):
				return [sub, p+1, i + 3]
				
			elif((i+2) <= self.longitud-1):
				sub.append(''.join(self.cadenaArnt[i:i+3]))
				i += 3	
			
			if(i > self.longitud-1 or i+1 > self.longitud-1 or 
			   i+2 > self.longitud-1):
				return [sub, p, i]
	
    # Descripcion: Funcion que cuenta las veces que se repite un codon.
    # Parametros: codones: Arreglo que contiene codones.
    # Pre: self.proteina != []
    # Post: self.proteina tiene un arreglo con el total de veces que se
    #       repite cada codon de proteina.
    # retorna: Un arreglo de arreglos, donde cada subarreglo contiene un
    #          codon y la cantidad de veces que aparece.

	def Contador_codones(self, codones):

		T = [['AUG',0], ['GCU',0], ['GCC',0], ['GCA',0],
	         ['GCG',0], ['CGU',0], ['CGC',0], ['CGA',0], 
	         ['CGG',0], ['AGA',0], ['AGG',0], ['AAU',0], 
	         ['AAC',0], ['GAU',0], ['GAC',0], ['UGU',0], 
	         ['UGC',0], ['CAA',0], ['CAG',0], ['GAA',0], 
	         ['GAG',0], ['GGU',0], ['GGC',0], ['GGA',0], 
	         ['GGG',0], ['CAU',0], ['CAC',0], ['AUU',0], 
	         ['AUC',0], ['AUA',0], ['UUA',0], ['UUG',0], 
	         ['CUU',0], ['CUC',0], ['CUA',0], ['CUG',0], 
     	     ['AAA',0], ['AAG',0], ['UUU',0], ['UUC',0], 
             ['CCU',0], ['CCC',0], ['CCA',0], ['CCG',0], 
             ['UCU',0], ['UCC',0], ['UCA',0], ['UCG',0],
             ['AGU',0], ['AGC',0], ['ACU',0], ['ACC',0],
             ['ACA',0], ['ACG',0], ['UGG',0], ['UAU',0],
             ['UAC',0], ['GUU',0], ['GUC',0], ['GUA',0],
             ['GUG',0]]
        
		for i in range(0, len(codones)):
			if(codones[i] != []):
				for j in range(0,len(codones[i])):
					for k in range(0, len(T)):
						if(codones[i][j] == T[k][0]):
							T[k][1] = T[k][1]+1
							
		A = []
		for i in range(0, len(T)):
			if(T[i][1] != 0):
				A.append(T[i])
		return A

    # Descripcion: Funcion que retranscribe el ARN basura en ADN.
    # Parametros: A: Arreglo de Arn basura.        
    # Pre: self.cadenaArnt != []
    # Post: Para todo i en A se cambia A[i] = 'U' por 
    #       A[i] == ('T').
    # retorna: Arreglo traducido a ADN.

	def retranscribir(self,A):
		for i in range(0, len(A)):
			if(A[i] == 'U'):
				A[i] = 'T'
		return A
