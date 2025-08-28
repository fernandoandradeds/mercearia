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

class DaoEstoque:

    @classmethod
    def salvar(cls, produto: Produtos, quantidade):
        with open('estoque.txt', 'a') as file:
            file.writelines(produto.nome + '|' + produto.preco + '|' + produto.categoria + '|' + str(quantidade))
            file.writelines('\n')

    @classmethod
    def ler(cls):
        with open('estoque.txt', 'r') as file:
            cls.estoque = file.readlines()

        cls.estoque = list(map(lambda x: x.replace('\n', ''), cls.estoque))
        cls.estoque = list(map(lambda x: x.split('|'), cls.estoque))
        est = []
        if len(cls.estoque) > 0:
            for i in cls.estoque:
                est.append(Estoque(Produtos(i[0], i[1], i[2]), i[3]))
        return est

class DaoFornecedor:

    @classmethod
    def salvar(cls, fornecedor: Fornecedor):
        with open('fornecedores.txt', 'a') as file:
            file.writelines(fornecedor.nome + '|' + fornecedor.cnpj + '|' + fornecedor.telefone + '|' + fornecedor.categoria)
            file.writelines('\n')

    @classmethod
    def ler(cls):
        with open('fornecedores.txt', 'r') as file:
            cls.fornecedor = file.readlines()

        cls.fornecedor = list(map(lambda x: x.replace('\n', ''), cls.fornecedor))
        cls.fornecedor = list(map(lambda x: x.split('|'), cls.fornecedor))
        forn = []
        for i in cls.fornecedor:
            forn.append(Fornecedor(i[0], i[1], i[2], i[3]))
        return forn

class DaoPessoa:

    @classmethod
    def salvar(cls, pessoa: Pessoa):
        with open('clientes.txt', 'a') as file:
            file.writelines(pessoa.nome + '|' + pessoa.telefone + '|' + pessoa.cpf + '|' + pessoa.email + '|' + pessoa.endereco)
            file.writelines('\n')

    @classmethod
    def ler(cls):
        with open('clientes.txt', 'r') as file:
            cls.pessoa = file.readlines()

        cls.pessoa = list(map(lambda x: x.replace('\n', ''), cls.pessoa))
        cls.pessoa = list(map(lambda x: x.split('|'), cls.pessoa))
        pes = []
        for i in cls.pessoa:
            pes.append(Pessoa(i[0], i[1], i[2], i[3], i[4]))
        return pes

class DaoFuncionario:

    @classmethod
    def salvar(cls, funcionario: Funcionario):
        with open('funcionarios.txt', 'a') as file:
            file.writelines(funcionario.clt + '|' + funcionario.nome + '|' + funcionario.telefone + '|' + funcionario.cpf + '|' +
                            funcionario.email + '|' + funcionario.endereco + '|' + str(funcionario.salario) + '|' + funcionario.cargo)
            file.writelines('\n')

    @classmethod
    def ler(cls):
        with open('funcionarios.txt', 'r') as file:
            cls.funcionario = file.readlines()

        cls.funcionario = list(map(lambda x: x.replace('\n', ''), cls.funcionario))
        cls.funcionario = list(map(lambda x: x.split('|'), cls.funcionario))
        func = []
        for i in cls.funcionario:
            func.append(Funcionario(i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7]))
        return func
