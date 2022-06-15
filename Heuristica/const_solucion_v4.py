# solucion_v4: encuentra solucion aleatoria verificando la capacidad de cada refugio y respetando la cantidad de refugios a utilizar. Calcula la distancia recorrida. Todo esto bajo la clase Solucion cuyos atributos son refugios[], bloques[], refugiosUtilizados[], n, d, distanciaTotal
# tenemos dos main, uno mostrando detalladamente el proceso y uno sin mostrar el proceso, la ejecucion de cada uno se define por consola (0 para no mostrar el procedimiento, otro valor para si mostrarlo)
# el orden de refugios es alatorio, y los bloques van por orden

import random as rd

class Solucion ():
    def __init__(self, Blocks, Shelters, n, distances, solucion, totalDistance, sheltersAsignados):
        self.Blocks = Blocks
        self.Shelters = Shelters
        self.n = n
        self.distances = distances
        self.solucion = solucion
        self.totalDistance = totalDistance
        self.sheltersAsignados = sheltersAsignados

    def getShelters (self):
        return self.Shelters

    def getBlocks (self):
        return self.Blocks

    def getN (self):
        return self.N

    def getDistances (self):
        return self.distances

    def getSolucion (self):
        return self.solucion

    def getTotalDistance (self):
        return self.totalDistance

    def getSheltersAsignados (self):
        return self.sheltersAsignados
    
    def setShelters (self, shelters):
        self.Shelters = shelters
        return 

    def setBlocks (self, blocks):
        self.Blocks = blocks
        return 

    def setN (self, N):
        self.n = N
        return 

    def setDistances (self, d):
        self.distances = d
        return 

    def setSolucion (self, sol):
        self.solucion = sol
        return

    def setTotalDistance (self, totalDist):
        self.totalDistance = totalDist
        return 

    def setSheltersAsignados (self, SheltersAsignados):
        self.sheltersAsignados = SheltersAsignados
        return

    def calcularDistanciaTotal(self):
        # solucion = {'S01':[objetos]}
        distanciaTotal = 0
        sol = self.solucion
        for shelter in sol:
            bloques = sol.get(shelter)
            for bloque in bloques:
                dist = d.get((bloque.getName(), shelter.getName()))
                distanciaTotal = distanciaTotal + dist

        return distanciaTotal*2         # se multiplica por dos porque es ida y vuelta

    def mostrar_solucion (self):
        sol = self.solucion
        for shelter in sol:
            bloques = sol.get(shelter)
            print("\n" + str(shelter) + ": ")
            for bloque in bloques:
                print("- " + bloque.getName())

        return


def calcularCapacidadUtilizada (bloquesList):  # Recibe una lista de bloques y calcula la demanda total de estos
    s = 0
    suma = 0
    
    for i in range(len(bloquesList)):
        s = int(bloquesList[i].getDemand())
        suma = suma + s

    return suma    

def crearSolucionAleatoria ():
    bloques_temp = I # Lista temporal de bloques
    sheltersAsignados = []
    solucion = {}   # diccionario {refugio:[bloques]}

    for j in J:
        solucion.setdefault(j, [])        # agregamos todos los Shelters al diccionario, cada uno relacionado a una lista vacia que luego serán los bloques asignados al respectivo shelter

    while ((len(sheltersAsignados) < n) and ((len(bloques_temp) != 0))):     # Mientras la cantidad de refugios asignados es menor a la cantidad de refugios a utilizar
        randRefugio = rd.randrange(0, len(J)-1)     # se obtiene un numero al azar entre 0 y la cantidad refugios en la lista de refugios
        refugio = J[randRefugio]                    # el refugio a utilizar será el que tome la posicion del numero obtenido anteriormente

        bloque = bloques_temp[-1]                    # el bloque a utilizar será el que tome la posicion i de la lista temporal de bloques
        
        cap_temp = calcularCapacidadUtilizada(solucion.get(refugio)) + bloque.getDemand()
        
        if (cap_temp <= refugio.getCapacity()): # mientras la capacidad utilizada sea menor o igual a la capacidad del shelter
   
            if (len(solucion.get(refugio)) == 0):         # Si no hay bloques asignados al refugio, este es agregado a la lista de refugios asignados                 
                sheltersAsignados.append(refugio)
                cap_temp = 0

            if (mostrar_procedimiento != 0): print ("Revisando shelter " + str(refugio.getName()) + " y " + str(bloque.getName()))
   
            
            solucion[refugio].append(bloque)  # agregamos el bloque a la lista asociada al shelter en el dicionario solucion
            
            bloques_temp.remove(bloque)                 # y eliminamos el bloque de la lista temporal de bloques

            

    return solucion, sheltersAsignados


def solution_main_print (I, J, n, d) :

    solucion = Solucion(I, J, 4, d, 0, 0, [])
    print ("Objeto solucion creado... ")

    print ("Obteniendo solucion factible... ")
    sol, sheltersAsignados = crearSolucionAleatoria()
    print ("Ya tenemos una solucion factible...")

    solucion.setSolucion (sol)   
    solucion.setSheltersAsignados (sheltersAsignados)
    dist = solucion.calcularDistanciaTotal()     # se calcula la distacia recorrida en esa solucion
    solucion.setTotalDistance(dist)

    return solucion


def solution_main (I, J, n, d) :
    solucion = Solucion(I, J, 4, d, 0, 0, [])

    sol, sheltersAsignados = crearSolucionAleatoria()
    solucion.setSolucion (sol)   
    solucion.setSheltersAsignados (sheltersAsignados)
    dist = solucion.calcularDistanciaTotal()     # se calcula la distacia recorrida en esa solucion
    solucion.setTotalDistance(dist)

    return solucion


def const_solucion_main (mostrar, i, j, N, D):
    global mostrar_procedimiento, I, J, n, d

    mostrar_procedimiento = mostrar
    I = i
    J = j
    n = N
    d = D

    if (mostrar_procedimiento == 0):   
        solucion = solution_main (I, J, n, d)
    else:
        solucion = solution_main_print (I, J, n, d)

    return solucion