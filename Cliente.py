#
# AUTORES: Albert Diaz, Nathalia Silvera.
# ULTIMA FECHA DE MODIFICACION: 07/06/2016.
# NOMBRE DEL ARCHIVO: Cliente.py
# DESCRIPCION: Cliente para el proceso de traduccion del adn en proteina.
#

import sys
from ARNtb import ARNt
from ADNDoble import ADNDoble
from ADNSimple import ADNSimple
from Proteina import Proteina
from Contenedor import Contenedoras

# Descripcion : Funcion que lee el archivo txt con el caso
# 				de prueba.
# Parametro: archivo: Archivo .txt con los casos de prueba.
# Pre: True
# Post: Lectura por linea del archivo txt almacenado 
#		en arreglos.
# retorna: Un arreglo con cada caso de prueba como un sub arreglo.

def lectura_archivo(archivo):
    lista = []
    with open(archivo,'r') as f:
        for line in f:
            ADN = line.rstrip()
            T = list(ADN)
            lista.append(T)
    return lista

####################
####################
#      Main        #
####################
####################
print('\n')
print('Iniciando el cliente...')
print('\n')

# Inicio del cliente.
if __name__ == "__main__":
	
    # Lectura del archivo .txt
    secuencias = lectura_archivo(sys.argv[1])
    secuencias2 = lectura_archivo(sys.argv[1])

    #Creando las cadenas de ADN doble para luego escribirlas en el 
    #archivo "AdnDoble.txt".
    print('Escribiendo cadenas de ADN Doble en AdnDoble.txt...')
    print('\n')
    AdnDoble = open('AdnDoble.txt','w')
    for i in range(0, len(secuencias)):
        a = ADNDoble(secuencias[i])
        c = a.zip()
        s = ''
        for j in range(0,len(a)):
            s += '(' + str(''.join(c[j])) + ')' + ' '
        AdnDoble.write(s + '\n')
    AdnDoble.close()

    # Creando los objetos adn simple y traduciendolos a arn
    # Se escribe el arn en el archivo "Arnt.txt".
    print('Traduciendo el adn simple en arn...')
    print('Escribiendo las cadenas de arn en Arnt.txt...')
    print('\n')
    ARN = []
    Arnt = open('Arnt.txt','w')
    for i in range(0, len(secuencias2)):
        adnsimple = ADNSimple(secuencias2[i])
        ARN.append(adnsimple.transcribir())
        x = ARN[i]
        v = ''
        for j in range(0,len(adnsimple)):
            v += str(x[j]) + ' '
        Arnt.write(v + '\n')
    Arnt.close()
	
    # Creando los objetos arn para formar los codones.
    print('Traduciendo las cadenas en codones...')
    print('Separando la basura...')
    print('\n')
    Codones = []
    Conteo = []
    Basura = []
    for i in range(0, len(ARN)):
        arn = ARNt(ARN[i])
        codon = arn.Traducir()
        Basura.append(arn.retranscribir(codon[1]))
        Conteo.append(arn.Contador_codones(codon[0]))
        Codones.append(codon[0])

    # Creando un objeto proteina con los codones y su frecuencia.
    print('Contando la frecuencia de los codones...')
    print('\n')
    for i in range(0, len(Conteo)):
        frecuencia = Proteina(Conteo[i])
        frecuencia.sort(frecuencia.proteina)

    # Creando un objeto Proteina para traducir secuencias de codones.
    print('Procediendo a traducir las secuencias de codones...')
    print('\n')
    Sec_proteinas = []
    for i in range(0, len(Codones)):
        proteina = Proteina(Codones[i])
        proteina.transcribir()
        Sec_proteinas.append(proteina.acomodar())
		
    # Creando un objeto Contenedor para ordenar las secuencias de 
    # proteinas.
    print('Ordenando las secuencias de codones...')
    print('\n')
    for i in range(0, len(Sec_proteinas)):
        contenedor = Contenedoras(Sec_proteinas[i])
        resultado = contenedor.ordenarquick()
        print(resultado)
    print('\n')
	
    # Creando un objeto Contenedor para ordenar la basura.
    print('Ordenando las cadenas rotas de ADN...')
    print('Escribiendo el ADN Basura en AdnBasura.txt...')
    print('\n')
    AdnBasura = open('AdnBasura.txt','w')
    Residuos = []
    for i in range(0, len(Basura)):
        if(Basura[i] != []):
            Residuos.append(Basura[i])
    Contenedor2 = Contenedoras(Residuos)
    Residuos = Contenedor2.ordenarmerge()
    y = ''
    for j in range(0,len(Residuos)):
        for i in range(0, len(Residuos[j])):
            y += str(Residuos[j][i]) + ' '
        AdnBasura.write(y + '\n')
        y = ''
    AdnBasura.close()

