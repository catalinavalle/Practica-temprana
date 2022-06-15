# Datos {Conjuntos y parametros}
# Se definen los conjuntos del modelo
set I;							# number of census block groups
set J;							# number of all shelters
set K;							# number of all designated shelters {pet-friendly or SpNS}.

# Se definen los parametros del modelo (cantidad de refugios a utilizar, coordenadas, distancia entre refugios y bloques de personas a rescatar, capacidad de cada refugio, cantidad de personas an cada bloque.
param N;									# number of shelters to be used, defined by the operator
param coordX{i in I union J};
param coordY{i in I union J};

param d{i in I, j in J}  >= 0;				# travel cost between the population block group i and the shelter at location j
param C{j in J} >= 0;						# capacity of the shelter at j, by total number of people
param P{i in I} >= 0;						# demand at point i

# Se definen las variables (no estoy segura cual es cual pero funciona jajaja)
var X{i in I, j in J} binary; 				# binary variable, 1 if the population block group is assigned to the shelter at j, 0 otherwise
var Y{j in J} binary;						# binary variable, 1 if the population block group is assigned to the shelter at j, 0 otherwise

# Se define la funcion objetivo
minimize FO: sum {j in J, i in I} d[i,j]*X[i,j];

# Se definen las restricciones

# R1: Each designated shelter {pet-friendly or SpNS} is fully utilized
R1 {j in K}: Y[j] = 1;

# R2: A census block group cannot be assigned to a shelter that is not designated for use
R2 {i in I, j in J}: X[i,j] <= Y[j];

# R3: Every population block group assigned to a one and only one shelter
R3 {i in I}: sum {j in J} X[i,j] == 1;

# R4: Number of shelters is set to a user defined value, N
R4: sum {j in J} Y[j] <= N;

# R5: For each shelter, assigned demand {in persons} should not exceed the capacity of the shelter
R5 {j in J}: sum {i in I} P[i]*X[i,j] <= C[j];
