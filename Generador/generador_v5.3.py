import random as rd
import math
import sys

I = []          # Lista de Bloques con gente a rescatar
J = []          # Lista de Refugios
K = []          # Lista de refugios PetFriendly (subconjunto de J)
d = {}          # Diccionario de distancias de la forma {(Bloque, Shelter): distancia}


class Block():
    def __init__(self, name, coordX, coordY, demand):
        self.name = name
        self.coordX = coordX
        self.coordY = coordY
        self.demand = demand

    def showInfo(self):
        print ("Name: "+self.name)
        print ("CoordX: "+str(self.coordX))
        print ("CoordY: "+str(self.coordY))
        print ("Demand: "+str(self.demand))

    def getName(self):
        return self.name

    def getCoordX (self):
        return self.coordX

    def getCoordY (self):
        return self.coordY
    
    def getDemand (self):
        return self.demand

    def setDemand (self, dem):
        self.demand = dem
        return
        
    def distanceToShelter(self, x, y):
        return int(math.sqrt(pow((self.coordX - x), 2) + pow((self.coordY - y), 2)))


class Shelter():
    def __init__(self, name, coordX, coordY, capacity):
        self.name = name
        self.coordX = coordX
        self.coordY = coordY
        self.capacity = capacity

    def showInfo(self):
        print ("Name: "+self.name)
        print ("CoordX: "+str(self.coordX))
        print ("CoordY: "+str(self.coordY))
        print ("Capacity: "+str(self.capacity))

    def getName(self):
        return self.name

    def getCoordX (self):
        return self.coordX

    def getCoordY (self):
        return self.coordY

    def setCapacity (self, capacidad):
        self.capacity = capacidad
        return

    def getCapacity (self):
        return self.capacity

# I
def generarBloques():
    for i in range(cantBloques):
        P = 'P'+str(i+1)
        P = Block (P, rd.randrange(1, 500), rd.randrange(1, 500), rd.randrange(25, 60))
        I.append(P)

# J
def generarRefugios():
    for i in range(cantRefugios):
        S = 'S'+str(i+1)
        S = Shelter (S, rd.randrange(1, 500), rd.randrange(1, 500), 0)
        J.append(S)

# K
def selectPetFriendlyShelters():
    cant = 0
    while (cant < cantRefPet):
        k = rd.choice(J)
        if k not in K:
            K.append(k)
            cant = cant + 1

# d
def obtenerDistancias():
     for i in I:
        for j in J:
            t = (i.getName(), j.getName())      # obtenemos la tupla (Bloque, Shelter)
            x = j.getCoordX()                   # Obtenemos la coordenada X del Shelter
            y = j.getCoordY()                   # Obtenemos la coordenada Y del Shelter
            dist = i.distanceToShelter(x, y)    # Se calcula la distancia desde el Bloque i al Shelter j
            d[t] = dist                         # Añadimos al diccionario {(Bloque, Shelter): distancia}

def generarCapacidades ():
    cantPxS = int(cantBloques/N) +1            # Cantidad de puntos por shelter
    print("cantPxS: " + str(cantPxS))
    shelterAsig = int(cantBloques/cantPxS) + 1
    i = 0
    j = 0
    z = 0

    for j in range(shelterAsig):
        dem = 0
        for i in range(cantPxS):
            if z < cantBloques :
                dem = dem + I[z].getDemand()
                z = z + 1
                i = i + 1
            else: break

        J[j].setCapacity(dem)
        j = j + 1
    
    k = cantRefugios - shelterAsig - 1

    while (k < cantRefugios):
        cap = rd.randrange(80, 120)
        J[k].setCapacity(cap)
        k = k + 1


def demandaTotal():
    i = 0
    suma = 0
    for i in range(len(I)):
        s = I[i].getDemand()
        suma = suma + s
        i = i + 1
    return suma
    
def capacidadTotal():
    i = 0
    suma = 0
    for i in range(len(J)):
        s = J[i].getCapacity()
        suma = suma + s
        i = i + 1
    return suma


def escribirArchivo ():
    nombre_archivo = 'instancia_v5.3' + '_I' + str(cantBloques) + '_J' + str(cantRefugios) + '_K' + str(cantRefPet) + '_N' + str(N) + '_P' + str(per) + '_s' + str(s) + '.dat'

    f = open (nombre_archivo,'w')

    f.write("set I  :=")
    i = 0
    for i in range(len(I)):
        f.write(("  " + I[i].getName()))
        i = i + 1
    f.write(" ;") 

    f.write("\n")

    f.write("set J  :=")
    i = 0
    for i in range(len(J)):
        f.write(("  " + J[i].getName()))
        i = i + 1
    f.write(" ;") 

    f.write("\n")

    f.write("set K  :=")
    i = 0
    for i in range(len(K)):
        f.write(("  " + K[i].getName()))
        i = i + 1
    f.write(" ;") 

    f.write("\n\n")

    f.write("param N := " + str(N) + " ;\n\n")

    f.write("param C := \n")
    i = 0
    for i in range(len(J)):
        f.write((J[i].getName() + "  " + str(J[i].getCapacity())) + "\n")
        i = i + 1
    f.write(" ; \n\n")

    f.write("param P := \n")
    i = 0
    for i in range(len(I)):
        f.write((I[i].getName() + "  " + str(I[i].getDemand())) + "\n")
        i = i + 1
    f.write(" ; \n\n")

    f.write("param d[*,*] :")
    i = 0
    for i in range(len(J)):
        f.write(("  " + J[i].getName()))
        i = i + 1
    f.write("   :=\n")  

    for i in I:
        f.write(i.getName() + " ")
        for j in J:
            distance = d.get( (str(i.getName()), str(j.getName())) )
            f.write(str(distance) + "   ")
        f.write("\n")
    f.write(" ;\n\n")

    f.write("param: coordX  coordY  := \n")
    for j in J:
        jx = j.getCoordX()
        jy = j.getCoordY()
        f.write(str(j.getName()) + "   " + str(jx) + "  " + str(jy) + "\n")
    for i in I:
        ix = i.getCoordX()
        iy = i.getCoordY()
        f.write(str(i.getName()) + "   " + str(ix) + "  " + str(iy) + "\n")
    f.write(" ;")

    f.close()


def verificacionDemandaCapacidad ():
    if (demandaTotal() <= capacidadTotal()): 
        return True
    else: 
        return False



def main ():

    global cantBloques, cantRefugios, cantRefPet, N, s, sem, per
    cantBloques = int(sys.argv[1])
    cantRefugios = int(sys.argv[2])
    N = int(sys.argv[3])
    per = float(sys.argv[4])
    s = int(sys.argv[5])
    sem = rd.seed(s)

    cantRefPet = int(N*per)

    #if cantRefPet >= N:
    #    cantRefPet = int(0.5*N)

    generarBloques()
    generarRefugios()
    generarCapacidades()

    selectPetFriendlyShelters()
    obtenerDistancias()

    escribirArchivo()


main()
