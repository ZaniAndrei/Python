##nsertionSort (V, TAM)
#2. Para cada posição i entre 1 e N-1, (i = i+1) faça:
#3.     auxiliar = valor na posição i
#4.     j = i -1
#5.     Enquanto (j >= 0) && (auxiliar < V[j]):
#6.         V[j+1] = V[j]
#7.         j = j -1
#8. V[j+1] = auxiliar

def insertionSort(vetor):
    tamanho = len(vetor)
    contador = 0
    for i in range(1, tamanho):
        aux = vetor[i]
        j = i - 1
        contador = contador + 1
        while(j >= 0 and aux < vetor[j]):
            contador = contador + 1
            vetor[j+1] = vetor[j]
            j = j - 1
        vetor[j+1] = aux
            
    print(contador)
        



vetor = [27, 98, 49, 59, 3, 32, -42, 28, 33, 31, 63, 100, -1, 61, 57]
#vetor = [-42, -1, 3, 27, 28, 31, 32, 33, 49, 57, 59, 61, 63, 98, 100]
#vetor = [14,13,12,11,10,9,8,7,6,5,4,3,2,1,0]

insertionSort(vetor)
print(vetor)
