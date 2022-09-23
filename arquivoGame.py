def escritaTamanhosFixos(arquivo, jogo):
    print("aiii")
def escritaCamps(arquivo, jogo, n) :
    print(" ")

def escritaBytes(file, game) :
    print(" ")

def escritaDelimitador(file, game) :
    print(" ")


def leituraTamanhosFixos(arquivo, jogo):
    print(" ")
def leituraCamps(arquivo, jogo, n):
    print(" ")
def leituraBytes(arquivo, jogo):
    print(" ")
def leituraDelimitador(arquivo, jogo):        
    print("dfsa")


class Game:
    #construtor do objeto game
    def __init__(self, nome = None, genero = None, plataforma = None, ano = None, classificacao = None, preco = None, midia = None, tamanho = None, produtora = None):
        self.nome = nome
        self.genero = genero
        self.plataforma = plataforma
        self.ano = ano
        self.classificacao = classificacao
        self.preco = preco
        self.midia = midia
        self.tamanho = tamanho
        self.produtora = produtora
    #nome
    def setNome(self, nome):
        self.nome = nome

    def getNome(self):
        return self.nome
    #ano
    def setAno(self, ano):
        self.ano = ano
    def getAno(self):
        return self.ano
    #genero
    def setGenero(self, genero):
        self.genero = genero
        
    def getGenero(self):
        return self.genero
    #plataforma
    def setPlataforma(self, plataforma):
        self.plataforma = plataforma
        
    def getPlataforma(self):
        return self.plataforma    
    #
    def setNome(self, nome):
        self.nome = nome
        
    def getNome(self):
        return self.nome


def main():
    arquivo = open("entrada.txt")
    #g1 = Game(nome = "sseei")
    #print(g1.getNome())
    #print(g1.getAno())
    text = arquivo.read()
    
    #while arquivo.readline() != -1:
    linha = text.split("|")
    

    j = 0

    for i in range(0, len(linha)): 
        listaAtributos[j] = linha[i]
        print(listaAtributos[j])
        print("############")
        j += 1 
        if(j == 9):
            j = 0


    print(linha)
    #print(len(sim))


listaAtributos = ["nome", "genero", "plataforma", "ano", "classificacao", "preco", "midia", "tamanho", "produtora"]


if __name__ == '__main__':
    main()
