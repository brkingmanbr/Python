class Cliente():
    def __init__(self, nome, telefone):
        self.__nome = nome
        self.__telefone = telefone
    def setNome(self, nome):
        self.__nome = nome
    def getNome(self):
        return self.__nome
    def setTelefone(self, telefone):
        self.__telefone = telefone
    def getTelefone(self):
        return self.__telefone
    def resumo(self):
        return self.__nome, self.__telefone
if __name__ == '__main__':
    c = Cliente('Jailson Mendes', 123456)
    print(c.resumo())
    print(c.getNome())
    print(c.getTelefone())
