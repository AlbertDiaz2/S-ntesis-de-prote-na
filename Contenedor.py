#
# AUTORES: Albert Diaz, Nathalia Silvera.
# ULTIMA FECHA DE MODIFICACION: 07/06/2016.
# NOMBRE DEL ARCHIVO: Contenedor.py
# DESCRIPCION: Clase para el objeto Contenedoras.
#

from ARNtb import ARNt
from ADNDoble import ADNDoble
from ADNSimple import ADNSimple
from Proteina import Proteina

class Contenedoras:

    # Descripcion: Constructor de la clase Proteina.
    # Parametros: contenedor: Arreglo de proteinas.
    # Pre: True
    # Post: self.c = contenedor and 
    #       self.largo = len(self.c)

    def __init__(self, contenedor):
        self.c = contenedor
        self.largo = len(self.c)

    # Descripcion: Calcula la longitud de self.c.
    # Pre: True
    # Post: len(self.c)
    # retorna: La longitud del arreglo self.c

    def __len__(self):
        return len(self.c)

    # Descripcion: Particiona el arreglo original en dos, quienes son
    #            menores o igual al pivote a la izquirda, los que son
    #            mayores al pivote a la derecha, y el pivote en el medio
    # Parametros: A: Arreglo de secuencias de proteinas.
    #             p: Posicion de la primera secuencia de proteina.
    #             r: posicion de la ultima secuencia de proteina.
    # Pre: A != []
    # Post: la posicion i+1 representa el elemento pivote.
    # retorna: La posicion del pivote

    def Partition(self, A, p, r):
        x = len(A[r])
        Y = A[r]
        i = p - 1
        for j in range(p, r):
            if(len(A[j]) < x):
                i += 1
                A[i], A[j] = A[j], A[i]
            elif(len(A[j]) == x):
                for k in range(x):
                    if(A[j][k] < Y[k]):
                        i += 1
                        A[i], A[j] = A[j], A[i]
                        break
        A[i+1], A[r] = A[r], A[i+1]
        return i+1

    # Descripcion: Funcion que busca los elementos necesarios para hacer
    #            ordenamiento por quicksort.
    # Pre: self.c != []
    # Post: para todo i en A se tiene que A[i] < A[i+1].
    # retorna: Arreglo A ordenado de menor a mayor.

    def ordenarquick(self):
        p = 0
        A = self.c
        r = len(A)-1
        self.quicksort(A,p,r)
        return A

    # Descripcion: Metodo de ordenamiento por quicksort.
    # Parametros: A: Arreglo de secuencias de proteinas.
    #             p: Posicion de la primera secuencia de proteina.
    #             r: posicion de la ultima secuencia de proteina.
    # Pre: A != []
    # Post: para todo i en A se tiene que A[i] < A[i+1].

    def quicksort(self, A, p, r):
        if(p < r):
            q = self.Partition(A, p, r)
            self.quicksort(A, p, q-1)
            self.quicksort(A, q+1, r)

    # Descripcion: Funcion que busca los elementos necesarios para hacer
    #            ordenamiento por mergesort.
    # Pre: self.c != []
    # Post: para todo i en A se tiene que A[i] < A[i+1].
    # retorna: Arreglo A ordenado de menor a mayor.

    def ordenarmerge(self):
        A = self.c
        p = 0
        r = len(A)-1
        self.mergesort(A, p, r)
        return A

    # Descripcion: Rutina merge, ordena los subarreglos.
    # Parametros: seq: Arreglo de secuencias de proteinas.
    #               p: Primera posicion del arreglo seq.
    #               q: posicion media del arreglo inicial.
    #               r: Ultima posicion del arreglo seq.
    # Pre: A != []
    # Post: para todo i en A se tiene que A[i] < A[i+1].

    def merge(self,seq,p,q,r):
        n1 = q - p + 1
        n2 = r - q
        L , R = [None] * (n1) , [None] * (n2)
        i , j = 0 , 0
        for i in range(n1):
            L[i] = seq[p + i]
        for i in range(0, len(L)):
            for j in range(0, len(L[i])):
                L[i][j] = ord(L[i][j])
        for j in range(n2):
            R[j] = seq[q + j + 1]
        for i in range(0, len(R)):
            for j in range(0, len(R[i])):
                R[i][j] = ord(R[i][j])
        L.append([9999])
        R.append([9999])
        i , j , k = 0 , 0 , p
        while k <= r:
            if(L[i] <= R[j]):
                for m in range(0, len(L[i])):
                    L[i][m] = chr(L[i][m])
                seq[k] = L[i]
                i = i + 1
            else:
                for n in range(0, len(R[j])):
                    R[j][n] = chr(R[j][n])
                seq[k] = R[j]
                j = j + 1
            k += 1

    # Descripcion: Metodo de ordenamiento por mergesort.
    # Parametros: seq: Arreglo de secuencias de proteinas.
    #               p: Primera posicion del arreglo seq.
    #               r: Ultima posicion del arreglo seq.
    # Pre: seq != []
    # Post: para todo i en A se tiene que A[i] < A[i+1].
    
    def mergesort(self, seq , p , r):
        if p < r:
            q = (p + r) // 2
            self.mergesort(seq , p , q)
            self.mergesort(seq , q + 1 , r)
            self.merge(seq , p , q , r)
