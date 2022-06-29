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
            print("\n" + str(shelter.getName()) + ": ")
            for bloque in bloques:
                print("- " + bloque.getName())

        return

    def noAsignados (self):
        shelters = self.Shelters
        asignados = self.sheltersAsignados
        s = set(shelters)
        a = set(asignados)
        return list(s - a)


def calcularCapacidadUtilizada (bloquesList):  # Recibe una lista de bloques y calcula la demanda total de estos
    s = 0
    suma = 0
    
    for i in range(len(bloquesList)):
        s = int(bloquesList[i].getDemand())
        suma = suma + s

    return suma    

def crearSolucionAleatoria ():

    bloques_temp = list(I) # Lista temporal de bloques
    refugios_temp = list(J)
    
    sheltersAsignados = []
    solved = {}   # diccionario {refugio:[bloques]}

    for j in J:
        solved.setdefault(j, [])        # agregamos todos los Shelters al diccionario, cada uno relacionado a una lista vacia que luego serán los bloques asignados al respectivo shelter


    i = 0

    while (((len(bloques_temp) != 0))):     # Mientras la cantidad de refugios asignados es menor a la cantidad de refugios a utilizar
        
        bloque = rd.choice(bloques_temp)                    # el bloque a utilizar será el que tome la posicion i de la lista temporal de bloques
        agregado = False  
         
        #print("\nit " + str(i))
        #i = i + 1

        refugio = rd.choice(refugios_temp)                    # el refugio a utilizar será el que tome la posicion del numero obtenido anteriormente
        
        #print("Refugio: " + refugio.getName() + "  Zona: " + bloque.getName())


        if (len(solved.get(refugio)) == 0 and len(sheltersAsignados) < n):         # Si no hay bloques asignados al refugio, este es agregado a la lista de refugios asignados                 
            
            sheltersAsignados.append(refugio)
            solved[refugio].append(bloque)     
            bloques_temp.remove(bloque)  
            agregado = True
       
        else:
            
            for shelter in sheltersAsignados:
                
                cap_temp = calcularCapacidadUtilizada(solved.get(shelter)) + bloque.getDemand()

                if (cap_temp <= shelter.getCapacity() and agregado == False):  

                    solved[shelter].append(bloque)  # agregamos el bloque a la lista asociada al shelter en el dicionario solucion
                    agregado = True
                    bloques_temp.remove(bloque)                 # y eliminamos el bloque de la lista temporal de bloques
            
            if (agregado == False and len(sheltersAsignados) < n):
                
                s = set(J)
                a = set(sheltersAsignados)

                noAsignados = list(s-a)
                
                for ref in noAsignados:
                    
                    if (ref.getCapacity() >= bloque.getDemand() and agregado == False):
                        
                        solved[ref].append(bloque)
                        sheltersAsignados.append(ref)
                        bloques_temp.remove(bloque) 
                        agregado = True
            
            elif (agregado == False and len(sheltersAsignados) == n):
                return False
            

        solucion.setSolucion(solved)
        #solucion.mostrar_solucion()

    solucion.setSolucion (solved)   
    solucion.setSheltersAsignados (sheltersAsignados)
    dist = solucion.calcularDistanciaTotal()    
    solucion.setTotalDistance(dist)    

    return True


def main ():

    flag = False

    while (flag == False):
        flag = crearSolucionAleatoria()

    else:
        return



def const_solucion_main (i, j, N, D):
    global I, J, n, d, solucion

    I = i
    J = j
    n = N
    d = D

    solucion = Solucion(I, J, n, d, 0, 0, [])

    main()

    return solucion

