
def deleteRegister(jogos, chave):
    #retorna booleano 
    print("sfd")

def storageCompactor(jogos, compactado):
    #deus nao sei
    print("sdflsdlfs")

def chaveCanonica(linha):
    registro = linha.split("|")
    game = Game(nome = registro[0], ano = registro[4]) 
    
    temp = game.getNome() + game.getAno()
    temp = temp.replace(" ", "")
    temp = temp.upper()
    #retirar espaco em branco e colocar tudo maiusculo
    return temp


class Game:
    #construtor do objeto game
    def __init__(self, nome = None, ano = None):
        self.nome = nome
        self.ano = ano

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
   

def main():
    jogos = open("jogos.txt", "r")
    lineCount = 0
    #text = jogos.read()
    text = jogos.readlines()
    #print(text)
    for linha in text:
        print(chaveCanonica(linha))
        #print(game.getNome())
        #print(game.getAno())
    #print(text)
    #print(chaveCanonica(jogos))

if __name__ == '__main__':
    main()    
