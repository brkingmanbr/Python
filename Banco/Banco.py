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
            lista +='\n%s Telefone: %s'%(c.getNome(), c.getTelefone())
        return lista
    def busca_cliente(self, nome):
        try:
            return self.clientes.index(nome)
        except ValueError:
            return "Nenhum"
    
    def abre_conta(self, conta):
        self.contas.append(conta)
    def lista_conta(self):
        for c in self.contas:
            c.resumo()
if __name__ == '__main__':
    from Controle import Controle
    c = Controle()
    c.cli_nome('nome')
    c.cli_telefone('telefone')
    c.Banco.novo_cliente(c.cliente())
    print('Banco.lista_cliente() %s'%c.Banco.lista_cliente())
    
