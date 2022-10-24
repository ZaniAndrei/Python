def numeroRegistros(arquivo):
    print("CO")

def registryRead(arquivo, meio):
    print("ZZZ")

def buscaBinaria(arquivo, chave):
    inicio = 0
    fim = numeroRegistros(arquivo) - 1
    while(inicio <= fim):
        meio = (inicio + fim)/2
        reg = registryRead(arquivo, meio)
        if(reg == chave):
            return reg
        elif(reg < chave):
            fim = meio - 1
        else:
            inicio = meio + 1
    return None

def chaveCanonica(linha):
    registro = linha.split("|")
    
    temp = registro[0] + registro[1]
    temp = temp.replace(" ", "")
    temp = temp.upper()
    #retirar espaco em branco e colocar tudo maiusculo
    return temp

def main():
    arquivo = open("herois.txt", "r+")
    for linha in arquivo:
        key = chaveCanonica(linha)
        busca = buscaBinaria(arquivo, key)
    

if __name__ == '__main__':
    main()
