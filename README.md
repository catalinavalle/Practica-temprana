# Resumen
Realización de trabajo investigativo basado en el ruteo de vehículos (VRP) dada la necesidad de transportar grandes volúmenes de personas con mascotas afectadas en situaciones de desastres naturales. En este caso particular se consideran situaciones de terremoto y posible tsunami. Cada grupo de personas debe ser transportado a un refugio, preferentemente Pet-Friendly. Para ello se implementó un modelo matemático AMPL y optimizado con Gurobi. Se implementó ademas un generador de prueba con un código Python. Dcas instancias fueron ejecutadas en un servidor dedicado. A partir de estos resultados se realiza un análisis de las características de las instancias y sus respectivas dificultades de resolución. A partir del análisis de complejidad de los casos de prueba, se propone una heurística con el objetivo de disminuir los tiempos de respuesta. Esto quedó documentado en un articulo en formato paper, escrito en LaTex. Todos los códigos y archivos utilizados se encuentran disponibles en el presente repositorio.



## Versiones finales de los archivos utilizados:

### Generador:
* **generador_v5.3.py**     - Genera una instancia de prueba.
* **generarTodo_v5.3.sh**   - Genera muchas instancias de prueba.
              
### Solver:     
* **modelo_kocatepe.mod**   - Modelo matematico utilizado.
* **prueba.run**            - Resuelve una instancia de prueba.
* **correrTodo.sh**         - Resuelve muchas instancias de prueba.
              
### Heurística:
* **lector_v1.py**          - Lee una instancia de prueba.
* **const_solucion_v5.py**  - Construye un a solución aleatoria respetando las restricciones del modelo.
* **rep_solucion_v2.py**    - Aplica una heuristica que consiste en reasignar los bloques más lejanos a cada shelter.
* **rep_solucion_v3.py**    - Aplica una heuristica que consiste en reasignar los bloques aleatorios a cada shelter.

