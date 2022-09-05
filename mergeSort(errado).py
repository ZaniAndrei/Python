def mergeSort(vetor, inicio, fim):
    if(inicio < fim):
        meio = round((inicio + fim)/2)
        mergeSort(vetor,inicio,meio)
        mergeSort(vetor,meio+1,fim)
        mergeAux(vetor,inicio,meio,fim)

def mergeAux(vetor, inicio, meio, fim):
    v_aux = []
    p1 = inicio
    p2 = meio + 1
    while(p1 <= meio and p2 <= fim):
        if(vetor[p1] < vetor[p2]):
            v_aux.append(vetor[p1])
            p1 = p1 + 1
        else:
            v_aux.append(vetor[p2])
            p2 = p2 + 1
    if p1 == meio:
        for i in range(0, fim):
            vetor[i] = v_aux[i]
    else:
        for i in range(0, fim):
            vetor[i] = v_aux[i]
      

vetor = [ 4, -38, -60, 36, 33, 10, 20, 69, -80, -39, 35, -34, -45, -100, -13]
inicio = 0
fim = len(vetor) - 1

mergeSort(vetor, inicio, fim)
print(vetor)
