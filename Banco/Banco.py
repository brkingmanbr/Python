from Cliente import Cliente
class Banco():
        def __init__(self, nome):
            self.nome = nome
            self.clientes=[]
            self.contas=[]
            self.LISTA = ''

        def novo_cliente(self, cliente):
            self.clientes.append(cliente)
        def lista_cliente(self):
            lista = ''
            for c in self.clientes:
                print("c: ",c)
                lista = lista+'\n'+str(
                        c.getNome()
                        ) 
            self.LISTA = lista
            return lista
        def busca_cliente(self, nome):
            try:
                return self.clientes.index(nome)
            except ValueError:
                return "Nenhum Cliente Adicionado Ainda"
        
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
    print(x.lista_cliente())
