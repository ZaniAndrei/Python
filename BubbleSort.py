def bubblesort(vetor, escolha):
    trocou = True
    i_max = len(vetor)

    while trocou == True:
        if escolha == 'crescente':
            trocou = False
            for i in range(0,i_max-1):
                print(i)
                if vetor[i] > vetor[i+1] and i != (i_max - 1):
                    temp =  vetor[i+1]
                    vetor[i+1] = vetor[i]
                    vetor[i] = temp
                    trocou = True
        elif escolha == 'decrescente':
            trocou = False
            for i in range(0,i_max-1):
                print(i)
                if vetor[i] < vetor[i+1] and i != (i_max - 1):
                    temp =  vetor[i+1]
                    vetor[i+1] = vetor[i]
                    vetor[i] = temp
                    trocou = True
vetor = [27, 98, 49, 59, 3, 32, -42, 28, 33, 31, 63, 100, -1, 61, 57]
bubblesort(vetor, 'crescente')
print(vetor)
