class Banco():
        def __init__(self, nome):
            self.nome = nome
            self.clientes=[]
            self.contas=[]

        def novo_cliente(self, cliente):
            self.clientes.append(cliente)
        def lista_cliente(self):
            lista = ''
            for c in self.clientes:
                lista = lista+'\n'+c.getNome()
            return lista
        def busca_cliente(self, nome):
            try:
                return self.clientes.index(nome)
            except ValueError:
                return False
        
        def abre_conta(self, conta):
            self.contas.append(conta)
        def lista_conta(self):
            for c in self.contas:
                c.resumo()
if __name__ == '__main__':
    x = Banco('')
    x.novo_cliente('jão')
    print(x.busca_cliente('jão'))
    print(x.busca_cliente('joão'))
