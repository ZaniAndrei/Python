def bubblesort(vetor, escolha):
    trocou = True
    i_max = len(vetor)
    trocas = 0
    while trocou == True:
        if escolha == 'crescente':
            trocou = False
            for i in range(0,i_max-1):
                if vetor[i] > vetor[i+1] and i != (i_max - 1):
                    vetor[i+1], vetor[i] = vetor[i],vetor[i+1]
                    trocas = trocas + 1
                    print("Trocou " + str(vetor[i]) + " por " + str(vetor[i+1]) + '\n' + str(vetor)+ '\n') 
                    trocou = True
        elif escolha == 'decrescente':
            trocou = False
            for i in range(0,i_max-1):
                if vetor[i] < vetor[i+1] and i != (i_max - 1):
                    vetor[i+1], vetor[i] = vetor[i],vetor[i+1]
                    trocas = trocas + 1
                    print("Trocou " + str(vetor[i]) + " por " + str(vetor[i+1]) + '\n' + str(vetor) + '\n') 
                    trocou = True
    print("Trocou " + str(trocas) + " vezes")                   
vetor = [27, 98, 49, 59, 3, 32, -42, 28, 33, 31, 63, 100, -1, 61, 57]
bubblesort(vetor, 'crescente')

