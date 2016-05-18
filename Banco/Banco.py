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
            lista +='\n%s Tel: %s'%(c.getNome(), c.getTelefone())
        return lista
    def busca_cliente(self, nome):
        lista = []
        for elemento in self.clientes:
            lista.append(elemento.getNome())
        try:
            return self.clientes[lista.index(nome)].getNome()
        except ValueError:
            return False
        
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
    
