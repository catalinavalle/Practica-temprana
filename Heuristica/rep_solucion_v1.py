# HAY QUE EJECUTAR VARIAS VECES YA QUE EN INSTANCIAS APRETADAS SE ALCANZA LA RECURSIVIAD MAXIMA PERMITIDA.

from lector_v1 import main
from const_solucion_v4 import const_solucion_main
from const_solucion_v4 import calcularCapacidadUtilizada
from const_solucion_v4 import Solucion

import random as rd
import sys


instancia = str(sys.argv[1])
#s = int(sys.argv[2])
#rd.seed(s)

I, J, d, n = main(instancia)


def obtenerLejanos (asignados, solved):

    bloques_lejanos = []
    temp = solved.copy()

    for shelter in asignados:              # se revisan todos los shelters asignados
        bloques = temp.get(shelter)     # se obtiene la lista de bloques asignados en el shelter   
        bloque_lejano_distance = 0

        for bloque in bloques:          # Se busca el bloque mas lejano al shelter
            current_dist = d.get((bloque.getName(), shelter.getName()))

            if (current_dist > bloque_lejano_distance):
                bloque_lejano_distance = current_dist
                bloque_mas_lejano = bloque
        
        temp.get(shelter).remove(bloque_mas_lejano)     # elimina el bloque del shelter
        bloques_lejanos.append(bloque_mas_lejano)         # agrega el bloque a la lista de lejanos
    
    return bloques_lejanos, temp


def reordenar_lista(lista):
    temp_lista = list(lista)
    lista_reordenada = []
    for i in range(len(temp_lista)):
        element = rd.choice(temp_lista)
        lista_reordenada.append(element)
        temp_lista.remove(element)
    return(lista_reordenada)


def asignar_shelter (lejanos, asignados, solved):

    for refugio in asignados:

        for bloque in lejanos:

            capacidad_temp = calcularCapacidadUtilizada(solved.get(refugio)) + bloque.getDemand()   # checamos la capacidad utilizada en el refugio
            capacidad_refugio = refugio.getCapacity()                                               # checamos la capacidad del refugio

            if( capacidad_temp <= capacidad_refugio):  # si entra, lo agregamos

                solved[refugio].append(bloque)
                lejanos.remove(bloque)                     # se elimina el bloque de la lista de lejanos

    if (len(lejanos) == 0):
        return solved
    else:
        return False


def reasignar_recursive (bloques_lejanos, sheltersAsignados, temp_solved):

    solved = asignar_shelter (bloques_lejanos, sheltersAsignados, temp_solved)

    if (solved == False):
        reasignar_recursive(bloques_lejanos, sheltersAsignados, temp_solved)
        return
    else:
        return solved



def obtenerVecinos(solution):

    lista_vecinos = list([])

    sheltersAsignados = list(solution.getSheltersAsignados())
    cantidad_vecinos = len(sheltersAsignados) 

    temp_solution_solved = solution.getSolucion().copy()

    temp_solved = {}

    # OBTENEMOS LOS BLOQUES MÁS LEJANOS DE CADA REFUGIO EN UNA LISTA Y LOS ELIMINAMOS DEL REFUGIO AL QUE FUE ASIGNADO

    bloques_lejanos, temp_solved = obtenerLejanos(sheltersAsignados, temp_solution_solved)

    """
     for shelter in temp_solved:
        bloques = temp_solved.get(shelter)
        print("\n" + str(shelter.getName()) + ": ")
        for bloque in bloques:
            print("- " + bloque.getName())   
    """

    # REPETIMOS SEGÚN LA CANTIDAD DE VECINOS NECESARIOS
    
    for i in range(cantidad_vecinos):
        
        # REASIGNAMOS LOS BLOQUES MAS LEJANOS A LOS SHELTERS ASIGNADOS DE FORMA ALEATORIA PARA OBTENER SOLUCIONES VECINAS

        asignados = list(reordenar_lista(sheltersAsignados))

        print("Vecino " + str(i))

        # PROBLEMA: EL DICCIONARIO CAMBIA, A PESAR DE USAR UN COPY.
        # En la primera iteración se utiliza bien la solucion temporal copiada (la que se le quitaron los puntos más lejanos de cada shelter)
        # En las siguientes iteraciones se utiliza la solución temporal modificada (resultado de la iteración anterior)
        # Cada iteración debe comenzar con la solucion sin los bloques lejanos ya que estos son reasignados

        temp = temp_solved.copy()

        print("\nMostrarndo copia solucion")
        for shelter in temp:
            bloques = temp.get(shelter)
            print("\n" + str(shelter.getName()) + ": ")
            for bloque in bloques:
                print("- " + bloque.getName())

        solved = reasignar_recursive(bloques_lejanos, asignados, temp).copy()

        # SETEAMOS LOS DATOS DEL NUEVO VECINO Y LO AGREGAMOS A LA LISTA DE VECINOS

        new_vecino = solution
        new_vecino.setSolucion(solved)
        distancia_total_vecino = new_vecino.calcularDistanciaTotal()
        new_vecino.setTotalDistance (distancia_total_vecino)
        lista_vecinos.append(new_vecino)

    return lista_vecinos

    

def hill_climbing (solucion_inicial, t_max):

    t = 0

    best_solution = solucion_inicial
    local_solution = solucion_inicial

    while ( t < t_max):

        print ("\nIteracion: " + str(t))

        Local = False       

        while ( Local == False ):

            vecinos = obtenerVecinos(local_solution)

            for vecino in vecinos:

                distancia_vecino = vecino.getTotalDistance()
                distancia_local = local_solution.getTotalDistance()

                print("DV: " + str(distancia_vecino) + "  DL: " + str(distancia_local))     # SE MUENTRAN LA DITACIA DEL VECINO A REVISAR Y LA DISTANCIA LOCAL ACTUAL

                if (distancia_vecino < distancia_local):
                    local_solution = vecino
                else:
                    Local = True
        
        print ("\nMejor distancia local: " + str(local_solution.getTotalDistance()))

        if (local_solution.getTotalDistance() < best_solution.getTotalDistance()):
            best_solution = local_solution
        else: best_solution = best_solution
        
        t = t + 1

    return best_solution


def rep_solucion_main ():

    solucion_inicial = const_solucion_main(I, J, n, d)

    print("Inicial")

    solucion_inicial.mostrar_solucion()

    print("----------------------------------------------------------------")

    #print("Distancia solucion inicial: " + str(solucion_inicial.getTotalDistance())+"\n")

    vecinos = obtenerVecinos(solucion_inicial)

    i = 0
    for vecino in vecinos:
        print("----------------------------------------------------------------")
        print("\n\nV"+str(i))
        vecino.mostrar_solucion()
        i = i + 1

    #solucion_inicial.mostrar_solucion()

    #mejor_solucion = hill_climbing(solucion_inicial, 1)
    #mejor_distancia = mejor_solucion.getTotalDistance()

    #print("\n\nMejor distancia: " + str(mejor_distancia))



rep_solucion_main()