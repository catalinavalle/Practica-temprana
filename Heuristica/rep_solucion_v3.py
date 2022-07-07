# V3: reasignacion de bloques aleatorios

from lector_v1 import reader_main
from const_solucion_v5 import const_solucion_main
from const_solucion_v5 import calcularCapacidadUtilizada
from const_solucion_v5 import Solucion

import random as rd
import sys
import time


instancia = str(sys.argv[1])
s = int(sys.argv[2])
rd.seed(s)
iteraciones = int(sys.argv[3])

I, J, d, n = reader_main(instancia)


def eliminarBloquesAleatoriaos (asignados, solved):

    bloques_eliminados = []
    temp = copy_dict(solved)

    for shelter in asignados:              # se revisan todos los shelters asignados
        bloques = temp.get(shelter)     # se obtiene la lista de bloques asignados en el shelter   
        bloque_eliminar = rd.choice(bloques)
        
        temp.get(shelter).remove(bloque_eliminar)     # elimina el bloque del shelter
        bloques_eliminados.append(bloque_eliminar)         # agrega el bloque a la lista de lejanos
    
    return bloques_eliminados, temp


def reordenar_lista(lista):
    temp_lista = list(lista)
    lista_reordenada = []
    for i in range(len(temp_lista)):
        element = rd.choice(temp_lista)
        lista_reordenada.append(element)
        temp_lista.remove(element)
    return(lista_reordenada)


def reasignar (lejanos, asignados, solved):

    temp_asignados = list(reordenar_lista(asignados))
    temp_lejanos = list(reordenar_lista(lejanos))
    temp_solved = copy_dict(solved)

    for refugio in temp_asignados:

        for bloque in temp_lejanos:

            capacidad_temp = calcularCapacidadUtilizada(temp_solved.get(refugio)) + bloque.getDemand()   # checamos la capacidad utilizada en el refugio
            capacidad_refugio = refugio.getCapacity()                                               # checamos la capacidad del refugio

            if( capacidad_temp <= capacidad_refugio):  # si entra, lo agregamos

                temp_solved[refugio].append(bloque)
                temp_lejanos.remove(bloque)                     # se elimina el bloque de la lista de lejanos

    if (len(temp_lejanos) == 0):
        return temp_solved
    else:
        return False


def reasignar_ciclo (bloques_lejanos, sheltersAsignados, temp_solved):

    solved = False

    while (solved == False):
        solved = reasignar (bloques_lejanos, sheltersAsignados, temp_solved)     

    return solved


def copy_dict (diccionario):

    temp_dict = {}

    for j in J:
        temp_dict.setdefault(j, [])

    for shelter in temp_dict:
        bloques = diccionario.get(shelter)
        temp_dict[shelter] = list(bloques)

    return temp_dict
   

def obtenerVecinos(solution):

    lista_vecinos = []

    sheltersAsignados = list(solution.getSheltersAsignados())
    cantidad_vecinos = len(sheltersAsignados) 

    temp_solution_solved = solution.getSolucion()

    temp_solved = {}

    # OBTENEMOS LOS BLOQUES MÁS LEJANOS DE CADA REFUGIO EN UNA LISTA Y LOS ELIMINAMOS DEL REFUGIO AL QUE FUE ASIGNADO

    bloques_lejanos, temp_solved = eliminarBloquesAleatoriaos(sheltersAsignados, temp_solution_solved)

    # REPETIMOS SEGÚN LA CANTIDAD DE VECINOS NECESARIOS

    for i in range(cantidad_vecinos):

        solved = reasignar_ciclo(list(bloques_lejanos), list(sheltersAsignados), copy_dict(temp_solved))

        # SETEAMOS LOS DATOS DEL NUEVO VECINO Y LO AGREGAMOS A LA LISTA DE VECINOS

        distanciaTotal = 0
        
        for shelter in solved:
            bloques = solved.get(shelter)
            for bloque in bloques:
                dist = d.get((bloque.getName(), shelter.getName()))
                distanciaTotal = distanciaTotal + dist

        new_vecino =  Solucion(I, J, n, d, solved, distanciaTotal, sheltersAsignados)

        lista_vecinos.append(new_vecino)


    return lista_vecinos


def hill_climbing (solucion_inicial, t_max):

    t = 0

    best_solution = solucion_inicial
    local_solution = solucion_inicial

    while ( t < t_max):

        #print ("\nIteracion: " + str(t))

        Local = False       

        while ( Local == False ):

            vecinos = obtenerVecinos(local_solution)

            for vecino in vecinos:

                distancia_vecino = vecino.getTotalDistance()
                distancia_local = local_solution.getTotalDistance()

                #print("DV: " + str(distancia_vecino) + "  DL: " + str(distancia_local))     # SE MUENTRAN LA DITACIA DEL VECINO A REVISAR Y LA DISTANCIA LOCAL ACTUAL

                if (distancia_vecino < distancia_local):
                    local_solution = vecino
                else:
                    Local = True
        
        #print ("\nMejor distancia local: " + str(local_solution.getTotalDistance()))

        if (local_solution.getTotalDistance() < best_solution.getTotalDistance()):
            best_solution = local_solution
            #print("\n Nuevo best: " + str(best_solution.getTotalDistance()))
        else: best_solution = best_solution
        
        t = t + 1

    return best_solution


def rep_solucion_main ():

    solucion_inicial = const_solucion_main(I, J, n, d)

    inicio = time.time()

    mejor_solucion = hill_climbing(solucion_inicial, iteraciones)

    fin = time.time()

    fo = mejor_solucion.getTotalDistance()
    tiempo = int(fin - inicio)

    f = open ('resumen_heuristica.txt','a')
    f.write(str(instancia) + ' ' + str(s) + ' ' + str(iteraciones) + ' ' + str(fo) + ' ' + str(tiempo))
    f.close()

    return
    
rep_solucion_main()