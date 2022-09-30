import re

def grep(file,  comparacao):
    indice = 0
    listaIndices = []
    listaCompleta = []
    text = file.readlines()
    for line in text:
        indice += 1 
        if re.search(comparacao, line):
            teste = str(indice)+ ': ' + line 
            #print(line)
            #print(teste)
            listaIndices.append(indice) 
            listaCompleta.append(teste)               
    return listaIndices, listaCompleta       


def main():
    file = open("jogo.txt")
    comparacao = "Teen"
    indices, lista = grep(file, comparacao)
    for i in range(0, len(indices)): 
        print(indices[i])
    print("\n")
    for i in range(0, len(lista)):    
        print(lista[i])

if __name__ == '__main__':
    
    main()
