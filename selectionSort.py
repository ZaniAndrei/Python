def selectionSort(vetor, opcao):
    n = len(vetor)
    iteracoes = 0
    if(opcao == "crescente"):
        for k in range(0, n - 1):
            iteracoes += 1
            menor = k
            for i in range(k, n):
                if vetor[i] < vetor[menor]:
                    menor = i
            if k != menor:
                vetor[menor], vetor[k] = vetor[k], vetor[menor]
                print("Trocou " + str(vetor[menor]) + " por " + str(vetor[k]) + '\n' + str(vetor) + '\n')
        print("Houveram " + str(iteracoes) + " iterações")        
    if(opcao == "decrescente"): 
        for k in range(0, n - 1):
            iteracoes += 1
            maior = k
            for i in range(k, n):
                if vetor[i] > vetor[maior]:
                    maior = i
            if k != maior:
                vetor[maior], vetor[k] = vetor[k], vetor[maior]   
                print("Trocou " + str(vetor[maior]) + " por " + str(vetor[k]) + '\n' + str(vetor) + '\n')        
        print("Houveram " + str(iteracoes) + " iterações")    
               
vetor = [4, -38, -60, 36, 33, 10, 20, 69, -80, -39, 35, -34, -45, -100, -13]       
selectionSort(vetor, "crescente")
print(vetor)
