class Banco():
        def __init__(self, nome):
            self.nome = nome
            self.cliente=[]
            self.contas=[]
        def abre_conta(self, conta):
            self.contas.append(conta)
        def lista_conta(self):
            for c in self.contas(self):
                c.resumo()
                
