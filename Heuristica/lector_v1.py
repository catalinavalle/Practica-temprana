import math

global I, J, d

I = []          # Lista de Bloques con gente a rescatar
J = []          # Lista de Refugios
d = {}          # Diccionario de distancias de la forma {(Bloque, Shelter): distancia}

class Block():
    def __init__(self, name, coordX, coordY, demand):
        self.name = name
        self.coordX = coordX
        self.coordY = coordY
        self.demand = demand

    def showInfo(self):
        print("\n")
        print ("Name: "+self.name)
        print ("CoordX: "+str(self.coordX))
        print ("CoordY: "+str(self.coordY))
        print ("Demand: "+str(self.demand))


    def distanceToShelter(self, x, y):
        return int(math.sqrt(pow((self.coordX - x), 2) + pow((self.coordY - y), 2)))

    def getName(self):
        return self.name

    def getCoordX (self):
        return self.coordX

    def getCoordY (self):
        return self.coordY
    
    def getDemand (self):
        return self.demand
    
    def setName (self, name):
        self.name = name
        return
    
    def setCoordX (self, x):
        self.coordX = x
        return
    
    def setCoordY (self, y):
        self.coordY = y
        return
    
    def setDemand (self, dem):
        self.demand = dem
        return
        

class Shelter():
    def __init__(self, name, coordX, coordY, capacity, tipo):
        self.name = name
        self.coordX = coordX
        self.coordY = coordY
        self.capacity = capacity
        self.tipo = tipo

    def showInfo(self):
        print("\n")
        print ("Name: "+self.name)
        print ("CoordX: "+str(self.coordX))
        print ("CoordY: "+str(self.coordY))
        print ("Capacity: "+str(self.capacity))
        print ("Type: "+str(self.tipo))

    def getName(self):
        return self.name

    def getCoordX (self):
        return self.coordX

    def getCoordY (self):
        return self.coordY
    
    def getCapacity (self):
        return self.capacity
    
    def getType (self):
        return self.tipo

    def setName (self, name):
        self.name = name
        return

    def setCoordX (self, x):
        self.coordX = x
        return

    def setCoordY (self, y):
        self.coordY = y
        return

    def setCapacity (self, cap):
        self.capacity = cap
        return

    def setType (self, tipo):
        self.tipo = tipo


def obtenerBloques(linea):
    bloques = " ".join(linea.split(" ")[5:])
    bloquesList = bloques.split()

    for i in range(len(bloquesList)):
        b = Block (bloquesList[i], 0, 0, 0)
        I.append(b)
        i = i + 1

    I.remove(I[-1])

    return

def obtenerRefugios(linea):
    refugios = " ".join(linea.split(" ")[5:])
    refugiosList = refugios.split()

    for j in range(len(refugiosList)):
        s = Shelter (refugiosList[j], 0, 0, 0, 'notPetFriendly')
        J.append(s)
        j = j + 1

    J.remove(J[-1])

    return

def obtenerPetFriendlyShelters(linea):
    petFriendly = " ".join(linea.split(" ")[5:])
    petFriendlyList = petFriendly.split()

    for j in range(len(J)):
        if (J[j].getName() in petFriendlyList):
            J[j].setType('PetFriendly')

    return

def obtenerN(linea):
    global N
    n = " ".join(linea.split(" ")[3:])
    N = int(n[:-2])
    return

def obtenerCapacidades():
    capList = []
    i = linea
    cap = ""
    while (';' not in cap):
        cap = lineas[i]
        capList.append(cap)
        i = i + 1

    capList.remove(capList[-1])

    for j in range(len(J)):
        ShelCap = capList[j].split()
        J[j].setCapacity(int(ShelCap[1]))


    return i

def obtenerDemandas():
    demList = []
    i = linea
    dem = ""
    while (';' not in dem):
        dem = lineas[i]
        demList.append(dem)
        i = i + 1

    demList.remove(demList[-1])

    for j in range(len(I)):
        BloDem = demList[j].split()
        I[j].setDemand(int(BloDem[1]))

    return i

def obtenerDistancias():
    distList = []
    i = linea
    dist = ""
    while (';' not in dist):
        dist = lineas[i]
        distList.append(dist)
        i = i + 1

    distList.remove(distList[-1])

    for j in range (len(I)):
        distShel = distList[j].split()
        for z in range(len(J)):
            t = (I[j].getName(), J[z].getName())
            dist = distShel[z+1]
            d[t] = int(dist)

    return i

def obtenerCoordenadas():
    coordList = []
    i = linea
    coord = ""
    while (';' not in coord):
        coord = lineas[i]
        coordList.append(coord)
        i = i + 1

    coordList.remove(coordList[-1])

    for j in range (len(J)):
        coords = coordList[j].split()
        J[j].setCoordX(int(coords[1]))
        J[j].setCoordY(int(coords[2]))

    z = len(J)

    k = 0
    while (z < (len(J)+len(I))):
        coords = coordList[z].split()
        I[k].setCoordX(int(coords[1]))
        I[k].setCoordY(int(coords[2]))
        k = k + 1
        z = z + 1

    return


def reader_main (instancia):

    global lineas, f, linea

    f = open (instancia,'r')

    lineas = f.readlines()

    obtenerBloques(lineas[0])
    obtenerRefugios(lineas[1])
    obtenerPetFriendlyShelters(lineas[2])
    obtenerN(lineas[4])

    linea = 7
    linea = obtenerCapacidades() + 2
    linea = obtenerDemandas() + 2
    linea = obtenerDistancias() + 2

    obtenerCoordenadas()

    f.close()

   

    return I, J, d, N


