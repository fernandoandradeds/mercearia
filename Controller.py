from Models import Categoria, Estoque, Produtos, Fornecedor, Pessoa, Funcionario, Venda
from DAO import DaoCategoria, DaoEstoque, DaoFornecedor, DaoPessoa, DaoFuncionario, DaoVenda
from datetime import datetime


class ControllerCategoria:

    def cadastrarCategoria(self, novaCategoria):
        x = DaoCategoria.ler()
        if any(i.categoria == novaCategoria for i in x):
            print("Categoria já existe!")
        else:
            DaoCategoria.salvar(novaCategoria)
            print("Categoria cadastrada com sucesso!")

    def removerCategoria(self, categoriaRemover):
        x = DaoCategoria.ler()
        nova = [i for i in x if i.categoria != categoriaRemover]
        if len(nova) == len(x):
            print("Categoria não encontrada!")
        else:
            with open('categoria.txt', 'w') as file:
                for i in nova:
                    file.write(i.categoria + '\n')
            print("Categoria removida com sucesso!")

    def listarCategorias(self):
        return DaoCategoria.ler()


class ControllerEstoque:

    def adicionarProduto(self, nome, preco, categoria, quantidade):
        estoque = DaoEstoque.ler()
        for item in estoque:
            if item.produto.nome.lower() == nome.lower():
                print("Produto já existe no estoque!")
                return
        produto = Produtos(nome, preco, categoria)
        DaoEstoque.salvar(produto, quantidade)
        print(f"Produto '{nome}' adicionado ao estoque!")

    def removerProduto(self, nome):
        estoque = DaoEstoque.ler()
        novo = [i for i in estoque if i.produto.nome.lower() != nome.lower()]
        if len(novo) == len(estoque):
            print("Produto não encontrado!")
        else:
            with open('estoque.txt', 'w') as file:
                for i in novo:
                    file.write(f"{i.produto.nome}|{i.produto.preco}|{i.produto.categoria}|{i.quantidade}\n")
            print(f"Produto '{nome}' removido do estoque!")

    def listarEstoque(self):
        return DaoEstoque.ler()

    def buscarProduto(self, nome):
        estoque = DaoEstoque.ler()
        for item in estoque:
            if item.produto.nome.lower() == nome.lower():
                return item
        return None


class ControllerVenda:

    def realizarVenda(self, produto_nome, vendedor, comprador, quantidade):
        estoque = DaoEstoque.ler()
        item_estoque = None
        for item in estoque:
            if item.produto.nome.lower() == produto_nome.lower():
                item_estoque = item
                break

        if not item_estoque:
            print("Produto não encontrado no estoque!")
            return

        qtd_disponivel = int(item_estoque.quantidade)
        qtd_venda = int(quantidade)

        if qtd_venda > qtd_disponivel:
            print(f"Estoque insuficiente! Disponível: {qtd_disponivel}")
            return

        venda = Venda(item_estoque.produto, vendedor, comprador, qtd_venda)
        DaoVenda.salvar(venda)

        nova_qtd = qtd_disponivel - qtd_venda
        novo_estoque = []
        for item in estoque:
            if item.produto.nome.lower() == produto_nome.lower():
                novo_estoque.append(Estoque(item.produto, nova_qtd))
            else:
                novo_estoque.append(item)

        with open('estoque.txt', 'w') as file:
            for i in novo_estoque:
                file.write(f"{i.produto.nome}|{i.produto.preco}|{i.produto.categoria}|{i.quantidade}\n")

        print(f"Venda registrada! Total: R$ {float(item_estoque.produto.preco) * qtd_venda:.2f}")

    def listarVendas(self):
        return DaoVenda.ler()


class ControllerFornecedor:

    def cadastrarFornecedor(self, nome, cnpj, telefone, categoria):
        fornecedores = DaoFornecedor.ler()
        if any(f.cnpj == cnpj for f in fornecedores):
            print("Fornecedor com esse CNPJ já cadastrado!")
            return
        fornecedor = Fornecedor(nome, cnpj, telefone, categoria)
        DaoFornecedor.salvar(fornecedor)
        print(f"Fornecedor '{nome}' cadastrado com sucesso!")

    def listarFornecedores(self):
        return DaoFornecedor.ler()


class ControllerCliente:

    def cadastrarCliente(self, nome, telefone, cpf, email, endereco):
        clientes = DaoPessoa.ler()
        if any(c.cpf == cpf for c in clientes):
            print("Cliente com esse CPF já cadastrado!")
            return
        cliente = Pessoa(nome, telefone, cpf, email, endereco)
        DaoPessoa.salvar(cliente)
        print(f"Cliente '{nome}' cadastrado com sucesso!")

    def listarClientes(self):
        return DaoPessoa.ler()


class ControllerFuncionario:

    def cadastrarFuncionario(self, clt, nome, telefone, cpf, email, endereco, salario, cargo):
        funcionarios = DaoFuncionario.ler()
        if any(f.cpf == cpf for f in funcionarios):
            print("Funcionário com esse CPF já cadastrado!")
            return
        funcionario = Funcionario(clt, nome, telefone, cpf, email, endereco, salario, cargo)
        DaoFuncionario.salvar(funcionario)
        print(f"Funcionário '{nome}' cadastrado com sucesso!")

    def listarFuncionarios(self):
        return DaoFuncionario.ler()
