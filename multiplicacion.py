print("Programa para multiplicar matrices")

##Ingreso de las dimensiones de la primera matriz
numMatriz1F = int(input("Introduce el numero de la fila de la primera matriz: "))
numMatriz1C = int(input("Introduce el numero de la columna de la primera matriz: "))

##Ingreso de los elementos de la primera matriz
matriz1 = []
for i in range(numMatriz1F):
    matriz1.append([])
    for j in range(numMatriz1C):
        valor = int(input("Fila {}, Columna {}: ".format(i+1, j+1)))
        matriz1[i].append(valor)        

##Ingreso de las dimensiones de la segunda matriz
numMatriz2F = int(input("Introduce el numero de la fila de la segunda matriz:"))
while(numMatriz2F!=numMatriz1C):
    print("Para multiplicar las matrices la fila de la segunda columna debera tener la misma dimension que la columna de la primera matriz")
    numMatriz2F = int(input("Reingrese el numero de la fila: "))
numMatriz2C = int(input("Introduce el numero de la columna de la segunda matriz: "))

##Ingreso de los elementos de la segunda matriz
matriz2 = []
for i in range(numMatriz2F):
    matriz2.append([])
    for j in range(numMatriz2C):
        valor = int(input("Fila {}, Columna {}: ".format(i+1, j+1)))
        matriz2[i].append(valor)

##Vista de los valores de las dos matrices 
print()
print("Elementos de la primera matriz")
for i in matriz1:
    print("[", end= " ")
    for valor in i:
        print("{}".format(valor), end=" ")
    print("]")
print()
print("Elementos de la segunda matriz")
for i in matriz2:
    print("[", end= " ")
    for valor in i:
        print("{}".format(valor), end=" ")
    print("]")

##Crecion de la matriz resultado dandole la dimension de las matrices 1 y 2
matrizr=[]
for i in range(len(matriz1)):
    matrizr.append([])
    for j in range(len(matriz2[0])):
        matrizr[i].append(0)

##Multiplicacion de las matrices
for i in range(len(matriz1)):
    for j in range(len(matriz2[0])):
        for k in range(len(matriz1[0])):
            matrizr[i][j] +=matriz1[i][k] * matriz2[k][j]

print()
print("Resultado de la multiplicacion matriz")
for i in matrizr:
    print("[", end= " ")
    for valor in i:
        print("{}".format(valor), end=" ")
    print("]")
print()


