from lector_v1 import main
from const_solucion_v4 import const_solucion_main
from const_solucion_v4 import calcularCapacidadUtilizada
from const_solucion_v4 import Solucion

import random as rd
import sys


instancia = str(sys.argv[1])
mostrar_procedimiento = int ((sys.argv[2]))

I, J, d, n = main(instancia)


def obtenerVecinos(solution):

    lista_vecinos = []

    sheltersAsignados = solution.getSheltersAsignados()
    cantidad_vecinos = len(sheltersAsignados)

    for i in range(cantidad_vecinos):                       # creamos los vecinos
        new_vecino = const_solucion_main(0, I, J, n, d)
        lista_vecinos.append(new_vecino)

    temp_solution_solved = solution.getSolucion()
    temp_sheltersAsignados = sheltersAsignados

    bloques_lejanos = []

    # OBTENEMOS LOS BLOQUES MÁS LEJANOS DE CADA REFUGIO EN UNA LISTA Y LOS ELIMINAMOS DEL REFUGIO AL QUE FUE ASIGNADO

    for shelter in temp_sheltersAsignados:              # se revisan todos los shelters asignados
        bloques = temp_solution_solved.get(shelter)     # se obtiene la lista de bloques asignados en el shelter   
        bloque_lejano_distance = 0

        for bloque in bloques:          # Se busca el bloque mas lejano al shelter
            current_dist = d.get((bloque.getName(), shelter.getName()))

            if (current_dist > bloque_lejano_distance):
                bloque_lejano_distance = current_dist
                bloque_mas_lejano = bloque
        
        temp_solution_solved.get(shelter).remove(bloque_mas_lejano)     # elimina el bloque del shelter
        bloques_lejanos.append(bloque_mas_lejano)                       # agrega el bloque a la lista de lejanos


    # REPETIMOS SEGÚN LA CANTIDAD DE VECINOS NECESARIOS
    
    for i in range(len(sheltersAsignados)):

        temp_solution_solved = solution.getSolucion()
        temp_sheltersAsignados = solution.getSheltersAsignados()
        temp_lejanos = bloques_lejanos

        j = 0

        # REASIGNAMOS LOS BLOQUES MAS LEJANOS A LOS SHELTERS ASIGNADOS DE FORMA ALEATORIA PARA OBTENER SOLUCIONES VECINAS

        while (j < len(sheltersAsignados)):

            randRef = rd.randrange(0, len(temp_sheltersAsignados))      #seleccionamos un shelter aleatorio
            refugio = temp_sheltersAsignados[randRef] 

            randBloque = rd.randrange(0, len(temp_lejanos))             #seleccionamos un  bloque aleatorio en la lista de bloques lejanos
            bloque = temp_lejanos[randBloque] 

            capacidad_utilizada = calcularCapacidadUtilizada(temp_solution_solved.get(refugio))     # checamos la capacidad utilizada en el refugio
            capacidad_refugio = refugio.getCapacity()                                               # checamos la capacidad del refugio

            if( capacidad_utilizada <= capacidad_refugio):  # si entra, lo agregamos

                temp_solution_solved[refugio].append(bloque)
                temp_lejanos.remove(bloque)                     # se elimina el bloque de la lista de lejanos
                temp_sheltersAsignados.remove(refugio)          # se elimina el refugio de la lista de refugios asignados

                j = j + 1


        # SETEAMOS LOS DATOS DEL VECINO IESIMO DE LA LISTA DE VECINOS

        lista_vecinos[i].setSolucion(temp_solution_solved)
        distancia_total_vecino = lista_vecinos[i].calcularDistanciaTotal()
        lista_vecinos[i].setTotalDistance (distancia_total_vecino)
        lista_vecinos[i].setSheltersAsignados (sheltersAsignados)

        print("V" + str(i) + "   dist: " + str(lista_vecinos[i].getTotalDistance()))


    return lista_vecinos

    

def hill_climbing (solucion_inicial, t_max):

    t = 0

    best_solution = solucion_inicial

    while ( t < t_max):

        print ("\nIteracion: " + str(t))

        Local = False
        local_solution = const_solucion_main(0, I, J, n, d)

        while ( Local == False ):

            vecinos = obtenerVecinos(local_solution)

            #i = 0

            for vecino in vecinos:

                #print("it" + str(t) + " - V" + str(i) + "   dist: " + str(vecino.getTotalDistance()))
                #i = i + 1

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
    solucion_inicial = const_solucion_main(0, I, J, n, d)

    print("Distancia solucion inicial: " + str(solucion_inicial.getTotalDistance()))

    mejor_solucion = hill_climbing(solucion_inicial, 1)
    mejor_distancia = mejor_solucion.getTotalDistance()

    print("\n\nMejor distancia: " + str(mejor_distancia))



rep_solucion_main()