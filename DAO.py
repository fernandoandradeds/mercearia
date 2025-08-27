from Models import *

class DaoCategoria:
    
    @classmethod
    def salvar(cls, categoria):
        with open('categoria.txt', 'a') as file:
            file.writelines(categoria)
            file.writelines('\n')

    @classmethod
    def ler(cls):
        with open('categoria.txt', 'r') as file:
            cls.categoria = file.readlines()

        cls.categoria = list(map(lambda x: x.replace('\n', ''), cls.categoria))

        cat = []
        for i in cls.categoria:
            cat.append(Categoria(i))

        return cat

class DaoVenda:

    @classmethod
    def salvar(cls, venda: Venda):
        with open('venda.txt', 'a') as file:
            file.writelines(venda.itensVendidos.nome + '|' + venda.itensVendidos.preco + '|' + venda.itensVendidos.categoria + '|' +
                            venda.vendedor + '|' + venda.comprador + '|' + str(venda.quantidadeVendida) + '|' +
                            venda.data)
            file.writelines('\n')
    
    @classmethod
    def ler(cls):
        with open('venda.txt', 'r') as file:
            cls.venda = file.readlines()

        cls.venda = list(map(lambda x: x.replace('\n', ''), cls.venda))
        cls.venda = list(map(lambda x: x.split('|'), cls.venda))
        vend = []
        for i in cls.venda:
            vend.append(Venda(Produtos(i[0], i[1], i[2]), i[3], i[4], i[5], i[6]))
        return vend

x = DaoVenda.ler()
print(x[0].itensVendidos.nome)  # Teste de leitura do arquivo venda.txt
